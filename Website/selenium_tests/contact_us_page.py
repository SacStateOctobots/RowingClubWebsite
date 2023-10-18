# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime 
from test_harness import run_tests, PATH_STRING

def contact_us_form_test(driver): 

	print("Inputting data to form.")
 
	# get name form element from the webpage and input a name
	element = driver.find_element(By.ID, "name")
	element.send_keys("Selenium Test Script Name")

	# get email form element from the webpage and input an email
	element = driver.find_element(By.ID, "email")
	element.send_keys("selenium-test@email.com")

	# get phone form element from the webpage and input an email
	element = driver.find_element(By.ID, "phone")
	element.send_keys("123-666-1337")

	# get subject form element from the webpage and input an email
	element = driver.find_element(By.ID, "subject")
	element.send_keys("Selenium Test Script Subject")

	# get message form element from the webpage and input an email
	element = driver.find_element(By.ID, "message")
	element.send_keys("Selenium test script message.\nTest script ran on: "+str(datetime.datetime.now()))

	# get submit button element and submit the email
	print("Submitting form.")
	element = driver.find_element(By.ID, "submit")
	element.submit() # for some reason click() fails but submit() works

	print("Email test complete. Verify email is received in inbox.")
	input("Verify contact us form works as expected. Press enter to continue")

# welcome page has no custom testing functionality so we just pass it an empty function
def main():
	run_tests(contact_us_form_test,PATH_STRING+"/contact")

if __name__ == "__main__":
	main()
