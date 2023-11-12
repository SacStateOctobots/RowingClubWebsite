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
    
    input("Entering invalid email. Press enter to continue.")    
	# Enter wrong login credentials
    element = driver.find_element(By.ID, 'email_otp')
    element.send_keys("wrong@guy.com")	
    element = driver.find_element(By.NAME, "submit")
    element.submit()
    
    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
        )
        print("Access to OTP successful.")
    except Exception:
        print("Access to OTP failed.")
        
    # Enter valid login credentials
    input("Testing login form. Press enter to continue.")
    element = driver.find_element(By.ID, 'email_otp')
    element.send_keys("tbcclv@gmail.com")
    element = driver.find_element(By.NAME, "submit")
    element.submit()    
    # Wait for login to complete (wait for the logout link to appear)
    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "email_otp"))
        )
        print("Access to OTP successful.")
    except Exception:
        print("Access to OTP failed.")

    input("Entering wrong OTP key. Press enter to continue.")  
    element = driver.find_element(By.ID, 'otp-id')
    element.send_keys("wrongkey")
    element = driver.find_element(By.NAME, "submit")
    element.submit()      
    print("Access to admin failed.")
    input("Verify OTP entry works as expected. Log in with OTP and press enter to continue.")
    # Attempting to access protected content
    # driver.get(PATH_STRING + "/protected")

    # Wait for the protected content page to load
    try:
        WebDriverWait(driver, 5).until(
            #for the admin-variable is added in the admin.html
            EC.presence_of_element_located((By.ID, "admin-variable"))
        )
        print("Access to protected content succeeded.")
    except Exception:
        print("Access to protected content failed.")
    # logout
    print("Testing logout.")
    driver.get(PATH_STRING +"/logout")
    input("Step through")    
    print("Logout succeeded")

def main():
    run_tests(login_form_test, PATH_STRING)

if __name__ == "__main__":
    main()