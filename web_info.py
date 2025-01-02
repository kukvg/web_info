from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
import pandas as pd
import time

driver_path = "/path_to/chromedriver.exe"
file_path = "/path_to/web_info/domain.csv"
result_path = "/path_to/web_info/result.txt"

service = Service(driver_path)
options = Options()
driver = webdriver.Chrome(service=service, options=options)

#driver.set_window_size(1920, 1080)

page_url = pd.read_csv(file_path)
page_id = 0

for urls in page_url['url']:
    page_id = page_id + 1
    scr_path = f"/path_to/web_info/scr/{page_id}.png"

    urls = "http://" + urls
    try:
        driver.get(urls)
        time.sleep(2)
    except Exception as e:
        print(f"Błąd przy otwieraniu {urls}: {e}")
        continue


    
    driver.save_screenshot(scr_path)
    resp = requests.get(urls)
    
    with open(result_path, mode="a") as file:
        file.write(str(page_id) + urls + "res:" + str(resp.status_code) +"\n")

driver.quit()

#github.com/kukvg