# Script by Chuma, Nepta and Dany
# This script in Selenium-Python will just go to any moddb mod and download it.
# This will be done in a free mod, and it will just be an experiment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# Driver_path = dp to summarize
dp = "chromedriver"
chrome_options = Options()
# Initialize the Chrome webdriver
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(dp, options=chrome_options)
# go to Moddb website
driver.get("https://www.moddb.com/")
# find the search bar and enter "Dark-Life 2"
search_bar = driver.find_element(By.ID, 'sitesearch')  # "sitesearch"
search_bar.send_keys("Dark-Life 2")
search_bar.submit()
darklife_link2 = driver.find_element(By.XPATH, "//a[contains(normalize-space(), 'Dark Life 2 demo')]") #Find in the website the demo
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
#This is just a "failsafe" to verify the current url the bot is going through.
darklife_link3 = driver.find_element(By.XPATH, "//a[contains(normalize-space(), 'Download now')]")
darklife_link3.click()


# This process of window handle must be done because moddb open different tabs.
# On changing window handle and finding download and clicking it, the file will download itself.


#As a template if you want to try with another mod is
# Step one : get in moddb.
# Step two : set up the name of the mod and send it through the keys , then click.
# Step three : be aware of new windows to do the new window handle.
# Step four : Click on your desired mod
# Step five and hopefully final : Set up the calls to download it and click it

# I think from the deplegable button / menu of the main website it can be done for sure.
# But we decided to do it this way.
