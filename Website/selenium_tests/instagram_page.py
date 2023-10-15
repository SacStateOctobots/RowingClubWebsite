# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime 
from test_harness import run_tests, PATH_STRING

def instagram_test(driver):
	print("NOTE: Instagram element is a custom embed, thus is not easily testable using this method.")
	print("NOTE: Calendar functionality is provided as-is by instagram.")

# welcome page has no custom testing functionality so we just pass it an empty function
def main():
	run_tests(instagram_test, PATH_STRING+"/instagram")

if __name__ == "__main__":
	main()
