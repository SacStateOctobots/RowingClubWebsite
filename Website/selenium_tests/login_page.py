from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_harness import run_tests, PATH_STRING

def login_form_test(driver):
    print("Testing login form.")

    # Load the login page
    driver.get(PATH_STRING + "/login")

    # Enter valid login credentials
    element = driver.find_element(By.ID, "email")
    element.send_keys("foo@bar.tld")
    element = driver.find_element(By.ID, "pw")
    element.send_keys("secret")
    element = driver.find_element(By.NAME, "submit")
    element.submit()

    # Wait for login to complete (wait for the logout link to appear)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
        )
        print("Login successful.")
    except Exception:
        print("Login failed.")

    # Attempting to access protected content
    driver.get(PATH_STRING + "/protected")

    # Wait for the protected content page to load
    try:
        WebDriverWait(driver, 10).until(
            #for the admin-variable is added in the admin.html
            EC.presence_of_element_located((By.ID, "admin-variable"))
        )
        print("Access to protected content succeeded.")
    except Exception:
        print("Access to protected content failed.")
    # logout
    print("Testing logout.")
    driver.get(PATH_STRING +"/logout")
    print("Logout succeeded")




def main():
    run_tests(login_form_test, PATH_STRING)

if __name__ == "__main__":
    main()

=======
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime 
from test_harness import run_tests, PATH_STRING

def login_form_test(driver): 

	print("Testing login form.")
	print("WARNING: This code is intended only to show sample functionality.")
	print("WARNING: As such the plain text email and password here are only temporary credentials for development.")

	print("Testing correct login.")
	element = driver.find_element(By.ID, "email")
	element.send_keys("foo@bar.tld")
	element = driver.find_element(By.ID, "pw")
	element.send_keys("secret")
	element = driver.find_element(By.NAME, "submit")
	element.submit()
	input("Press enter if login worked correctly.")
	# logout
	print("Testing logout.")
	driver.get(PATH_STRING+"/logout")
	input("Press enter if logout worked correctly.")
	# attempting to access protected content after logout
	print("Attempting to access protected content after logout.")
	driver.get(PATH_STRING+"/protected")
	input("Press enter if access fails.")
	# return to the login page
	driver.get(PATH_STRING+"/login")

	# incorrect email, correct password
	print("Testing incorrect login.")
	element = driver.find_element(By.ID, "email")
	element.send_keys("fizz@bang.buzz")
	element = driver.find_element(By.ID, "pw")
	element.send_keys("secret")
	element = driver.find_element(By.NAME, "submit")
	element.submit()
	input("Press enter if login fails.")
	
	# correct email, correct password
	print("Testing incorrect login.")
	element = driver.find_element(By.ID, "email")
	element.send_keys("foo@bar.tld")
	element = driver.find_element(By.ID, "pw")
	element.send_keys("fakesecret")
	element = driver.find_element(By.NAME, "submit")
	element.submit()
	input("Press enter if login fails.")

	# incorrect email, incorrect password
	print("Testing incorrect login.")
	element = driver.find_element(By.ID, "email")
	element.send_keys("boom@bang.ouch")
	element = driver.find_element(By.ID, "pw")
	element.send_keys("fakesecret")
	element = driver.find_element(By.NAME, "submit")
	element.submit()
	input("Press enter if login fails.")

	print("Login test complete.")

def main():
	run_tests(login_form_test,PATH_STRING+"/login")

if __name__ == "__main__":
	main()