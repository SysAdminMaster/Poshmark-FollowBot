from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from os import system

email = ""
password = ""


def check_exists_by_xpath(xpath):
    try:
       driver.find_element(By.XPATH, xpath)
    except:
        return False
    return True

with webdriver.Chrome() as driver:

    driver.get('https://poshmark.com/login')


    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'login_form[username_email]'))
    )


    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'login_form[password]'))
    )


    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-primary'))
    )

    email_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()


    feed_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div/div[2]/div[7]/div[1]/div/div/div[1]/a'))
    )


    feed_title.click()


    followers_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/div[1]/div/div[2]/div/div/nav/ul/li[3]/div'))
    )


    followers_button.click()


    index = 1
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:

        follow_button_xpath = f'/html/body/div[1]/main/div[2]/div/div[3]/div/div[{index}]/button'
        follow_button_available = check_exists_by_xpath(follow_button_xpath)

        if not follow_button_available:
           
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            new_height = driver.execute_script('return document.body.scrollHeight')

            if new_height == last_height:
                break

            last_height = new_height
        else:
     
            follow_button = driver.find_element(By.XPATH, follow_button_xpath)
            follow_button.click()
            index += 1

      
            system(f'title Total followed [{index}]')


        time.sleep(1.5)


    input('Press Enter to exit')
