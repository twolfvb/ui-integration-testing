from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_driver():
    caps = DesiredCapabilities.FIREFOX

    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", '/home/jonathan/Desktop')
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")

    # Tell the Python bindings to use Marionette.
    # This will not be necessary in the future,
    # when Selenium will auto-detect what remote end
    # it is talking to.
    caps["marionette"] = True

    # Path to Firefox DevEdition or Nightly.
    # Firefox 47 (stable) is currently not supported,
    # and may give you a suboptimal experience.
    #
    # On Mac OS you must point to the binary executable
    # inside the application package, such as
    # /Applications/FirefoxNightly.app/Contents/MacOS/firefox-bin
    caps["binary"] = "/usr/bin/firefox"

    driver = webdriver.Firefox(
        executable_path='geckodriver',
        firefox_profile=profile,
        capabilities=caps,
    )

    return driver
