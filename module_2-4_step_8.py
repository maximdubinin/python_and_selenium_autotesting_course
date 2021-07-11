import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
try:
    browser.get(link)
    book_button = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_button.click()

    answer = browser.find_element_by_id("answer")
    x = browser.find_element_by_id("input_value").text
    answer.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    submit = browser.find_element_by_id("solve")
    submit.click()
    time.sleep(10)
finally:
    browser.quit()

