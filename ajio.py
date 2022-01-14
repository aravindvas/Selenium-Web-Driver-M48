from selenium import webdriver

urLL = "https://www.ajio.com/teamspirit-embroidered-hoodie-with-kangaroo-pockets/p/441112315006"

chr_drvr = "D:\Softwares\chromedriver_win32\chromedriver.exe"
drvr = webdriver.Chrome(executable_path=chr_drvr)

drvr.get(url=urLL)
pr = drvr.find_element_by_class_name("prod-sp")
print(pr.text)
# drvr.close()
drvr.quit()