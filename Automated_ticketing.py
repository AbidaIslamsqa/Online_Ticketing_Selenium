from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
browser = "chrome"  # chrome, firefox, edge
driver = ''
if browser == "chrome":
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
elif browser == "firefox":
    driver = webdriver.Firefox()
elif browser == "edge":
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)
else:
    driver = webdriver.Chrome()

driver.get("https://ticketing.learnsqa.com/")
driver.maximize_window()
#Login by Admin or Agent
driver.find_element("xpath","(//a[normalize-space()='Login'])").click()
time.sleep(10)
driver.find_element(By.XPATH,"(//input[@id='email'])").clear()
driver.find_element(By.XPATH,"(//input[@id='email'])").send_keys("admin@admin.com")
driver.find_element(By.XPATH,"(//input[@id='password'])").clear()
driver.find_element(By.XPATH,"(//input[@id='password'])").send_keys("password")
driver.find_element(By.XPATH,"(//label[normalize-space()='Remember me'])").click()
driver.find_element(By.XPATH,"(//button[normalize-space()='Login'])").click()
time.sleep(10)
act_title=driver.title
exp_title="Support Ticketing"
if act_title==exp_title:
    print("Login test pass")
else:
    print("Login test fail")
driver.find_element(By.XPATH,"(//a[normalize-space()='User management'])").click()
time.sleep(10)
driver.find_element(By.XPATH,"//a[normalize-space()='Permissions']").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//option[@value='50'])").click()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("50")
driver.find_element(By.XPATH,"//a[normalize-space()='View']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='Back to list']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("51")
driver.find_element(By.XPATH,"//a[normalize-space()='Edit']").click()
time.sleep(5)
#Edit Permission With Unique Title
driver.get_screenshot_as_file("Previous_title.png")
driver.find_element(By.XPATH,"//input[@id='title']").clear()
driver.find_element(By.XPATH,"//input[@id='title']").send_keys("dashboard_access_admin")
driver.get_screenshot_as_file("Edited_title.png")
driver.find_element(By.XPATH,"//input[@value='Save']").click()
act_title=driver.title
exp_title="Support Ticketing"
if act_title==exp_title:
    print("Permission Edited & Saved with Unique Tile")
else:
    print("Permission Failed to Edit & Save with Unique Tile")
time.sleep(5)
#Edit with duplicate title
driver.find_element(By.XPATH,"//input[@type='search']").send_keys(50)
driver.find_element(By.XPATH,"//a[normalize-space()='Edit']").click()
driver.get_screenshot_as_file("before_edit.png")
driver.find_element(By.XPATH,"//input[@id='title']").clear()
driver.find_element(By.XPATH,"//input[@id='title']").send_keys("dashboard_access_admin")
driver.find_element(By.XPATH,"//input[@value='Save']").click()
time.sleep(5)
driver.get_screenshot_as_file("after_edit.png")#(permission 50,51 edited with same tile)
act_title=driver.title
exp_title="Support Ticketing"
if act_title==exp_title:
    print("Permission Edited & Saved with duplicate Tile is a BUG")
else:
    print("Permission Failed to Edit & Save with Duplicate Tile")

