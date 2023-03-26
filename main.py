from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib.request

dp="chromedriver"
chrome_options= Options()

# initialize the Chrome webdriver
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(dp, options= chrome_options)

# go to Moddb website
driver.get("https://www.moddb.com/")

# find the search bar and enter "Dark-Life 2"
search_bar = driver.find_element(By.ID,'sitesearch')  #Corregido Chuma , era "sitesearch"
search_bar.send_keys("Dark-Life 2")
search_bar.submit()

# go to the Dark-Life 2 page
# Indev Chuma estas lineas
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select#Vorig_station"))).click()
#select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select#Vorig_station"))))

darklife_link = driver.find_element(By.XPATH,"//a[contains(text(),'dark life 2 mod for')]")
darklife_link.click()

# go to the Files section
files_link = driver.find_element_by_xpath("//a[contains(@href,'files')]")
files_link.click()

# download the demo file
demo_link = driver.find_element_by_xpath("//a[contains(@href,'dark-life-2-demo')]")
demo_url = demo_link.get_attribute("href")
urllib.request.urlretrieve(demo_url, "DarkLife2Demo.zip")

# close the webdriver
driver.quit()
#Note that you may need to modify the file path for the downloaded file ("DarkLife2Demo.zip") to save it to the desired location on your system. Also, make sure to have the urllib module imported for downloading the file.


#C:\Users\luism\Downloads is the download path
#Great! In that case, you can modify the urllib.request.urlretrieve line to the following:

#python
#Copy code
#urllib.request.urlretrieve(demo_url, r"C:\Users\luism\Downloads\DarkLife2Demo.zip")
#This will save the downloaded file to the specified path on your system.