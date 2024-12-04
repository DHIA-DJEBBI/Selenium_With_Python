from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def discord_login():
    # Example username and password for testing 
    username = "Dhiadjebbi"  
    password = "123456DDD"   


    driver = webdriver.Chrome()
    driver.maximize_window()


    driver.get('https://discord.com/login')

    # Wait for the login fields to load
    wait = WebDriverWait(driver, 30)
    try:
        
        username_field = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
        password_field = driver.find_element(By.NAME, 'password')
        username_field.send_keys(username)
        password_field.send_keys(password)

  
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

       
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "closeIcon-150W3V")))
        print("Login successful!")
    except TimeoutException:
        print("Timeout while waiting for login elements. Check your credentials or network connection.")
    except NoSuchElementException as e:
        print(f"Element not found: {e}")
    finally:
        
        driver.quit()

if __name__ == "__main__":
    discord_login()
