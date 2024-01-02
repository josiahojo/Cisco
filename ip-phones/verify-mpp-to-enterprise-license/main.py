from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import os,time,logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


#Function to Webscrape the Cisco MPP Web Server and retrieve the license status
def execute_commands(ip_address):
    
    try:
        URL = f'http://{ip_address}/admin/advanced'


        #Setting the parameters for the Chrome Web Browser
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--disable-gpu')
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--disable-dev-shm-usage')
        chromeOptions.add_argument('--allow-running-insecure-content')
        chromeOptions.add_argument('--ignore-certificate-errors')

        driver = webdriver.Chrome(options=chromeOptions)
        driver.get(URL)
        time.sleep(2)
        driver.find_element(By.ID, 'InfoTabContainer_tablist_Download Status').click()
        time.sleep(1)
        html = driver.page_source
        time.sleep(1)
        driver.close()

        soup = BeautifulSoup(html, 'html.parser')
        mydivs = soup.find_all('td', {"class": "info"})

        #Creates a log file to output the results for each IP Address
        with open("html_export.txt", "a") as file:
            file.write("\n") 
            file.write(f"--------------  NEW SECTION --------------- \n")
            file.write(f"--------------  {ip_address}  --------------- \n")
            #section = mydivs[186:188]
            #file.write(str(section))
            file.write(str(mydivs[186]))
            file.write("\n")
            file.write(str(mydivs[187]))
            file.write("\n")
            #file.write(str(mydivs[188]))
            #file.write("\n")
            file.write("--------------   END    -------------------- \n")
        
    except Exception as e:
        with open("html_export.txt", "a") as file:
            file.write(f"--------------{ip_address}------------")
            file.write(f"Failed to connect or execute command at {ip_address} \n")
            file.write(f"Error: {str(e)} \n")
            file.write("\n")
            file.write("--------------   END    --------------------")
            file.write("\n")     


# Read the list of IP addresses
with open('ip_addresses.txt', 'r') as f:
    ip_addresses = [line.strip() for line in f]

# Perform the operations for each IP address
for ip_address in ip_addresses:
    execute_commands(ip_address)
