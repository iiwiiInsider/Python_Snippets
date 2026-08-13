from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

def open_x_homepage():
    options = Options()
    options.add_argument("--start-maximized")

    # Use Selenium Manager (no chromedriver path required)
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://x.com/")
        # Wait for full page load
        WebDriverWait(driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")
        print("X homepage opened.")
        # keep browser open briefly so you can see it
        time.sleep(5)
    finally:
        driver.quit()

if __name__ == "__main__":
    open_x_homepage()
