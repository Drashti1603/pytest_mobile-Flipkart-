from selenium import webdriver

# Specify the full path to ChromeDriver executable
chromedriver_path = '/usr/bin/chromedriver'

# Initialize Chrome webdriver with ChromeDriver executable path
driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.gethttps://admin-demo.nopcommerce.com/Admin')
search_box = driver.find_element_by_name('q')
search_box.send_keys('Selenium')
search_box.submit()

# Remember to close the browser after you're done
driver.quit()
