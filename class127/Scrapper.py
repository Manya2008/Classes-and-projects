from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

start_url= "https://science.nasa.gov/exoplanets/exoplanet-catalog/"
browser = webdriver.Chrome()
browser.get(start_url)
time.sleep(2)
planets_data = []
for i in range(0,10):
    print(f'scrapping page {i+1}')
    soup = bs(browser.page_source,"html.parser")
    time.sleep(2)
    for p in soup.find_all("div",class_ = 'hds-content-item'):
        planet_info = []
        planet_info.append(p.find('h3',class_ = 'heading-22').text.strip())
        info_to_extract = ['Light-Years From Earth','Planet Mass',"Stellar Magnitude","Discovery Date"]
        for info_name in info_to_extract:
            try:
                planet_info.append(p.select_one(f'span:-soup-contains("{info_name}")').find_next_sibling('span').text.strip())
            except:
                planet_info.append('unkown')
        planets_data.append(planet_info)
    try:
        time.sleep(2)
        next_button = WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="primary"]/div/div[3]/div/div/div/div/div/div/div[2]/div[2]/nav/button[8]')))
        browser.execute_script("arguments[0].scrollIntoView()",next_button)
        time.sleep(2)
        next_button.click()
    except:
        print("Error occured while navigating to next page")

#print(planets_data)
headers = ["name","light years from earth","planet mass","stelar magnitude","discovery date"]
planet_df = pd.DataFrame(planets_data,columns = headers)
planet_df.to_csv('planetsdata.csv',index = True,index_label = "id")