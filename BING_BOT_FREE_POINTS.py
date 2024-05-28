#install selenium with --> open cmd --> type "pip install selenium"
import time
import random
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options

# Set up Edge WebDriver
edge_driver_path = 'C:\\Users\\Yourname\\Desktop\\edge_path_for_selenium\\msedgedriver.exe'  # Correct the path to your Edge WebDriver, this is just where mine is change as required
edge_service = EdgeService(edge_driver_path)
options = Options()
options.use_chromium = True

# Initialize the Edge WebDriver
driver = webdriver.Edge(service=edge_service, options=options)

def perform_search(query):
    """
    Function to perform a search on Bing using the provided query.
    """
    try:
        driver.get('https://www.bing.com')  # Open Bing
        search_box = driver.find_element(By.NAME, 'q')  # Find the search box
        search_box.send_keys(query)  # Enter the search query
        search_box.send_keys(Keys.RETURN)  # Simulate pressing the Enter key
        time.sleep(3)  # Wait for 3 seconds to mimic human behavior
    except Exception as e:
        print(f"An error occurred during search: {e}")

# Perform 30 searches with random numbers
for _ in range(30):
    random_number = random.randint(1000, 9999)  # Generate a random number between 1000 and 9999
    perform_search(str(random_number))  # Convert the number to a string and perform the search

# Close the browser
driver.quit()
