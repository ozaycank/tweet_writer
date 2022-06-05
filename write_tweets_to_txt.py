from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import time

browser = webdriver.Firefox()

browser.get("https://twitter.com/")

time.sleep(5)

log_in = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")

log_in.click()

time.sleep(5)

username = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")

Next = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span")
username.send_keys("#YOUR_USERNAME")

time.sleep(5)

Next.click()

time.sleep(5)

password = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
logging = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")


time.sleep(5)

password.send_keys("#YOUR_PASSWORD")

time.sleep(5)

logging.click()

time.sleep(5)

search_area = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")

search_area.send_keys("#galatasaray")

time.sleep(5)

search_area.send_keys(Keys.ENTER)


time.sleep(5)

#search_button = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[1]/button")

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True



time.sleep(5)
all_tweets = []
tweets =  browser.find_elements_by_css_selector("span[class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']")

for tweet in tweets:
    all_tweets.append(tweet.text)

tweetCount = 1

with open("tweets.txt","w",encoding= "UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("====================================================\n")
        tweetCount +=1

time.sleep(5)

browser.close()