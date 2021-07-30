from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Initialize Webdrivers In final build to get no window
"""
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
"""

driver = webdriver.Chrome()

driver.get("https://indentyourration.web.app/")
username_input = "/html/body/div/div/form/div/input[1]"
password_input = "/html/body/div/div/form/div/input[2]"
login_submit = "/html/body/div/div/form/div/button/div[1]"

# Monday
mon_breakfast = "/html/body/div/div/div[5]/div[3]/div[2]/button[1]"
mon_lunch = "/html/body/div/div/div[5]/div[3]/div[2]/button[2]"
mon_dinner = "/html/body/div/div/div[5]/div[3]/div[2]/button[3]"

mon_53 = "/html/body/div/div/div[5]/div[3]/div[2]/div/button[1]"
mon_200 = "/html/body/div/div/div[5]/div[3]/div[2]/div/button[2]"

# Tuesday
tue_breakfast = "/html/body/div/div/div[5]/div[4]/div[2]/button[1]"
tue_lunch = "/html/body/div/div/div[5]/div[4]/div[2]/button[2]"
tue_dinner = "/html/body/div/div/div[5]/div[4]/div[2]/button[3]"

tue_53 = "/html/body/div/div/div[5]/div[4]/div[2]/div/button[1]"
tue_200 = "/html/body/div/div/div[5]/div[4]/div[2]/div/button[2]"

# Wednesday
wed_breakfast = "/html/body/div/div/div[5]/div[5]/div[2]/button[1]"
wed_lunch = "/html/body/div/div/div[5]/div[5]/div[2]/button[2]"
wed_dinner = "/html/body/div/div/div[5]/div[5]/div[2]/button[3]"

wed_53 = "/html/body/div/div/div[5]/div[5]/div[2]/div/button[1]"
wed_200 = "/html/body/div/div/div[5]/div[5]/div[2]/div/button[2]"

# Thursday
thu_breakfast = "/html/body/div/div/div[5]/div[6]/div[2]/button[1]"
thu_lunch = "/html/body/div/div/div[5]/div[6]/div[2]/button[2]"
thu_dinner = "/html/body/div/div/div[5]/div[6]/div[2]/button[3]"

thu_53 = "/html/body/div/div/div[5]/div[6]/div[2]/div/button[1]"
thu_200 = "/html/body/div/div/div[5]/div[6]/div[2]/div/button[2]"

# Friday
fri_breakfast = "/html/body/div/div/div[5]/div[7]/div[2]/button[1]"
fri_lunch = "/html/body/div/div/div[5]/div[7]/div[2]/button[2]"
fri_dinner = "/html/body/div/div/div[5]/div[7]/div[2]/button[3]"

fri_53 = "/html/body/div/div/div[5]/div[7]/div[2]/div/button[1]"
fri_200 = "/html/body/div/div/div[5]/div[7]/div[2]/div/button[2]"

# Saturday
sat_breakfast = "/html/body/div/div/div[5]/div[8]/div[2]/button[1]"
sat_lunch = "/html/body/div/div/div[5]/div[8]/div[2]/button[2]"
sat_dinner = "/html/body/div/div/div[5]/div[8]/div[2]/button[3]"

sat_53 = "/html/body/div/div/div[5]/div[8]/div[2]/div/button[1]"
sat_200 = "/html/body/div/div/div[5]/div[8]/div[2]/div/button[2]"

# Sunday
sun_breakfast = "/html/body/div/div/div[5]/div[9]/div[2]/button[1]"
sun_lunch = "/html/body/div/div/div[5]/div[9]/div[2]/button[2]"
sun_dinner = "/html/body/div/div/div[5]/div[9]/div[2]/button[3]"

sun_53 = "/html/body/div/div/div[5]/div[9]/div[2]/div/button[1]"
sun_200 = "/html/body/div/div/div[5]/div[9]/div[2]/div/button[2]"

'''
# User Input goes here

# Login and sign up functions go here

# In line keyboard/Poll function goes here
'''
# Test list
option_list = [mon_breakfast, mon_lunch, mon_dinner, tue_breakfast, tue_lunch, tue_dinner, wed_breakfast, wed_lunch,
               wed_dinner, thu_breakfast, thu_lunch, thu_dinner, fri_breakfast, fri_lunch, fri_dinner, sat_breakfast,
               sat_lunch, sat_dinner, sun_breakfast, sun_lunch, sun_dinner]
loc_list = [mon_53, tue_53, wed_53, thu_53, fri_53, sat_53, sun_53]

# Test login
driver.find_element_by_xpath(username_input).send_keys("martinleejiakang")
driver.find_element_by_xpath(password_input).send_keys("m@rtinl33jiakang")
driver.find_element_by_xpath(login_submit).click()

WebDriverWait(driver, timeout=10).until(expected_conditions.url_to_be("https://indentyourration.web.app/dashboard"))

for i in option_list:
    driver.find_element_by_xpath(i).click()

for i in loc_list:
    driver.find_element_by_xpath(i).click()

"""

# Try and close should encapsulate finished code
try:
    driver.get("https://indentyourration.web.app/")
    username_input = "/html/body/div/div/form/div/input[1]"
    password_input = "/html/body/div/div/form/div/input[2]"
    login_submit = "/html/body/div/div/form/div/button/div[1]"
    driver.find_element_by_xpath(username_input).send_keys("martinleejiakang")
    driver.find_element_by_xpath(password_input).send_keys("m@rtinl33jiakang")
    driver.find_element_by_xpath(login_submit).click()

finally:
    driver.close()
"""
