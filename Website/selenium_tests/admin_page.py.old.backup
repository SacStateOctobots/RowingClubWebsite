# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime 
from test_harness import run_tests, PATH_STRING
import os 
#from selenium.webdriver.support.wait import WebDriverWait

def admin_page_test(driver): 

	print("Testing admin page.")

	print("Testing correct login, please wait.")
	print("Attempting to connect to "+PATH_STRING+"/login")
	driver.get(PATH_STRING+"/login")
	element = driver.find_element(By.ID, "email")
	element.send_keys("foo@bar.tld")
	element = driver.find_element(By.ID, "pw")
	element.send_keys("secret")
	element = driver.find_element(By.NAME, "submit")
	element.submit()
	input("Press enter if login worked correctly.")

	dir_path = os.path.dirname(os.path.realpath(__file__))

	# test player form input
	driver.get(PATH_STRING+"/protected")
	element = driver.find_element(By.ID, "players-tab")
	element.click()
	element = driver.find_element(By.ID, "addname-player")
	element.clear()
	element.send_keys("Test Player "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	element = driver.find_element(By.ID, "desc-player")
	element.clear()
	element.send_keys("Test description "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
	element = driver.find_element(By.ID, "file-player")
	element.clear()
	element.send_keys(dir_path+"/sample-image.jpg")
	#element = driver.find_element(By.ID, "add-form-submit-player")
	element = driver.find_element(By.NAME, "player-button-name")
	input("Press enter if player form input worked correctly")
	#element = driver.find_element(By.ID, "add-form-submit-player")
	element.click()
	input("Press enter if player submission worked correctly.")
	
	# Test alumni form
	driver.get(PATH_STRING+"/protected")
	element = driver.find_element(By.ID, "alumni-tab")
	element.click()
	element = driver.find_element(By.NAME, "alumni-addname")
	element.clear()
	element.send_keys("Test Player "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	element = driver.find_element(By.NAME, "alumni-desc")
	element.clear()
	element.send_keys("Test description "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
	element = driver.find_element(By.NAME, "alumni-file")
	element.clear()
	element.send_keys(dir_path+"/sample-image.jpg")
	element = driver.find_element(By.NAME, "alumni-form-button-name")
	driver.execute_script("document.getElementById(\"alumni-form-button-id\").scrollIntoView();")
	input("Press enter if alumni form input worked correctly")
	#element = driver.find_element(By.NAME, "alumni-add-form")
	element.click()
	input("Press enter if alumni submission worked correctly.")

	# Test team members form
	driver.get(PATH_STRING+"/protected")
	element = driver.find_element(By.ID, "team-tab")
	element.click()
	element = driver.find_element(By.NAME, "team-addname")
	element.clear()
	element.send_keys("Test Player "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	element = driver.find_element(By.NAME, "team-desc")
	element.clear()
	element.send_keys("Test description 1 "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
	element = driver.find_element(By.NAME, "role-desc")
	element.clear()
	element.send_keys("Test description 2 "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
	element = driver.find_element(By.NAME, "team-file")
	# This element fails to scroll into view using only selenium.
	# This is a hack where we run javascript in the browser to scroll the file element into view by id
	driver.execute_script("document.getElementById(\"team-file\").scrollIntoView();")
	element = driver.find_element(By.ID, "team-file")
	input("Wait for viewport update")
	element.clear()
	element.send_keys(dir_path+"/sample-image.jpg")
	element = driver.find_element(By.NAME, "team-button-name")
	input("Press enter if team member form input worked correctly")
	element.click()
	input("Press enter if team member form submission worked correctly.")
	
	# Test officers form
	driver.get(PATH_STRING+"/protected")
	element = driver.find_element(By.ID, "officers-tab")
	element.click()
	element = driver.find_element(By.NAME, "officers-addname")
	element.clear()
	element.send_keys("Test Player "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	element = driver.find_element(By.NAME, "officers-desc")
	element.clear()
	element.send_keys("Test description "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	element = driver.find_element(By.NAME, "officers-file")
	element.clear()
	element.send_keys(dir_path+"/sample-image.jpg")
	input("Press enter if officers form input worked correctly")
	# This element fails to scroll into view using only selenium.
	# This is a hack where we run javascript in the browser to scroll the submit button element into view by id
	# We have to wait a second for the viewport to update for this one to work.
	driver.execute_script("document.getElementById(\"officers-button-id\").scrollIntoView();")
	element = driver.find_element(By.ID, "officers-button-id")
	input("Wait for viewport update.")
	element.click()
	input("Press enter if officers submission worked correctly.")

	# logout
	print("Testing logout.")
	driver.get(PATH_STRING+"/logout")
	input("Press enter if logout worked correctly.")
	

def main():
	run_tests(admin_page_test,PATH_STRING+"/protected")

if __name__ == "__main__":
	main()
