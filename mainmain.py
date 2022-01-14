from selenium import webdriver

urLL = "https://www.python.org"

chr_drvr = "D:\Softwares\chromedriver_win32\chromedriver.exe"
drvr = webdriver.Chrome(executable_path=chr_drvr)

drvr.get(url=urLL)
tm = drvr.find_elements_by_css_selector(".event-widget time")
nm = drvr.find_elements_by_css_selector(".event-widget li a")
events = {}

# for i in tm:
#     print(i.text)
# for j in nm:
#     print(j.text)
for n in range(len(tm)):
    events[n] = {
        "time": tm[n].text,
        "name": nm[n].text
    }

print(events)
# drvr.close()
drvr.quit()