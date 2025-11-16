from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver (make sure you have ChromeDriver installed)
driver = webdriver.Chrome()

# Open the F1 Drivers page
driver.get('https://www.formula1.com/en/drivers')

# Wait for the page to load completely (adjust the time as needed)
time.sleep(5)  # Wait for 5 seconds for the content to fully load

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all <img> tags that contain the word 'driver' in their src attribute (which will include driver images)
driver_images = soup.find_all('img', src=lambda x: x and 'driver' in x)

# Extract 'src' URLs for driver images
driver_image_urls = [img['src'] for img in driver_images if 'src' in img.attrs]

# Print the list of driver image URLs
for img_url in driver_image_urls:
    print(img_url)

# Close the browser
driver.quit()
