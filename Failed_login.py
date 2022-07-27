import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
   
    def test_a_failed_login_with_empity_email_and_password(self): 

        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_message_email = browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[2]/div").text
        response_message_password = browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[3]/div").text

        #self.assertIn('tidak valid', response_data)
        self.assertEqual(response_message_email, 'diperlukan email')
        self.assertEqual(response_message_password, 'diperlukan kata sandi')

    def test_b_failed_login_with_empity_password(self): 

        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("rizkiiamallia20@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_message_password = browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[3]/div").text

        #self.assertIn('tidak valid', response_data)
        self.assertEqual(response_message_password, 'diperlukan kata sandi')

    def test_c_failed_login_with_empity_email(self): 

        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys("123456") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_message_email = browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[2]/div").text

        #self.assertIn('tidak valid', response_data)
        self.assertEqual(response_message_email, 'diperlukan email')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()