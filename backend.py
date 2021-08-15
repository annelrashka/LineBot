import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

searchable="fc-claim" #this is the result's class, might need revision

# Check Tipe Query
def checkQuery(query):
    query = query.split(" ")
    return query[0]

#Requires Selenium WebDriver 3.13 or newer
def hoax(query):
    if checkQuery(query.lower()) == "fc":
        query = query.split(" ")
        query = query[1:]
        query = " ".join(query)
        with webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options) as driver: #change this line according to your chromedriver location
            wait = WebDriverWait(driver, 10)
            driver.get("https://toolbox.google.com/factcheck/explorer")
            driver.find_element(By.NAME, "query").send_keys(query + Keys.RETURN)
            wait.until(presence_of_element_located((By.XPATH, '//*[@title="Claim text" or text()="Suggestions:"]')))
            claims=driver.find_elements_by_xpath('//*[@title="Claim text"]')
            results=driver.find_elements_by_xpath('//*[@title="Publisher rating"]')
            article=driver.find_elements_by_xpath('//*[@title="View article in a new window"]')
            ret="Query : %s\n" % query
            for i in range(len(claims)): #will be replaced by function return
                ret+=("--------------------------------------------------------------\n")
                ret+=("Claim:\n")
                ret+=(claims[i].text+"\n")
                ret+=("Result:\n")
                ret+=(results[i].text+"\n")
                ret+=("Article:\n")
                ret+=(str(article[i].get_attribute("href"))+"\n")
            if len(claims)==0:
                ret="Query : %s\n" % query
                ret+=("--------------------------------------------------------------\n")
                ret+=("Search error")
    elif checkQuery(query.lower()) == "help":
        ret="Help\n"
        ret+="----------\n"
        ret+="fc <title> = to check the title's validity\n"
        ret+="creator = to show the creators of SELEKTA\n"
        ret+="help = to show this message\n"
        ret+="----------\n"
    elif checkQuery(query.lower()) == "creator":
        ret="Creator (Kelompok 4 - Epimelis)"
        ret+="------------------------------"
        ret+="Gresya Angelina Eunike Leman - 16520082"
        ret+="Frederik Imanuel Louis - 16520103"
        ret+="Andreana Hartadi Suliman - 16520113"
        ret+="Wesly Giovano - 16520363"
        ret+="M Syahrul Surya Putra - 16520430"
        ret+="David Nathanio Gabriel Siahaan - 16520432"
        ret+="Annel Rashka Perdana - 16520448"
        ret+="Afkar Dhiya Ulhaq - 16520452"
        ret+="Rifki Kaida - 16520496"
       
    else:
        ret="Sorry, your format is invalid :(\nUse \"help\" to show list of command"

    return ret