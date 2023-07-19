import time

from selenium import webdriver
import logging

logging.getLogger().setLevel(logging.INFO)

class SeleniumAPI():
    imooc_driver = None

    def create_imooc_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('start_maximized')
        prefs = {"download_prompt_for_download": False, "download.default_directory": 'D:\download'}
        options.add_experimental_option('prefs', prefs)
        driver_path = r'D:\drivers\chromedriver.exe'

        SeleniumAPI.imooc_driver = webdriver.Chrome(executable_path=driver_path, options=options)
        SeleniumAPI.imooc_driver.set_page_load_timeout(120)
        SeleniumAPI.imooc_driver.maximize_window()
        logging.info('Create imooc dirver success')
        time.sleep(2)

    def click_element(self, element):
        element.click()
        time.sleep(2)

    def input_to_element(self, element, text):
        element.send_keys(text)
        time.sleep(1)

    def close_browser(self, driver):
        driver.quit()
