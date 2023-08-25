import requests
from bs4 import BeautifulSoup

def get_website_content(url):
    # Send a request to the website
    response = requests.get(url)
    
    # Parse the website content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    return soup.text

website_url = 'https://home.nest.com/thermostat/DEVICE_18B4300000BA8913'
content = get_website_content(website_url)
print(content)
