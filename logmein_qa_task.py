from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import urllib3
import sys

# Parse input parameter (Chrome, Safari or Firefox)
input_browser = sys.argv[1]


def BrowserInit(browser):
	print(browser)

	if browser == 'Chrome' or 'chrome':

		driver = webdriver.Chrome(ChromeDriverManager().install())

	elif browser == 'Firefox' or 'firefox':

		driver = webdriver.geckodriver()

	# Set the targeted URL
	driver.get('https://www.seleniumeasy.com/test/')

	return driver

def TestRunner(browser):
	print('Tests will run on: ' + browser)

	# Test1 - Verify page title
	result1 = PageTitleVerTest(browser)
	print(result1)
	# Test2 - Get Total
	result2 = GetTotalTest(browser)
	print(result2)
	# Test3 - CheckBox
	result3 = CheckboxDemoTest(browser)
	print(result3)
	# Test4 = Input Form
	result4 = FormSubmitTest(browser)
	print(result4)

def PageTitleVerTest(target_browser):

	# Set the targeted URL
	driver = BrowserInit(target_browser)

	title = driver.title
	result = ""
	if  'Selenium Easy' in title:
		result = result + 'Verify page title test case is: PASSED!'
	else:
		result = result + 'Verify page title test case is: FAILED! The string is: ' + title

	driver.close()

	return result

def GetTotalTest(target_browser):

	# Set the targeted URL
	driver = BrowserInit(target_browser)

	result = ""
	button = driver.find_elements_by_xpath("//*[contains(text(), 'Input Forms')]")
	button[0].click()
	time.sleep(1)

	button2 = driver.find_elements_by_xpath("//*[contains(text(), 'Simple Form Demo')]")
	button2[0].click()
	time.sleep(1)

	sum1 = driver.find_element_by_id("sum1")
	sum1.send_keys("5")


	sum2 = driver.find_element_by_id("sum2")
	sum2.send_keys("6")


	sumbutton = driver.find_element_by_xpath("//button[contains(text(), 'Get Total')]")
	sumbutton.click()

	value = driver.find_element_by_id("displayvalue")

	if value.text == '11':
		result = result + 'Get Total test case is: PASSED!'
	else:
		result = result + 'Get Total test case is: FAILED! The string is: ' + value.text

	driver.close()

	return result

def CheckboxDemoTest(target_browser):
	
	# Set the targeted URL
	driver = BrowserInit(target_browser)

	result = ""

	button = driver.find_elements_by_xpath("//*[contains(text(), 'Input Forms')]")
	button[0].click()
	time.sleep(1)

	button2 = driver.find_elements_by_xpath("//*[contains(text(), 'Checkbox Demo')]")
	button2[0].click()
	time.sleep(1)

	checkbox = driver.find_element_by_id("isAgeSelected")
	checkbox.click()

	text2 = driver.find_element_by_id("txtAge")
	if text2.text == 'Success - Check box is checked':
		result = result + 'Check Demo test case is : PASSED!'
	else:
		result = result + 'Check Demo test case is: FAILED!'

	driver.close()

	return result

def FormSubmitTest(target_browser):

	# Set the targeted URL
	driver = BrowserInit(target_browser)

	result = ""

	button = driver.find_elements_by_xpath("//*[contains(text(), 'Input Forms')]")
	button[0].click()
	time.sleep(1)

	button2 = driver.find_elements_by_xpath("//*[contains(text(), 'Ajax Form Submit')]")
	button2[0].click()
	time.sleep(1)

	field1 = driver.find_element_by_id("title")

	field2 = driver.find_element_by_id("description")

	button5 = driver.find_element_by_id("btn-submit")
	button5.click()

	if button5.is_displayed() and field1.get_attribute('value') == '' and field2.get_attribute('value') == '':
		result = result + 'First part of the test case is: PASSED! \n'
	else: 
		result = result + 'First part of the test case is: FAILED! \n'

	field1.send_keys("Test1")
	field2.send_keys("Test2")
	button5.click()

	appr2 = driver.find_element_by_id("submit-control")
	time.sleep(2)
	if appr2.text == 'Form submited Successfully!':
		result = result + 'Second part of the test case is: PASSED!'
	else:
		result = result + 'Second part of the test case is: FAILED!'

	driver.close()

	return result
	
TestRunner(input_browser)