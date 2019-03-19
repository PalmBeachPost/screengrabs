from selenium import webdriver
from PIL import Image
import os
from time import strftime, sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.chrome.service as service

# pip install Pillow
# pip install selenium
# Manually install PhantomJS


masterdirectory = "x:/screengrabs"
PhantomJSlocation = 'C:/helpers/phantomjs.exe'
chromedriverlocation = 'c:/helpers/chromedriver.exe'
chromebinarylocation = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'


# So you can have as many sites as you want. Each goes in a parenthesis: (URL, abbreviation)
mysites = [
    ("https://www.palmbeachpost.com", "pb"),
    ("https://www.palmbeachdailynews.com", "dn")
    ]


#delay = 50      # Time to wait to finish loading AJAX-y things after main page loads.   
delay = 50      # Time to wait to finish loading AJAX-y things after main page loads.       

datepath = strftime("/%Y/%m/%d/")
filesuffix = strftime("_%Y-%m-%d_%H%M")

if not os.path.exists(masterdirectory + datepath):
    os.makedirs(masterdirectory + datepath)

browser = webdriver.PhantomJS(executable_path = PhantomJSlocation)
browser.set_window_size(1300, 2500);

# service = service.Service(chromedriverlocation)
# service.start()
# capabilities = {'chrome.binary': chromebinarylocation}
# driver = webdriver.Remote(service.service_url, capabilities)

#options = webdriver.ChromeOptions()
# options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#options.binary_location = chromedriverlocation
#options.add_argument('headless')
#options.add_argument('window-size=1300x1920')
#driver = webdriver.Chrome(chrome_options=options)
        
for site in mysites:
    URL, abbreviation = site
    print("Working on " + URL)
    browser.get(URL)
    sleep(delay)
    print("Thing should have downloaded by now. Scrolling down.")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")       # activate scroll-over stuff like photo gallery
    browser.execute_script("window.scrollTo(0, 0);")     # Then return up top for header.
    print("Waiting for Ajax-y trigger-y stuff to go.")
    sleep(delay)
    browser.execute_script("window.scrollTo(0, 0);")     # Then return up top for header.
    print("Saving " + URL)
    browser.save_screenshot(masterdirectory + "/screenie.png")
    im = Image.open(masterdirectory + '/screenie.png')
    # im = im.convert("RGB")
    im.save(masterdirectory + datepath + abbreviation + filesuffix + ".png", optimize=True)

browser.quit()
