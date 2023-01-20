
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

def browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    try:    
        driver.maximize_window()
        driver.get("https://vk.com")
        time.sleep(1)
        login = driver.find_element_by_xpath("//*[@id='index_email']")

        login.send_keys("Login"+ "\n")
        time.sleep(2)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        password = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/input")
        password.send_keys("Password"+ "\n")
        # m = driver.find_element_by_xpath("//*[text() = 'Продолжить']")
        # m.click()

        time.sleep(2)
        d= driver.find_element_by_xpath("//*[@id='l_fr']/a/span")
        d.click()

        time.sleep(3)
        d= driver.find_element_by_xpath("//*[@id='friends_right_blocks_root']/div/section/div[1]/div/div[3]/a/span[1]") 
        d.click()
        for i in range(3):
            time.sleep(3)
            img = driver.find_elements_by_css_selector("#friends_list > div.friends_find_user > div.friends_find_user_info > a.friends_find_user_add")
            print(len(img))
            time.sleep(1)
            for i in img:
                i.click()
                time.sleep(1)
                print(i)
            driver.refresh()
        # time.sleep(3)
        # img = driver.find_elements_by_css_selector("#friends_list > div.friends_find_user > div.friends_find_user_info > a.friends_find_user_add")
        # print(len(img))
        # time.sleep(1)
        # for i in img:
        #     i.click()
        #     time.sleep(1)
        #     print(i)

        time.sleep(5)
        driver.quit()
    except:
        driver.quit()


browser()
