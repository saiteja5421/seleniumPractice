from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# service_obj=Service("C:\\Users\\malip\\OneDrive\\Desktop\\chromedrivers\\chromedriver_win32\\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="C:\\Users\\malip\\OneDrive\\Desktop\\chromedrivers\\chromedriver_win32\\chromedriver.exe", options=options)
# driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//input[@name='name']").send_keys("saiteja")
# Select(driver.find_element(By.ID,"exampleFormControlSelect1")).select_by_visible_text("Female")
# WebDriverWait(driver,6).until(expected_conditions.presence_of_element_located(By.ID,""))


# driver.switch_to.alert

# action=ActionChains(driver)
# action.move_to_element(driver.find_element(By.ID,"")).perform()
# windowsOpened=driver.window_handles
# driver.switch_to.window(windowsOpened[1])

# driver.switch_to.frame("")
# driver.switch_to.default_content()

# driver.execute_script("window(ScrollBy(0,800)")



