import pytest
from Keyword.test_on_usr_def_key import SearchPage, FilterPage, SelectPage, CartPage, Login 
from Config.config import driver

def test_Flipkart(driver):
    ##--SEARCH--##
    SearchPage(driver).test_searching()

    ##--FILTER--##
    FilterPage(driver).test_filter()

    ##--SELECT--##
    SelectPage(driver).test_selecting()

    ##--CART--##
    CartPage(driver).test_cart_and_login()

    ##--FAIL--##
    Login(driver).login()    
