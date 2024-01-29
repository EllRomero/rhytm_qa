import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver(drivers, headless):
    '''
    Инициализация браузера, который будет использоваться для тестирования.
    А так же дополнительная настройка в фоном режиме.
    Chrome по умолчанию.
    '''

    if drivers == 'chrome':
        if headless:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Chrome()
    elif drivers == 'edge':
        if headless:
            options = webdriver.EdgeOptions()
            options.add_argument('--headless')
            driver = webdriver.Edge()
        else:
            driver = webdriver.Firefox()
    elif drivers == 'firefox':
        if headless:
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            driver = webdriver.Firefox(options=options)
        else:
            driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


class TestHomePage:
    '''Класс для тестирования домашней страницы'''

    url = 'https://demoqa.com/'

    def test_load_home_page(self):
        '''
        Функция проверяет доступен ли данный URL.
        '''

        status = requests.get(self.url)
        assert status.status_code == 200, \
            f"URL {self.url} не был загружен, статус-код {status}"

    def test_find_elements(self, driver):
        '''Функция проверяет наличие Elements на странице.'''

        driver.get(self.url)
        element = driver.find_elements(By.CLASS_NAME, 'card-body')
        text = [el.text for el in element]
        assert 'Elements' in text, 'Elements не существует на странице.'

    def test_pos_elements(self, driver):
        '''Функция проверяет наличие текста Elements, в первом div.'''

        driver.get(self.url)
        element = driver.find_element(By.CLASS_NAME, 'card-body')
        assert element.text == 'Elements', \
                               'Elements не первый в списке'


class TestElementsPage:
    '''Класс для тестирования страницы elements.'''

    url = 'https://demoqa.com/elements'

    def test_load_elements_page(self):
        '''Функция проверяет доступен ли данный URL.'''

        status = requests.get(self.url)
        assert status.status_code == 200, \
            f"URL {self.url} не был загружен, статус-код {status} "

    def test_find_check_box(self, driver):
        '''Функция проверяет существует Check box на странице.'''

        driver.get(self.url)
        elements = driver.find_element(By.CLASS_NAME,'menu-list')
        elements = elements.find_elements(By.TAG_NAME, 'li')
        text = [el.text for el in elements]
        assert 'Check Box' in text, 'Check box не существует, в Elements'

    def test_pos_check_box(self, driver):
        '''Функция проверяет доступен ли данный CheckBox вторым из списка.'''

        driver.get(self.url)
        assert driver.find_element(By.CLASS_NAME, 'left-pannel'
                            ).find_element(By.ID, 'item-1').is_displayed(), \
                            'Checkbox не второй, в списке'

class TestCheckboxPage:
    '''Класс для тестирования страницы chekbox.'''

    url = 'https://demoqa.com/checkbox'

    def test_load_checkbox_page(self):
        '''Функция проверяет доступен ли данный URL.'''

        status = requests.get(self.url)
        assert status.status_code == 200, \
            f"URL {self.url} не был загружен, статус-код {status}"

    def test_find_dir_home(self, driver):
        '''Функция проверяет, существование директории Home.'''

        driver.get(self.url)
        text = driver.find_element(By.CLASS_NAME, 'rct-title').text
        assert text == 'Home', 'Директория home не была найдена'

    def test_find_dir_downloads(self, driver):
        '''Функция проверяет, существование директории Downloads.'''

        driver.get(self.url)
        driver.find_element(By.CLASS_NAME, 'rct-collapse-btn').click()
        elements = driver.find_elements(By.CLASS_NAME, 'rct-title')
        text = [el.text for el in elements]
        assert 'Downloads' in text, 'Директория Downloads не была найдена'

    def test_pos_dir_downloads(self, driver):
        '''Функция проверяет является директорию по счету 3,в каталоге home.'''

        driver.get(self.url)
        driver.find_element(By.CLASS_NAME, 'rct-collapse-btn').click()
        elements = driver.find_elements(By.CLASS_NAME, 'rct-text')
        text = elements[-1].text
        assert 'Downloads' == text, 'Директория Downloads не 3 по счету'


    def test_find_file_word(self, driver):
        '''Функция проверяет, существование файла Word File.doc'''

        driver.get(self.url)
        driver.find_element(By.CLASS_NAME, 'rct-collapse-btn').click()
        elements = driver.find_elements(By.CSS_SELECTOR,
                        'li.rct-node.rct-node-parent.rct-node-collapsed')
        elements[-1].find_element(By.TAG_NAME, 'button').click()
        elements = driver.find_elements(By.CLASS_NAME, 'rct-title')
        text = [el.text for el in elements]
        assert 'Word File.doc' in text, 'Файл Word File.doc не был найден'


    def test_check_alert_message(self, driver):
        '''Функция проверяет, вывод надписи в результате выбора Word File.'''

        driver.get(self.url)
        driver.find_element(By.CLASS_NAME, 'rct-collapse-btn').click()
        elements = driver.find_elements(By.CSS_SELECTOR,
                        'li.rct-node.rct-node-parent.rct-node-collapsed')
        elements[-1].find_element(By.TAG_NAME, 'button').click()
        driver.find_element(By.XPATH,
                    "//span[@class='rct-title' and text()='Word File.doc']"
                    ).click()
        text = driver.find_element(By.ID, 'result').text
        assert text == 'You have selected :\nwordFile'
