from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_harness import run_tests, PATH_STRING

#todo:
# wrong otp after accessing
# wrong emails
def login_form_test(driver):
	print("Testing login form.")

	# Load the login page
	driver.get(PATH_STRING + "/login_otp")

	print("Testing invalid email.")    
	# Enter wrong login credentials
	element = driver.find_element(By.ID, 'email_otp')
	element.send_keys("wrong@guy.com")	
	element = driver.find_element(By.NAME, "submit")
	input("Verify incorrect email input to page. Press enter to continue.")
	element.submit()
	input("Verify email entry failed. Press enter to continue.")

	# Enter valid login credentials
	print("Testing valid email invalid passcode.")    
	element = driver.find_element(By.ID, 'email_otp')
	in_email = input("Please enter a valid email: ")
	element.send_keys(in_email)
	input("Entering your email to the webpage. Press enter to continue.")  
	element = driver.find_element(By.NAME, "submit")
	element.submit()    
	input("Entering wrong OTP key. Press enter to continue.")  
	element = driver.find_element(By.ID, 'otp-id')
	element.send_keys("wrongkey")
	element = driver.find_element(By.NAME, "submit")
	element.submit()      
	input("Verify email passcode entry failed. Press enter to continue.")
	# Attempting to access protected content
	# driver.get(PATH_STRING + "/protected")

 
	# Enter valid login credentials
	print("Testing correct login.")
	element = driver.find_element(By.ID, 'email_otp')
	in_email = input("Please enter a valid email: ")
	element.send_keys(in_email)
	input("Entering email to web page. Press enter to continue.")  
	element = driver.find_element(By.NAME, "submit")
	element.submit()    
	print("Testing correct email and OTP key. ")  
	in_email = input("Please re-enter the corresponding email: ")
	element = driver.find_element(By.ID, 'email-id')
	element.send_keys(in_email)
	in_code = input("Please enter the passcode received by the email input above: ")
	element = driver.find_element(By.ID, 'otp-id')
	element.send_keys(in_code)
	element = driver.find_element(By.NAME, "submit")
	element.submit()      
	input("Verify protected page loads. Press enter to continue.")  

	# Attempting to access protected content
	# Wait for the protected content page to load
	#try:
		#WebDriverWait(driver, 5).until( EC.presence_of_element_located((By.ID, "admin-variable")))
		#print("Access to protected content succeeded.")
	#except Exception:
		#print("Access to protected content failed.")

	# logout
	print("Testing logout.")
	driver.get(PATH_STRING +"/logout")
	print("Logout succeeded")

def main():
    run_tests(login_form_test, PATH_STRING)

if __name__ == "__main__":
    main()
