from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
input("If you have done scanning QR code Press Enter:  ")
ans = 'y'
def search_user() :
    find_user = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    find_user.send_keys(name)
def user_click() :
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
def send_button() :
    send_bttn = driver.find_element_by_xpath('//span[@data-icon="send"]')
    send_bttn.click()  
def attach_button() :
    attach_box = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div')
    attach_box.click()
def cancel_all() :
    cancelall = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/button')
    cancelall.click()
while(ans == 'y' or ans == 'Y') :
    print("Press 0: To Create a Whatsapp Group\nPress 1: To Send Message\nPress 2: To Send Image/Video\nPress 3: To send a document.\n")
    option = input()
    if(option == '0') :
        grp_name = input("Enter group name: ")
        temp = input("Enter the contacts name with comma seperated\n")
        names = temp.split(',')
        threedots = driver.find_element_by_xpath('//span[@data-testid="menu"]')
        threedots.click()
        newgrp = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div')
        newgrp.click()
        for name in names :
            find_user = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input')
            find_user.send_keys(name+'\n')
        creatgrp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/span')
        creatgrp.click()
        group_name = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]')
        group_name.send_keys(grp_name)    
        final_click = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div')
        final_click.click()
    if(option == '1') :
        msg = input("Enter Your Message:\n")
    elif(option == '2' or option == '3') :
        filepath = input("Enter file path :") 
    if(option == '1' or option == '2' or option == '3') :
        t1 = input("Enter group or participant names(comma delimated):")
        fnames = t1.split(',')
        length = len(fnames)
        names = [fnames[i] +'\n' for i in range(length)]
    if(option == '1') :
        for name in names :
            search_user()
            try:
                msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')        
                msg_box.send_keys(msg)
            except:
                print("Contact Not Found- {}".format(name))
                cancel_all()
                continue
            sleep(1)
            sendbttn = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')        
            sendbttn.click()
            sleep(1.5)
    if(option == '2') :
        for name in names :
            search_user()
            try:
                attach_button()
            except:
                print("Contact Not Found- {}".format(name))
                cancel_all()
                continue
            img_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            img_box.send_keys(filepath)
            while(True) :
                try :
                    send_button()
                    break
                except:
                    continue
    if(option == '3') :
        for name in names :
            search_user()
            try:
                attach_button()
            except:
                print("Contact Not Found - {}".format(name))
                cancel_all()
                continue
            doc_box = driver.find_element_by_xpath('//input[@accept="*"]')
            doc_box.send_keys(filepath)
            while(True) :
                try :
                    send_button()
                    break
                except :
                    continue    
    ans = input("Want to do anything else? Press y(Yes)/n(No) ")
driver.quit()