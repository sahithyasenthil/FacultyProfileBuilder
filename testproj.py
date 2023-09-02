from selenium import webdriver
#import os
import time
browser = webdriver.Chrome('C:\\Users\\intel\\Desktop\\python_proj\\chromedriver')
browser.get('http://59a52cbf.ngrok.io/')
time.sleep(2)
z='//*[@id="nav"]/a[2]'
browser.find_element_by_xpath(z).click()


time.sleep(2)
z1='//*[@id="nav"]/a[1]'
browser.find_element_by_xpath(z1).click()

ele1=browser.find_element_by_name("username")
ele1.send_keys('Jyotsna')
browser.find_element_by_name("password").send_keys('jyo')
browser.find_element_by_name("cpassword").send_keys('jyo')
browser.find_element_by_name("profname").send_keys('Jyotsna B')
browser.find_element_by_name("about").send_keys('Student')
browser.find_element_by_name("qualification").send_keys('UG')
browser.find_element_by_name("dob").send_keys('28-09-1999')
browser.find_element_by_name("phone").send_keys('9535442515')
browser.find_element_by_name("email").send_keys('rithu.baskar@gmail.com')
browser.find_element_by_name("uniname").send_keys('Amrita Vishwa Vidyapeetam')
browser.find_element_by_name("gdate").send_keys('2017')
browser.find_element_by_name("schname").send_keys('Sri Kumarans')
browser.find_element_by_name("gsdate").send_keys('2013')
browser.find_element_by_name("course").send_keys('Btech ')
browser.find_element_by_name("place1").send_keys('ANCIT Consultations')
browser.find_element_by_name("design").send_keys('Testing engineer')
browser.find_element_by_name("duration").send_keys('feb 2017 - feb 2018')
browser.find_element_by_name("descr").send_keys('Testing automated products ')
browser.find_element_by_name("place2").send_keys('Wipro')
browser.find_element_by_name("design1").send_keys('Software developer')
browser.find_element_by_name("duration1").send_keys('march 2018 - jan 2020')
browser.find_element_by_name("descri").send_keys('Front end and back end developer')
browser.find_element_by_name("skill1").send_keys('Python')
browser.find_element_by_name("skill2").send_keys('Machine Learning')
browser.find_element_by_name("skill3").send_keys('Android app development')
browser.find_element_by_name("skill4").send_keys('Web page designing')
browser.find_element_by_name("skill5").send_keys('Testing')
browser.find_element_by_name("aeo1").send_keys('Coding')
browser.find_element_by_name("aeo2").send_keys('Machine learning')
browser.find_element_by_name("aeo3").send_keys('App development')
x='//*[@id="x"]'

ele1=browser.find_element_by_xpath(x)
ele1.click()

#ele2=browser.find_element_by_xpath("//a[contains(@href,'slogin')]")
#ele2.click()
browser.find_element_by_name("username").send_keys('jyo')
browser.find_element_by_name("password").send_keys('jyo')
y='//*[@id="nav"]/center/form/input'
ele2=browser.find_element_by_xpath(y)
ele2.click()



#browser.find_element_by_name("username").send_keys('CSE1234')
#browser.find_element_by_name("password").send_keys('321')
#time.sleep(2)
#ele2=browser.find_element_by_class_name('login100-form-title')
#ele2.click()
#browser.quit()







