from selenium import webdriver
from selenium.webdriver.common.by import By

# Changing this variable ensures all tests will use this url for the given tests
PATH_STRING = "http://localhost:5000"

# our common tests will iterate over this pair of href/attribute pairs
# xpaths: https://en.wikipedia.org/wiki/XPath 
xpath_tests = ['//a','//img','//video','//source']
attributes = ['href','src','src','src']

def run_tests(custom_test,site_url):
	# create webdriver object
	print("Loading webdriver.")
	driver = webdriver.Firefox() # we can generalize this to later drivers later

	# force our test driver to wait 2 seconds on every element location call
	driver.implicitly_wait(3)

	# get the local website 
	print("Attempting to connect to "+site_url)
	driver.get(site_url)

	# run user defined custom test
	print("Running custom tests.")
	custom_test(driver)

	# run the common tests for all webpages
	print("Running common tests.")
	common_test(driver,site_url)


# run all tests from array above
def common_test(driver,site_url):
	for i in range(len(xpath_tests)):
		print("Checking xpath: "+str(xpath_tests[i])+" with attribute: "+str(attributes[i])+".")
		c = input("Enter S to skip this test or C to continue:")
		if c == "S":
			continue
		test_item(driver,site_url,xpath_tests[i],attributes[i])

# run the test_val/attribute test
def test_item(driver,site_url,test_val,attribute):
	# navigate back to site_url
	driver.get(site_url)
	# get all links on page
	links = driver.find_elements(By.XPATH,test_val)
	link_list = [link.get_attribute(attribute) for link in links]
	print("Attempting links:"+str(link_list))
	# we can wrap this in try catch but it probably makes more sense to let things just fail
	for link in link_list:
		if link != '': # don't follow empty links
			c = input("Following link "+str(link)+" press S to skip this test or C to continue:")
			if c == "S":
				continue
			driver.get(link)
			input("Press enter if link navigation worked correctly.")
			driver.get(site_url)