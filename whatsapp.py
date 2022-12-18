#  Hello hi there,this script is used to send the corresponding messages to the mentioned mobile numbers
#  in a google sheet . Don't you know about goggle sheets, well no problem it's a simple spreadsheet or
#  more precisely, I would refer to it as an online excel sheet. In, my script, I have kept mobile numbers
#  in the first column and messages in the corresponding next column,i.e. column 2.
import gspread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
'''
.......Haven't heard about the above libraries? No problem, ok so these libraries will be used to perform our
task where gspread for using the spreadsheet and ya, I am sure you must have heard about selenium which
a lot of uses, here for chromedriver
.......setting the python console (installing required libraries)
In the terminal type below commands and press enter and let them download
pip install gspread
pip install selenium
pip install oauth2client
'''
#Auth
'''
establishing a google spreadsheet for reading data
step1)create a new spreadsheet in your drive and save it.
step2)get the share link that will be give as input below
step3)Underneath Google Apps APIs select Drive API:
      now select the credentials and click the little arrow create credentials button
step4)Now select service account key and;
......Choose App Engine default service account under Service account and JSON as the format:
......Click create, and you should get a .json file download.
......Move this into your project directory and rename it as "google_spread.json".
......Finally, open the file and look for client_email. This should be the name of your project at
gserviceaccount.com.
.....Share your Google Sheet with this email address (Top Right > Share > Enter Email).
     That’s it for the Google Drive side.
Still not able to understand, then you may want to refer to this
'''
#Auth
#copy the path of the .json file you downloaded from drive
path = r'C:\Users\hp\.PyCharmEdu2019.2\config\scratches\creds.json'
gc = gspread.service_account(filename=path)
#Open_using_URL
#copy the url of the spreadsheet that you created online on your drive
url  = 'https://docs.google.com/spreadsheets/d/1W6Xd8dVN-1hHOJJb67S77xRWnUjCO0xzl9qEC2AmlkA/edit#gid=0' #Enter URL
sht1 = gc.open_by_url(url)
workbook = sht1.sheet1
no_of_msg = len(workbook.get_all_values())
'''
Downloading the chromedriver executable
this will help you in loading the whatsapp web at chrome through the script
step1)download a chromedriver from https://chromedriver.chromium.org/downloads
step2)that will be a zip folder so extract it in your drive
step3)then copy the path of your driver below in executable path
'''
# copy and paste the path of your chromedriver executable_path, mine is on desktop
driver = webdriver.Chrome(executable_path=r'C:\Users\hp\Desktop\chromedriver.exe')
driver.get('https://web.whatsapp.com/')# access whatsapp web using driver
time.sleep(15)#these sleep functions are of no use but just to make sure that the script works even
              #under weak internet connectivity
print('Logged In !!!!!')
for i in range(1,no_of_msg+1):
    Phone_list = workbook.row_values(i)
    ele = driver.find_element_by_tag_name('body')
    ele.send_keys(Keys.COMMAND + 't')
    ele.send_keys(Keys.COMMAND + '1')
    ele.send_keys(Keys.COMMAND + 'w')
    driver.get(f'https://api.whatsapp.com/send?phone=91{int(Phone_list[0])}')
    ele1 = driver.find_element_by_link_text('CONTINUE TO CHAT')
    ele1.click()
    time.sleep(10)
    ele2 = driver.find_element_by_link_text('use WhatsApp Web')
    ele2.click()
    time.sleep(15)
    ele3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
    # nothing fancy in above line, In Whatsapp web, just right click at the space where we type a message to
    # send and copy the path the xpath of the element where we write our message
    ele3.click()
    for i in range(int(Phone_list[2])+1):
        ele3.send_keys(Phone_list[1])
        ele3.send_keys(Keys.RETURN)
    print(f'Msg sent to {int(Phone_list[0])}')
    time.sleep(15)
driver.quit()# quit the chromedriver
print('Done !!')
