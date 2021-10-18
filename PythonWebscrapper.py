from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=chrome_options)
driver.get("http://nytimes.com")
topNews = driver.find_elements_by_css_selector("a[class='css-dyj8mj']")
topNewsLinks = []
for i in range(len(topNews)):
    topNewsLinks.append(topNews[i].get_attribute('href'))

parent = driver.current_window_handle


driver.get("http://twitter.com/login")
sleep(3)

for ID in driver.window_handles:
    if ID != parent:
        driver.switch_to.window(ID)

element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

username = driver.find_element_by_css_selector('input[name="username"]')
username.clear()
username.send_keys("brookessecondemail@gmail.com")
username.send_keys(Keys.RETURN)

element2 = WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

username = driver.find_element_by_css_selector('input[name="password"]')
username.clear()
username.send_keys("jwkgR6tBN6esR2Q")
username.send_keys(Keys.RETURN)

#===========================================================================================

for i in range(5):
    element3 = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox']"))
    )
    tweet = driver.find_elements_by_css_selector("div[role='textbox']")[0]
    tweet.send_keys(topNewsLinks[i])
    click = driver.find_element_by_css_selector("div[data-testid='tweetButtonInline']")
    click.click()
    sleep(10)




