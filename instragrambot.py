import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
import pyautogui
import time

CHROME_DRIVER_PATH = [Path-to-chrome-driver]
INSTAGRAM_USERNAME = [Account]
INST_PASSWORD = [Secret KEY]
INST_SITE = "https://www.instagram.com/"

class InstagramBot:

    def __init__(self,driver_path):
        s = Service(driver_path)
        self.driver = webdriver.Chrome(service=s)



    # Loging Function

    def login(self):
        self.driver.get(INST_SITE)
        time.sleep(7)
        user_input = self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        user_input.send_keys(INSTAGRAM_USERNAME)
        pass_input = self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        pass_input.send_keys(INST_PASSWORD)
        time.sleep(4)
        try:
            cookies_btn = self.driver.find_element(By.XPATH,"/html/body/div[4]/div/div/button[1]")
            cookies_btn.click()
            time.sleep(4)
            login_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
            login_button.click()
            time.sleep(7)
        except:
            login_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
            login_button.click()
            time.sleep(7)
        try:
            self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div/div/button").click()
            time.sleep(12)
            not_now_button = self.driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div/div[3]/button[2]")
            not_now_button.click()
            time.sleep(3)
        except:
            time.sleep(12)
            not_now_button = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]")
            not_now_button.click()
            time.sleep(3)
        pass


    # Follow accounts based on specified instagram account
    def find_followers(self):
        time.sleep(15)
        self.driver.get("https://www.instagram.com/tech_myths/")
        time.sleep(15)
        followers_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span")
        followers_button.click()
        time.sleep(7)
        modal = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[2]')

        for i in range(100):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
        pass


    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,"li button")
        x_ = 1
        for button in all_buttons:
            if x_ % 20 == 0:
                time.sleep(60*5)
                x_ += 1
            else:
                try:
                    button.click()
                    time.sleep(1)
                    x_ += 1
                except:
                    time.sleep(1)
                    cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[7]/div/div/div/div[3]/button[2]')
                    cancel_button.click()
                    x_ += 1
        pass



    # POSTING Function

    def post_daily(self):
        time.sleep(5)
        post_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div")
        post_button.click()
        time.sleep(5)
        selectfile_button = self.driver.find_element(By.XPATH,'/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')
        selectfile_button.click()
        time.sleep(1)  # waiting for window popup to open
        pyautogui.write(r"C:\Users\NickDCorona\PycharmProjects\DailyGraphicCreator\Background photos\WednesdayElon Musk.png")  # path of File
        pyautogui.press('enter')
        time.sleep(7)
        size_btn = self.driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button')
        size_btn.click()
        time.sleep(.5)
        original_btn = self.driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/button[1]')
        original_btn.click()
        time.sleep(.5)
        next_btn = self.driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
        next_btn.click()
        next_btn_2 = self.driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button')
        next_btn_2.click()
        time.sleep(3)
        caption_box = self.driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea')
        time.sleep(.5)
        caption_box.send_keys("hello world.\n\n\n @Gogetsum_tech")
        share_btn = self.driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
        share_btn.click()
        time.sleep(12)
        self.driver.get(INST_SITE)


bot = InstagramBot(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()


