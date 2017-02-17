import time

from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ( "Mozilla-5.0 (Windows NT 6.3; WOW64) AppleWebKit-537.36 (KHTML, like Gecko) Chrome-34.0.1847.137 Safari-537.36"
)


driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.set_window_size(1024, 768)

driver.save_screenshot('test.png')