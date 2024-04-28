# geoBan

**Identify/verify the IP ranges of countries to help with geoblocking**

geoBan is a Python program designed to scrape data from IP2Location for the purpose of identifying and verifying IP ranges of specific countries. This tool is intended to assist in blocking traffic originating from certain countries by providing accurate IP range data.

## Installation

### Clone the Repository:

https://github.com/bryce-kimber/geoBan.git

### Install Dependencies:

Ensure you have Python installed (version 3.7 or higher recommended) along with the required libraries. You can install the dependencies using pip:

pip install -r requirements.txt

## Usage

### Run the Program:

Use the following command to execute the main script:

python geoBan.py

## Components

- **`scraper.py`:** Contains the web scraping functionality using Selenium and Beautiful Soup to retrieve IP range data from IP2Location.
  
- **`ranges.py`:** Implements methods to process and verify IP ranges.
  
- **`duplicates.py`:** Provides functions to match scraped IP ranges to your block list.
  
- **`cleanup.py`:** Removes temporary files.
  
- **`ban.py`:** Identifies the largest possible IP ranges given the start and end IP addresses from the scraped data.

## For servers with CLI only:

I have only tested the CLI functionality on Ubuntu server. If you already have firefox installed via apt, there seems to be an issue in the binary installed when using apt/snap. Follow the following steps to install the firefox binary directly from mozilla. Make sure to get the latest version.

`Uninstall firefox:`

- sudo apt remove firefox

`Install firefox package:`

- wget https://ftp.mozilla.org/pub/firefox/releases/125.0.2/linux-x86_64/en-US/firefox-125.0.2.tar.bz2

- tar -xf firefox-116.0.3.tar.bz2 --directory /opt/

- ln -s /opt/firefox/firefox /usr/bin/firefox

`Install the required libraries for selenium to be able to interact headless with firefox:`

- sudo apt install libgtk-3-0, libasound2t64

- export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/:$LD_LIBRARY_PATH


## Libraries Used

- `pandas`: For data manipulation and handling.
- `selenium`: For web scraping.
- `BeautifulSoup`: For parsing HTML content.
- `ipaddress`: For handling IP addresses and networks.

## Contributing

Contributions to geoBan are welcome! If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.

## Disclaimer

Please use geoBan responsibly and in compliance with applicable laws and regulations. Blocking traffic based on geographical location may have legal implications, and it is the user's responsibility to ensure compliance with local laws.
