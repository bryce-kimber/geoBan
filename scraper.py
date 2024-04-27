import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup


def scrape(name, url):
    # Set up the webdriver options
    options = Options()
    options.headless = True

    # Set up the webdriver with the options
    driver = webdriver.Firefox(options=options)

    # Navigate to the page
    url = f"{url}"
    print("Scraping " + f"{url} to get ranges")
    driver.get(url)

    # Get the page source
    html = driver.page_source

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(html, "html.parser")

    # Find the table in the HTML
    table = soup.find_all('table')[0]

    # Prepare a list to store the table data
    data = []

    # Find all table rows
    table_rows = table.find_all('tr')

    # Loop through each table row
    for tr in table_rows:
        # Find all columns in each row
        td = tr.find_all('td')
        # Extract the text from the columns and add to the data list
        row = [i.text for i in td]
        data.append(row)

    # Convert the list into a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    country_file = f"{name}_IP2Location.csv"
    df.to_csv(f"{country_file}", index=False)

    # Close the browser
    driver.quit()

    return country_file
