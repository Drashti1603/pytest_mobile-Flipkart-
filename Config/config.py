import pytest
from selenium import webdriver
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
@pytest.fixture
def driver():
    
    appium_service = AppiumService()
    appium_service.start(port=4723, args=["--base-path", "/wd/hub"])


    capabilities = {
        "deviceName"     : "test",
        "platformName"   : "Android",
        "platformVersion": "12",
        "automationName" : "UiAutomator2",
        "appPackage"     : "com.flipkart.android",
        "appActivity"    : "com.flipkart.android.SplashActivity",
        "udid"           : "cdcfe431",
    }
    appium_server_url    =  'http://localhost:4723/wd/hub'
    capabilities_options =  UiAutomator2Options().load_capabilities(capabilities)
    driver               =  webdriver.Remote(command_executor=appium_server_url,options=capabilities_options)
    return driver


###--SEARCH ITEM NAME--###
def my_input():
    Item_to_search = "shoes"
    return Item_to_search

###--SIZE--###
def my_num():
    Num = '6'
    return Num

###--PRODUCT NUMBER--###
def my_prod():
    n = 'P2'
    return n   
    