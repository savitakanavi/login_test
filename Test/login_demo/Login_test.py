from selenium import webdriver
import unittest

class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def Test_1(self):
        self.driver.get("https://qa.connect.calamp.com/connect/")
        self.driver.find_element_by_id("login_username").send_keys("savita44")
        self.driver.find_element_by_id("login_password").send_keys("Pass124!")
        self.driver.find_element_by_id("login").click()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        cls.driver.find_element_by_id("logout").click()

if __name__ == '__main__':
    unittest.main()
