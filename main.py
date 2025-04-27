import time

import pandas as pd
from bs4 import BeautifulSoup
from pandas import DataFrame

from selenium_driver.driver import selenium_driver


URL_PATTERN = "https://indy-towers.ru/search?korpus=4&section=1&floor={floor}&flat={flat}"


if __name__ == "__main__":
    df = pd.read_excel("files/file.xlsx")
    new_df = DataFrame()

    for _, row in df.iterrows():
        floor = row[3]
        flat = row[0]
        url = URL_PATTERN.format(floor=floor, flat=flat)

        selenium_driver.get(url)
        time.sleep(2)
        html = selenium_driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        p_values = soup.find_all('p', class_='value')

        old_price = p_values[0].text
        new_price = p_values[1].text

        new_row = pd.Series([floor, flat, old_price, new_price], index=['floor', 'flat', 'old_price', 'new_price'])
        new_df = pd.concat([new_df, pd.DataFrame([new_row])], ignore_index=True)


    new_df.to_excel("files/result.xlsx")
    selenium_driver.quit()
