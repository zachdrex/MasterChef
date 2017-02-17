import time

from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

print(str("  __  __           _             ____ _           __ "))
print(str(" |  \/  | __ _ ___| |_ ___ _ __ / ___| |__   ___ / _|"))
print(str(" | |\/| |/ _` / __| __/ _ \ '__| |   | '_ \ / _ \ |_ "))
print(str(" | |  | | (_| \__ \ ||  __/ |  | |___| | | |  __/  _|"))
print(str(" |_|  |_|\__,_|___/\__\___|_|   \____|_| |_|\___|_|  "))
print(str("                                                     "))
print(str("Splash Edition"))
print("")
time.sleep(5)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

url = input("Splash Page URL: ")
prox = input("Proxies? (Y/N): ")
username = input("Adidas Email: ")
password = input("Adidas Pass: ")
size = input("Shoe Size: ")


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ( "Mozilla-5.0 (Windows NT 6.3; WOW64) AppleWebKit-537.36 (KHTML, like Gecko) Chrome-34.0.1847.137 Safari-537.36"
)

driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.set_window_size(1024, 768)

driver.get("https://www.adidas.com/us/myaccount-create-or-login")
userform = driver.find_element_by_xpath('//*[@id="signinForm"]/fieldset/div[2]/div')
userform.send_keys(str(username))
passform = driver.find_element_by_xpath('//*[@id="signinForm"]/fieldset/div[3]/div')
passform.send_keys(str(password))

driver.find_element_by_xpath('//*[@id="signinForm"]/fieldset/div[5]').click()



#driver.save_screenshot('test.png')