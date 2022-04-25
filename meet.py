from config import Gmail, Pass ,sound_not_found,sound_play
from requests.api import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import time


from playsound import playsound
import speech_recognition as sr


r = sr.Recognizer()#using speech reconization module
# PATH='D:\\python'
opt = Options()
opt.add_argument("--disable-infobars")

opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 2,  # mic-->off
    "profile.default_content_setting_values.media_stream_camera": 2,  # camera--> off
    "profile.default_content_setting_values.geolocation": 2,  # location--> off
    "profile.default_content_setting_values.notifications": 2  # notifications--> off
})
driver = webdriver.Chrome(options=opt)
driver.get('https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

driver.maximize_window()
# Logs in the classroom
username = driver.find_element_by_xpath('//*[@id="identifierId"]')
username.click()
username.send_keys(Gmail)

next = driver.find_element_by_xpath(
    '//*[@id="identifierNext"]/div/button/span')
next.click()
time.sleep(4)


# looks for the password area and clicks enter
password = driver.find_element_by_xpath(
    '//*[@id="password"]/div[1]/div/div[1]/input')
password.click()
password.send_keys(Pass)
time.sleep(3)
confirm = driver.find_element_by_xpath(
    '//*[@id="passwordNext"]/div/button/span')
confirm.click()
time.sleep(20)


# Finds the classroom
classroom = driver.find_element_by_xpath(
    '/html/body/div[2]/div[1]/div[6]/div/ol/li[5]/div[1]/div[3]/h2/a[1]/div[1]')
classroom.click()
time.sleep(8)

# looks for the link
link = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[2]/aside/div/div[1]/div/div[2]/div/a')
link.click()
time.sleep(5)


# Switches the tab
driver.switch_to.window(driver.window_handles[1])
current_tab = driver.window_handles[1]
driver.switch_to.window(current_tab)

# dismiss tab
dismiss=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
dismiss.click()
time.sleep(10)

# join now button
joinnow=driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
joinnow.click()
time.sleep(5)


# records all the words and stors as a list and then matches with the words required for attention
time.sleep(5)
c=0
while(True):
    with sr.Microphone() as source:
        if(c!=0):
            break
        print("speak anything")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text=text.split()
            # print('you said : {}'.format(text))

            for t in text:
                print(t)
                if(t == 'Devansh' or t == 'Aryan' or t == 'roll' or t == '41'  or t=='attendance'):
                    c+=1
                    playsound(sound_play)
                        

        except:
            print("Audio not recognized")
            playsound(sound_not_found)
            break


time.sleep(5)

driver.quit()
