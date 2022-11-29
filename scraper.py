from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

stars_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping '+START_URL+'...' )
        
        # BeautifulSoup Object     
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # Loop to find element using XPATH
        tbody_tags = soup.find_all("tbody")
        for tbody_tag in tbody_tags:

            td_tags = tbody_tag.find_all("tr")
            # print(td_tags)
           
            temp_list = []

            for index, td_tag in enumerate(td_tags):

                if index == 0:                   
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")

            stars_data.append(temp_list)

        # Find all elements on the page and click to move to the next page
        # browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

# Calling Method    
scrape()

# Define Header
headers = ["Proper name", "Distance", "Mass", "Radius"]

# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(stars_data, columns=headers)

# Convert to CSV
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
