import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
   
    def test_a_succses_register(self): 

        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div[2]/button").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("Itzy") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("admin123@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[3]").send_keys("itzy123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[4]").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        #response_data = browser.find_element(By.ID,"swal2-title").text
        response_message_a = browser.find_element(By.ID,"swal2-title").text
        response_message_b = browser.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_message_a, 'Berhasil')
        self.assertEqual(response_message_b, 'created User')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()