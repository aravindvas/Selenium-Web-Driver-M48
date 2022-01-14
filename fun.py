from selenium import webdriver

urLL = "https://paytm.com/flights/flightSearch/HYD-Hyderabad/BOM-Mumbai/1/0/0/E/2021-06-24"

chr_drvr = "D:\Softwares\chromedriver_win32\chromedriver.exe"
drvr = webdriver.Chrome(executable_path=chr_drvr)

drvr.get(url=urLL)
# pr = drvr.find_element_by_css_selector(".YMlIz FpEdX jLMuyc div")
pr = drvr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div[8]/div/div')
print(pr.text, pr)
# drvr.close()
drvr.quit()