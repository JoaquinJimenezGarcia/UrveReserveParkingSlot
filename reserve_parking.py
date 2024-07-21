from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)
browser.get("<URL>")

try:
    # In some cases, it can ask for the server
    print("Registering server.")
    server_input = browser.find_element(By.ID, "serverurl")
    server_input.send_keys("<URL>")

    link = browser.find_element(By.LINK_TEXT, "Kontynuuj")
    link.click()
except:
    print("Server is already registered.")

print("Authenticating...")
user_input = browser.find_element(By.ID, "username")
password_input = browser.find_element(By.ID, "password")

user_input.send_keys("<USER>")
password_input.send_keys("<PASS>")
password_input.send_keys(Keys.RETURN)

print("Authenticated successfully.")
car_parking_link = browser.find_element(By.ID, "park")
car_parking_link.click()

available_spots = browser.find_elements(By.CLASS_NAME, "status-available")
available_spots[0].click()

button_booking_parking = browser.find_element(By.ID, "bookBtn")
button_booking_parking.click()
button_booking_parking.click() # Duplicated because the button for confirmation has the same ID than button for booking

print("Booking done successfully. Please check the APP to see your spot.")
time.sleep(2)
browser.quit()