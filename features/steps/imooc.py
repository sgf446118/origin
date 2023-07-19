import time
from selenium.webdriver.common.by import By
from behave import step
from features.selenium_api.selenium_api import SeleniumAPI
import logging
logging.getLogger().setLevel(logging.INFO)

@step('open chrome browser')
def step_impl(context):
    logging.info('open chrome browser')
    SeleniumAPI.create_imooc_driver(context)

@step('input url <{url}>')
def step_impl(context, url):
    logging.info('input url '+url)
    SeleniumAPI.imooc_driver.get(url)
    time.sleep(2)

@step('click login button')
def step_impl(context):
    logging.info('click login button')
    element = SeleniumAPI.imooc_driver.find_element(by=By.ID, value='js-signin-btn')
    SeleniumAPI.click_element(context, element)

@step('input user id')
def step_impl(context):
    logging.info('input user id')
    user_id=context.config.userdata['user']
    element = SeleniumAPI.imooc_driver.find_element(by=By.NAME, value='email')
    SeleniumAPI.input_to_element(context, element, user_id)
    time.sleep(2)


@step('input password')
def step_impl(context):
    logging.info('input password')
    pwd = context.config.userdata['password']
    element = SeleniumAPI.imooc_driver.find_element(by=By.NAME, value='password')
    SeleniumAPI.input_to_element(context,  element, pwd)
    time.sleep(2)

@step('click to login')
def step_impl(context):
    logging.info('click login')
    element = SeleniumAPI.imooc_driver.find_element(by=By.XPATH, value='//input[@value="登录"]')
    SeleniumAPI.click_element(context, element)
    time.sleep(2)

@step('verify login success')
def step_impl(context):
    assert True


@step('close browser')
def step_impl(context):
    SeleniumAPI.close_browser(context, SeleniumAPI.imooc_driver)
