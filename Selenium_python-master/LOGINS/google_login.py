from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def google_login():
    # my Email and Password are used , not the true ones.
    username = "Dhiadjebbi@gmail.com"
    password = "DDD123456"


    driver = webdriver.Chrome('../drivers/chromedriver.exe')

    # Open Google Accounts page
    driver.get('https://accounts.google.com/')

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'identifier'))
    )
    input_email = driver.find_element(By.NAME, 'identifier')
    input_email.send_keys(username)
    input_email.send_keys(Keys.ENTER)


    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'password'))
    )
    input_pass = driver.find_element(By.NAME, 'password')
    input_pass.send_keys(password)
    input_pass.send_keys(Keys.ENTER)


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div#gb'))
    )
    print('Logged in successfully!')

    
    input('Press Enter to close the browser...')
    driver.quit()

# Call the function to test the login process
google_login()
