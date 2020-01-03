#coding=utf-8

from selenium import webdriver
from LabSecurityExam import password

driver = webdriver.Chrome()
driver.get('http://authserver.hbnu.edu.cn/authserver/login?service=http://dxyq.hbnu.edu.cn/caslogin.aspx')
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="username"]').send_keys(password.USER)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password.PW)
picture = driver.find_element_by_xpath('//*[@id="captchaImg"]')
picture.screenshot('pic.png')
code = input('输入验证码：')
driver.find_element_by_xpath('//*[@id="captchaResponse"]').send_keys(code)
driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[4]/button').click()
#driver.get('http://dxyq.hbnu.edu.cn/aqzr/model/TwoGradePage/selfStudy.html?ID=12')
#driver.find_element_by_xpath('//*[@id="tb_Secu"]/tbody/tr[1]/td[3]/span/a').click()
driver.get('http://dxyq.hbnu.edu.cn/aqzr/model/TwoGradePage/Practice.aspx?PaperSetID=24&SecurityKindID=0,2,3,4,10')
driver.implicitly_wait(10)
i=1
for i in range(50):
    driver.find_element_by_xpath('//*[@id="DataGridA_ctl02_RBLCData_0"]').click()
    driver.find_element_by_xpath('//*[@id="DataGridA_ctl03_RBLAData_0"]').click()
    driver.find_element_by_xpath('//*[@id="DataGridA_ctl04_RBLAData_1"]').click()

    driver.find_element_by_xpath('//*[@id="DataGridA_ctl05_RBLBData_0"]').click()
    driver.find_element_by_xpath('//*[@id="DataGridA_ctl05_RBLBData_1"]').click()
    driver.find_element_by_xpath('//*[@id="DataGridA_ctl05_RBLBData_2"]').click()
    driver.find_element_by_xpath('//*[@id="DataGridA_ctl05_RBLBData_3"]').click()

    driver.find_element_by_xpath('//*[@id="DataGridA_ctl06_RBLBData_0"]').click()
    driver.find_element_by_xpath('//*[@id="DataGridA_ctl06_RBLBData_1"]').click()

    driver.find_element_by_xpath('//*[@id="btnOk"]').click()
    print(i)
    driver.refresh()