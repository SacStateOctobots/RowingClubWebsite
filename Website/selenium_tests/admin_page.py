# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import datetime 
from test_harness import run_tests, PATH_STRING
import os 

def test_input_helper(driver,tab,field_input_pairs,submit_id):
	# Navigate to admin page
	driver.get(PATH_STRING+"/protected")
	# Navigate to the required tab
	element = driver.find_element(By.ID,tab)
	element.click()
	# fill out the fields of this form based on given list
	for val in field_input_pairs:
		# This is a hack where we run javascript in the browser to scroll the submit button element into view by id
		# We have to wait a second for the viewport to update for this one to work.
		driver.execute_script("document.getElementById(\""+val[0]+"\").scrollIntoView();")
		element = driver.find_element(By.ID,val[0])
		input("Wait for viewport update.")
		element.clear()
		element.send_keys(val[1])
		input("Verify value "+val[1]+" input to form.")

	# force user to confirm field input
	input("Press enter if all form inputs worked correctly")

	# This is a hack where we run javascript in the browser to scroll the submit button element into view by id
	# We have to wait a second for the viewport to update for this one to work.
	driver.execute_script("document.getElementById(\""+submit_id+"\").scrollIntoView();")
	element = driver.find_element(By.ID, submit_id)

	# wait for viewport update, submit, then force user to confirm submission
	input("Wait for viewport update.")
	#element.click()
	element.submit()
	input("Press enter if submission worked correctly.")

def test_delete_helper(driver,tab,field_id,field_input,submit_id):
	# Navigate to admin page
	driver.get(PATH_STRING+"/protected")
	# Navigate to the required tab
	element = driver.find_element(By.ID,tab)
	element.click()

	# fill out the delete field of this form based on given values
	# This is a hack where we run javascript in the browser to scroll the submit button element into view by id
	# We have to wait a second for the viewport to update for this one to work.
	driver.execute_script("document.getElementById(\""+field_id+"\").scrollIntoView();")

	# For raw text fields things work as in the previous helper function
	#element = driver.find_element(By.ID,field_id)
	#input("Wait for viewport update.")
	#element.clear()
	#element.send_keys(field_input)

	# For select elements we can do the following
	element = driver.find_element(By.ID,field_id)
	input("Wait for viewport update.")
	select = Select(element)
	select.select_by_value(field_input)

	# force user to confirm field input
	input("Press enter if all form inputs worked correctly")

	# This is a hack where we run javascript in the browser to scroll the submit button element into view by id
	# We have to wait a second for the viewport to update for this one to work.
	driver.execute_script("document.getElementById(\""+submit_id+"\").scrollIntoView();")
	element = driver.find_element(By.ID, submit_id)

	# wait for viewport update, submit, then force user to confirm submission
	input("Wait for viewport update.")
	#element.click()
	element.submit()
	input("Press enter if submission worked correctly.")

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
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	# test player form input
	form_input_pairs = [
		("player-name-id","Test Player "+now),
		("player-desc-id","Test Player Description "+now),
		("player-file-id",dir_path+"/sample-image.jpg")
	]
	print("Testing player input.")
	test_input_helper(driver,"players-tab",form_input_pairs,"player-button-id")
	print("Testing player delete.")
	test_delete_helper(driver,"players-tab","deleteplayer-id",form_input_pairs[0][1],"delete-player-button-id")
	
	# test alumni form input
	form_input_pairs = [
		("alumni-name-id","Test Alumni "+now),
		("alumni-desc-id","Test Alumni Description "+now),
		("alumni-file-id",dir_path+"/sample-image.jpg")
	]
	print("Testing alumni input.")
	test_input_helper(driver,"alumni-tab",form_input_pairs,"alumni-button-id")
	print("Testing alumni delete.")
	test_delete_helper(driver,"alumni-tab","deletealumni-id",form_input_pairs[0][1],"delete-alumni-button-id")

	# test team member form input
	form_input_pairs = [
		("team-name-id","Test Member "+now),
		("team-player-desc-id","Test Member Player Description "+now),
		("team-role-desc-id","Test Member Role Description "+now),
		("team-file-id",dir_path+"/sample-image.jpg")
	]
	print("Testing team member input.")
	test_input_helper(driver,"team-tab",form_input_pairs,"team-button-id")
	print("Testing team member delete.")
	test_delete_helper(driver,"team-tab","deleteteam-id",form_input_pairs[0][1],"delete-team-button-id")

	# test officer form input
	form_input_pairs = [
		("officers-name-id","Test Officer "+now),
		("officers-desc-id","Test Officer Description "+now),
		("officers-file-id",dir_path+"/sample-image.jpg")
	]
	print("Testing officers input.")
	test_input_helper(driver,"officers-tab",form_input_pairs,"officers-button-id")
	print("Testing officers delete.")
	test_delete_helper(driver,"officers-tab","deleteofficers-id",form_input_pairs[0][1],"delete-officers-button-id")

	# test testimonial form input
	form_input_pairs = [
		("testimonial-name-id","Test Testimonial "+now),
		("testimonial-text1-id","Testimonial Text1 "+now),
		("testimonial-text2-id","Testimonial Text2 "+now),
		("testimonial-file-id",dir_path+"/sample-image.jpg")
	]
	print("Testing testimonial input.")
	test_input_helper(driver,"testimonials-tab",form_input_pairs,"testimonial-button-id")
	print("Testing testimonial delete.")
	test_delete_helper(driver,"testimonials-tab","deletetestimonial-id",form_input_pairs[0][1],"delete-testimonial-button-id")
	
	# logout
	print("Testing logout.")
	driver.get(PATH_STRING+"/logout")
	input("Press enter if logout worked correctly.")
	

def main():
	run_tests(admin_page_test,PATH_STRING+"/protected")

if __name__ == "__main__":
	main()