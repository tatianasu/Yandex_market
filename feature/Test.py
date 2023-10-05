from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pytest
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_yandex_search(driver):
    driver.get('https://market.yandex.ru')
    driver.find_element(By.ID, 'hamburger').click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul > li:nth-of-type(5) > a > span")))
    driver.find_element(By.CSS_SELECTOR, "ul > li:nth-of-type(5) > a > span").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_2jsCq")))
    driver.find_element(By.CLASS_NAME, "_2jsCq").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_1PSTa")))
    driver.find_element(By.CLASS_NAME, "_1PSTa").click()

    filters_btm = driver.find_element(By.CSS_SELECTOR, "aside#searchFilters > div > div:nth-of-type(4)  a> button")
    driver.execute_script("arguments[0].scrollIntoView();", filters_btm)
    filters_btm.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#glprice > div > div:nth-of-type(2) > input")))
    driver.find_element(By.CSS_SELECTOR, "div#glprice > div > div:nth-of-type(2) > input").click()
    driver.find_element(By.CSS_SELECTOR, "div#glprice > div > div:nth-of-type(2) > input").send_keys(20000)


    #Выбираем первые 5 марок
    mark1 = driver.find_element(By.XPATH, "//div[@data-filter-id='7893318']//div[@class='_8yOdX'][1]//input[@type='checkbox']")
    driver.execute_script("arguments[0].scrollIntoView();", mark1)
    driver.execute_script("arguments[0].click();", mark1)
    mark2 = driver.find_element(By.XPATH, "//div[@data-filter-id='7893318']//div[@class='_8yOdX'][2]//input[@type='checkbox']")
    driver.execute_script("arguments[0].click();", mark2)
    mark3 = driver.find_element(By.XPATH,
                                "//div[@data-filter-id='7893318']//div[@class='_8yOdX'][3]//input[@type='checkbox']")
    driver.execute_script("arguments[0].click();", mark3)
    mark4 = driver.find_element(By.XPATH,
                                "//div[@data-filter-id='7893318']//div[@class='_8yOdX'][4]//input[@type='checkbox']")
    driver.execute_script("arguments[0].click();", mark4)
    mark5 = driver.find_element(By.XPATH,
                                "//div[@data-filter-id='7893318']//div[@class='_8yOdX'][5]//input[@type='checkbox']")
    driver.execute_script("arguments[0].click();", mark5)

    time.sleep(4)
    #выбираем диагональ
    btm_dioganal = driver.find_element(By.XPATH, '//button[@aria-controls="14805766"]')
    driver.execute_script("arguments[0].scrollIntoView();", btm_dioganal)
    btm_dioganal.click()
    driver.find_element(By.XPATH, '//div[@data-auto="14805766"]//input[@data-auto= "range-filter-input-min"]').click()
    driver.find_element(By.XPATH, '//div[@data-auto="14805766"]//input[@data-auto= "range-filter-input-min"]').send_keys(3)

    # нажимаем на кнопку "показать предложения"
    result_filters= driver.find_element(By.XPATH, '//a[@data-autotest-id="result-filters-link"]')
    driver.execute_script("arguments[0].scrollIntoView();", result_filters)
    result_filters.click()

    #считаем количество смартфонов
    count = 0
    n = 1

    for i in range(1,100):
        try:
            elements = driver.find_element(By.XPATH, f"//div[@data-index='{i}']")
            if elements != None:
                driver.execute_script("arguments[0].scrollIntoView();", elements)
                count += 1
        except:
            break
    print('Количество смартфонов на странице:', count)

    # Находим последний смартфон и запоминаем
    element = driver.find_element(By.XPATH, f"//div[@data-index='{count}']")
    # получаем ссылку на новый смартфон
    new_attribute = element.get_dom_attribute('href')
    btm = driver.find_element(By.XPATH, "//button[@data-autotest-id = 'dprice']")
    driver.execute_script("window.scrollTo(0, 0);")
    btm.click()
