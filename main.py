from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
dp = "chromedriver"
chrome_options = Options()
# initialize the Chrome webdriver
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(dp, options=chrome_options)
# go to Moddb website
driver.get("https://www.moddb.com/")
# find the search bar and enter "Dark-Life 2"
search_bar = driver.find_element(By.ID, 'sitesearch')  # "sitesearch"
search_bar.send_keys("Dark-Life 2")
search_bar.submit()
darklife_link2 = driver.find_element(
    By.XPATH, "//a[contains(normalize-space(), 'Dark Life 2 demo')]")
darklife_link2.click()
# get current window handle
p = driver.current_window_handle
# get first child window
chwd = driver.window_handles
for w in chwd:
    if w != p:
        driver.switch_to.window(w)
get_url = driver.current_url
print("The current url is:"+str(get_url))
darklife_link3 = driver.find_element(
    By.XPATH, "//a[contains(normalize-space(), 'Download now')]")
darklife_link3.click()
