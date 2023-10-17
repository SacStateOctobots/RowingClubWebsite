# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime 
from test_harness import run_tests, PATH_STRING

def calendar_test(driver):
	print("NOTE: Calendar element is a custom google embed, thus is not easily testable using this method.")
	print("NOTE: Calendar functionality is provided as-is by Google.")

# welcome page has no custom testing functionality so we just pass it an empty function
def main():
	run_tests(calendar_test, PATH_STRING+"/calendar")

if __name__ == "__main__":
	main()
