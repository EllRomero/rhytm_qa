from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def main():
    url = 'https://demoqa.com/'
    driver = webdriver.Chrome()
    # Загрузка веб-страницы
    driver.maximize_window()
    # Открытие урл
    driver.get(url=url)
    #Ожидание 10 сек, если не найден элемент
    wait = WebDriverWait(driver, 10)
    # Ожидание, пока элемент на странице не будет видимым
    wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, 'card-body'))).click()
    # Из левой панели выбираем Check box
    driver.find_element(By.CLASS_NAME, 'left-pannel'
                        ).find_element(By.ID, 'item-1').click()
    # Открываем директорию home
    driver.find_element(By.CLASS_NAME, 'rct-collapse-btn').click()
    # Парсим список тэгов li
    el = driver.find_elements(By.CSS_SELECTOR,
                            'li.rct-node.rct-node-parent.rct-node-collapsed')
    # Открываем последний (директория Downloads)
    el[-1].find_element(By.TAG_NAME, 'button').click()
    # Выбираем файл Word File.doc
    driver.find_element(By.XPATH,
                        "//span[@class='rct-title' and text()='Word File.doc']"
                        ).click()
    # Парсим полученную надпись
    text = driver.find_element(By.ID, 'result').text
    print("Получаем :\n", text)


if __name__ == '__main__':
    main()
