from bs4 import BeautifulSoup
import requests


# The link to the page that data will be extrapolated from
url = 'https://www.verizonwireless.com/smartphones/'

# Headers to masquerade as a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

# Download page HTML using requests
response = requests.get(url, headers=headers)

# Check valid response received
if response.status_code == 200:

    # Parse HTML using Beautiful Soup
    soup = BeautifulSoup(response.text, 'lxml')

    # Initialize dictionaries to store scraped info
    reg_phones = {}
    smartphones = {}

# print(soup.prettify())

# div = soup.find('div')

# devices = div.id.text
# print(devices)
