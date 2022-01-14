from selenium import webdriver

urLL = "https://www.amazon.in/dp/B08LRFZ4LZ/ref=sspa_dk_hqp_detail_aax_0?psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFLRTVCNTNLVjdXRjcmZW5jcnlwdGVkSWQ9QTAwMzM4NDAyMDdEV01aR0JXRDJLJmVuY3J5cHRlZEFkSWQ9QTAzOTUyMjUxMkpDMVVaTzg0RkJTJndpZGdldE5hbWU9c3BfaHFwX3NoYXJlZCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

chr_drvr = "D:\Softwares\chromedriver_win32\chromedriver.exe"
drvr = webdriver.Chrome(executable_path=chr_drvr)

drvr.get(url=urLL)
pr = drvr.find_element_by_id("priceblock_ourprice")
print(pr.text)
# drvr.close()
drvr.quit()