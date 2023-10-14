from selenium import webdriver
from selenium.webdriver.common.by import By
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

    # Wait for login to complete
    driver.implicitly_wait(5)

    # Check if login is successful
    success_message = driver.page_source
    if "Login successful" in success_message:
        print("Login successful.")
    else:
        print("Login failed.")

    # Logout
    driver.get(PATH_STRING + "/logout")

    # Wait for logout to complete
    driver.implicitly_wait(5)

    # Check if logout is successful
    success_message = driver.page_source
    if "Logout successful" in success_message:
        print("Logout successful.")
    else:
        print("Logout failed.")

    # Attempting to access protected content after logout
    driver.get(PATH_STRING + "/protected")

    # Wait for the protected content page to load
    driver.implicitly_wait(5)

    # Check if access fails
    error_message = driver.page_source
    if "This is protected content" not in error_message:
        print("Access to protected content failed.")
    else:
        print("Access to protected content succeeded.")

    print("Login test complete.")

def main():
    run_tests(login_form_test, PATH_STRING + "/login")

if __name__ == "__main__":
    main()
