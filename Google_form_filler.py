# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# open Chrome
driver = webdriver.Chrome('C:\EXTRAS\Python-Developer-Course-Codes\Auto Gform\chromedriver.exe')

# Open URL
driver.get('https://forms.gle/eoF2dYjpeyEXZbpu5')
current_url = driver.current_url

# wait for one second, until page gets fully loaded
time.sleep(1)

# Data
datas = [
    ['68' ,'Thorat Jay']
]
i =0
body_text = driver.find_element_by_tag_name("body").get_attribute("innerText")
for i in range(100) :
    #Will run this If form is closed
    if "/closedform" in current_url:
        print("form is closed right now")

        time.sleep(10)
        driver.get('https://forms.gle/eoF2dYjpeyEXZbpu5')
        time.sleep(1.5)
        current_url = driver.current_url
        i+=1
    #will execute this block in case of internal error page shows up
    if "internal error" in body_text:
        print("Internal Error occured refreshing in 3 sec")

        time.sleep(3)
        driver.get('https://forms.gle/eoF2dYjpeyEXZbpu5')
        time.sleep(1.5)
        current_url = driver.current_url
        i+=1
    if "/viewform" in current_url :
        print("Form is open now...")
        # Iterate through each data
        for data in datas:
            # Initialize count is zero
            count = 0

            # contain input boxes
            textboxes = driver.find_elements_by_class_name(
                "quantumWizTextinputPaperinputInput")

            # contain textareas
            textareaboxes = driver.find_elements_by_class_name(
                "quantumWizTextinputPapertextareaInput")
            #contain Radio Button
            target = driver.find_element_by_id("i11")
            target.click();

            # Iterate through all input boxes
            for value in textboxes:
                # enter value
                value.send_keys(data[count])
                # increment count value
                count += 1

            # Iterate through all textareas
            for value in textareaboxes:
                # enter vlaue
                value.send_keys(data[count])
                # increment count value
                count += 1


            # click on submit button
            submit = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
            submit.click()
            print("Response Submitted")
            exit()

            # close the window
driver.quit()