# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime 
from test_harness import run_tests, PATH_STRING

# about page has no custom testing functionality so we just pass it an empty function
def main():
	run_tests(lambda x: None, PATH_STRING+"/about")

if __name__ == "__main__":
	main()
