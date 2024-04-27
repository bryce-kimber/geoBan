# geoBan
 Identify/verify the IP ranges of countries to help with geoblocking

geoBan is a Python program designed to scrape data from IP2Location for the purpose of identifying and verifying IP ranges of specific countries. This tool is intended to assist in blocking traffic originating from certain countries by providing accurate IP range data.

Installation
To use geoBan, follow these steps:

Clone the Repository:

git clone https://github.com/yourusername/geoBan.git

Install Dependencies:

Ensure you have Python installed (version 3.7 or higher recommended) along with the required libraries. You can install the dependencies using pip:

pip install -r requirements.txt

Usage

Run the Program:
Use the following command to execute the main script:
python geoBan.py

Components
scraper.py: Contains the web scraping functionality using Selenium and Beautiful Soup to retrieve IP range data from IP2Location.
ranges.py: Implements methods to process and verify IP ranges.
duplicates.py: Provides functions to match scraped IP ranges to your block list.
cleanup.py: Removes tmp files.
ban.py: Identifies the largest possible IP ranges given the start and end IP addresses from the scraped data.

Libraries Used
pandas: For data manipulation and handling.
selenium: For web scraping.
BeautifulSoup: For parsing HTML content.
ipaddress: For handling IP addresses and networks.

Contributing
Contributions to geoBan are welcome! If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.

Disclaimer
Please use geoBan responsibly and in compliance with applicable laws and regulations. Blocking traffic based on geographical location may have legal implications, and it is the user's responsibility to ensure compliance with local laws.


