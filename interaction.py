from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# urLL = "https://en.wikipedia.org/wiki/Main_Page"
urLL = "https://www.amazon.in/ref=nav_logo"

chr_drvr = "D:\Softwares\chromedriver_win32\chromedriver.exe"
drvr = webdriver.Chrome(executable_path=chr_drvr)

drvr.get(url=urLL)
# tm = drvr.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# tm = drvr.find_element_by_css_selector("#articlecount a")
# tm.click()

# allp = drvr.find_element_by_link_text("All portals")
# allp.click()

# srh = drvr.find_element_by_name("search")
# srh.send_keys("python")
# srh.send_keys(Keys.ENTER)
# srh = drvr.find_elements_by_css_selector("a-button-text button")
# srh.send_keys(Keys.ENTER)
srh = drvr.find_element_by_name("email")
srh.send_keys("919491654127")
srh.send_keys(Keys.ENTER)
srh = drvr.find_element_by_name("password")
srh.send_keys("Aravindvas@1997")
srh.send_keys(Keys.ENTER)


# drvr.close()
# drvr.quit()