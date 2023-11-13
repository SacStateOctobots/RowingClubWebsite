# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_harness import run_tests, PATH_STRING
import datetime 
import requests

def get_github_html(url):
    response = requests.get(url)
    return response.text

def welcome_page_test(driver):
    print("Testing welcome page.")

    # Load the HTML element
    driver.get(PATH_STRING)

    # Test video element
    video = driver.find_element(By.TAG_NAME, "video")
    assert video.is_displayed()
    print("Video element test is working")

    # Test "About Us" section
    about_us = driver.find_element(By.ID, 'homepage_about')
    assert about_us.is_displayed()
    print("About us section test is working") 

    # Test "Interested in joining?" button
    join_button = driver.find_element(By.ID, 'recruitment-button')
    assert join_button.is_displayed()
    print("Interested in joining button test is working")

    # Test "Upcoming Events" section
    upcoming_events = driver.find_element(By.XPATH, "//*[contains(text(), 'Upcoming Events')]")
    assert upcoming_events.is_displayed()
    print("Upcoming Events section test is working")

    # Test event cards
    event_cards = driver.find_elements(By.CLASS_NAME, 'central') #this sucks
    for event_card in event_cards:
        assert event_card.is_displayed()
    print("test event cards")

def main():
    run_tests(welcome_page_test, PATH_STRING)

if __name__ == "__main__":
    main()

# welcome page has no custom testing functionality so we just pass it an empty function
if __name__ == "__main__":
	run_tests(lambda x: None, PATH_STRING)
