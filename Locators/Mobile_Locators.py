from Config.config import my_prod
##--ACTIONS--##
skip               =  '//android.widget.TextView[@text="Skip"]'
allow              =  '//android.widget.Button[@resource-id="com.flipkart.android:id/not_now_button"]'
conti              =  '//android.widget.TextView[@text="Continue"]'
apply              =  '//android.widget.TextView[@text="Apply"]'

##--CART_LOGIN--##
go_to_cart         =  '//android.widget.TextView[@text="Go to cart"]'
add_to_cart        =  '//android.widget.FrameLayout[@resource-id="com.flipkart.android:id/main_content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView'
add_to_cart1       =  '//android.widget.TextView[@text="Add to cart"]'
remove_item        =  '(//android.widget.TextView[@text="Remove"])[1]'
remove             =  '(//android.widget.TextView[@text="Remove"])'
phone              =  '//android.widget.EditText[@content-desc="Phone Number"]'
Placeorder         =  '//android.widget.TextView[@text="Place order "]'
Phn_input          =  '//*contains[@text, "+91 "]'

##--FILTERS--##
PriceFilterClass   =  '//android.widget.TextView[@text="Filter"]'
PriceMaxFilter     =  '//android.widget.TextView[@text="Price"]'
PriceMaxValue      =  '//android.widget.TextView[@text="Rs. 3000 and Above"]'
brand              =  '//android.widget.TextView[@text="Brand"]'
adidas             =  '//android.widget.TextView[@text="ADIDAS"]'

##--SEARCH--##        
categories         =  '//android.widget.TextView[@text="Categories"]'
SearchButton       =  '//android.widget.ImageView[@content-desc="Search"]'
SearchFieldLocator =  '//android.widget.EditText[@text="Search for products"]'
SearchButton1      =  '//android.widget.TextView[@text="shoes for women"]'


##--PRODUCT--##
search_query    =  my_prod()
try:   
    search_query == '1'
    prod = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]'
except:
    pass
try: 
    search_query == '2'
    prod = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]'
except:
    pass
try: 
    search_query == '3'
    prod = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]'
except:
    pass
try:
    search_query == '4'
    prod = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]'
except:
    pass


