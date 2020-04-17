from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from email.mime.text import MIMEText
from github import Github
import time
import urllib3
import sys
import smtplib, ssl
import os


# Parse input parameter (Chrome, Safari or Firefox)
input_browser = sys.argv[1]


def browserInit(browser):
	
	if browser == 'Chrome':

		driver = webdriver.Chrome(ChromeDriverManager().install())

	elif browser == 'Firefox':

		driver = webdriver.Firefox(executable_path="/<path>/geckodriver")

	elif browser == 'Safari':

		driver = browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver') 

	else:

		print('Selected browser is not supported, please choose another one!')
		exit()

	# Set the targeted URL
	driver.get('https://www.seleniumeasy.com/test/')

	return driver

def testRunner(browser):

	summary = 'Executed all of the test cases on: ' + browser + '\n'

	# Test1 - Verify page title
	result1 = pageTitleVerTest(browser)
	summary = summary + result1

	# Test2 - Get Total
	result2 = getTotalTest(browser)
	summary = summary + result2

	# Test3 - CheckBox
	result3 = checkboxDemoTest(browser)
	summary = summary + result3

	# Test4 = Input Form
	result4 = formSubmitTest(browser)
	summary = summary + result4

	email = sendMail(summary)
	print(email)

	file = createResultTxt(summary)
	print(file)


def pageTitleVerTest(target_browser):

	# Set the targeted URL
	driver = browserInit(target_browser)

	title = driver.title
	result = ""
	if  'Selenium Easy' in title:
		result = result + 'Verify page title test case is: PASSED! \n'
		print('Verify page title test case is: PASSED!')
	else:
		result = result + 'Verify page title test case is: FAILED! The string is: ' + title + '\n'
		print('Verify page title test case is: FAILED!')

	driver.quit()

	return result

def getTotalTest(target_browser):

	# Set the targeted URL
	driver = browserInit(target_browser)

	result = ""
	driver.find_elements_by_xpath("//*[contains(text(), 'Input Forms')]")[0].click()
	button2 = driver.find_element_by_xpath("//*[contains(text(), 'Simple Form Demo')]").click()

	sum1 = driver.find_element_by_id("sum1")
	sum1.send_keys("5")


	sum2 = driver.find_element_by_id("sum2")
	sum2.send_keys("6")


	driver.find_element_by_xpath("//button[contains(text(), 'Get Total')]").click()

	value = driver.find_element_by_id("displayvalue")

	if value.text == '11':
		result = result + 'Get Total test case is: PASSED! \n'
		print('Get Total test case is: PASSED!')
	else:
		result = result + 'Get Total test case is: FAILED! The string is: ' + value.text + '\n'
		print('Get Total test case is: FAILED!')

	driver.quit()

	return result

def checkboxDemoTest(target_browser):
	
	# Set the targeted URL
	driver = browserInit(target_browser)

	result = ""

	button = driver.find_elements_by_xpath("//*[contains(text(), 'Input Forms')]")[0].click()
	driver.find_element_by_xpath("//*[contains(text(), 'Checkbox Demo')]").click()


	driver.find_element_by_id("isAgeSelected").click()

	text2 = driver.find_element_by_id("txtAge")
	if text2.text == 'Success - Check box is checked':
		result = result + 'Check Demo test case is : PASSED! \n'
		print('Check Demo test case is : PASSED!')
	else:
		result = result + 'Check Demo test case is: FAILED! \n'
		print('Check Demo test case is : FAILED!')

	driver.quit()

	return result

def formSubmitTest(target_browser):

	# Set the targeted URL
	driver = browserInit(target_browser)

	result = ""

	button = driver.find_elements_by_xpath("//*[contains(text(), 'Input Forms')]")[0].click()

	button2 = driver.find_element_by_xpath("//*[contains(text(), 'Ajax Form Submit')]").click()

	field1 = driver.find_element_by_id("title")

	field2 = driver.find_element_by_id("description")

	button5 = driver.find_element_by_id("btn-submit")
	button5.click()

	if button5.is_displayed() and field1.get_attribute('value') == '' and field2.get_attribute('value') == '':
		result = result + 'First part of the Form Submit test case is: PASSED! \n'
		print('First part of the Form Submit test case is: PASSED!')
	else: 
		result = result + 'First part of the Form Submit test case is: FAILED! \n'
		print('First part of the Form Submit test case is: FAILED!')

	field1.send_keys("Test1")
	field2.send_keys("Test2")
	button5.click()

	appr2 = driver.find_element_by_id("submit-control")
	time.sleep(2)
	if appr2.text == 'Form submited Successfully!':
		result = result + 'Second part of the Form Submit test case is: PASSED! \n'
		print('Second part of the Form Submit test case is: PASSED!')
	else:
		result = result + 'Second part of the Form Submit test case is: FAILED! \n'
		print('Second part of the Form Submit test case is: FAILED')

	driver.quit()

	return result


def sendMail(results):

	fromx = '<from_mail>'
	to  = '<to_mail>'
	msg = MIMEText('Hi,\n\nPlease find below the test results.\n\nThanks,\nPeter\n\n' + results)
	msg['Subject'] = 'Test Results - ' + datetime.today().strftime('%Y-%m-%d')
	msg['From'] = fromx
	msg['To'] = to

	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.ehlo()
		server.login('<login_mail>', '<login_password>')
		server.sendmail(fromx, to, msg.as_string())
		server.quit()
		return('Email is sent!')

	except:
		return('Email is not sent!')

def createResultTxt(results):

	try:
		f = open("Results_" + datetime.today().strftime('%Y-%m-%d') + ".txt", "w")
		f.write(results)
		f.close()
		return('File is created')

	except:
		return('File is not created')




testRunner(input_browser)



