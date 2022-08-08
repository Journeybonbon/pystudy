import pymysql
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import timedelta, date

dt = date(2022, 1, 3)
insert_data = {'dt': '20230103', 'res': '', 'tt' : '', 'menu' : ''}
sql_query = "INSERT INTO 'TABLE' (COLUMS) VALUES (%s, %s, %s, %s)"

#초기화 설정
def initProgram():
    db = connectDB()
    cursor = db.cursor()
    driver = getDriver()
    return db, cursor, driver

#식단 페이지 이동
def getDriver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    day_result = dt.strftime("%Y-%m-%d")
    driver.get("https://dorm.kumoh.ac.kr/dorm/restaurant_menu01.do?mode=menuList&srDt=" + day_result)
    return driver

#DB 연결
def connectDB():
    db = pymysql.connect(host='', 
                    port=, 
					user='', 
					passwd='', 
					db='',
					charset='utf8')    
    return db

#sql 쿼리문 실행 후 DB에 저장
def saveData(cursor, db):
    cursor.execute(sql_query, list(insert_data.values()))
    db.commit()

#식당, 메뉴 설정
def setData(element_menu, cursor, db):
    for menu in element_menu:
        print(dt.strftime("2023" + "%m%d"))
        if '중식' in menu.text:
            insert_data['tt'] = '중식'
            insert_data['menu'] = menu.text.lstrip('중식\n')
        elif '석식' in menu.text:
            insert_data['tt'] = '석식'
            insert_data['menu'] = menu.text.lstrip('석식\n')
        else:
            insert_data['menu'] = '식당운영 없음\n'
        saveData(cursor, db)

#날짜 변경
def changeDate():
    global dt
    dt = dt + timedelta(days=1)
    insert_data['dt'] = dt.strftime("2023" + "%m%d")

#프로그램 실행
def exeProgram(db, cursor, driver):
    while dt.strftime("%Y-%m-%d") != '2022-06-27':
        for i in range(1, 8):
            element_menu = driver.find_elements(By.XPATH, '//*[@id="jwxe_main_content"]/div/div/div/div/table/tbody/tr/td[' + str(i) + ']')
            setData(element_menu, cursor, db)
            changeDate()
        element = driver.find_element(By.XPATH, '//*[@id="date_next"]').click()

#프로그램 종료
def endProgram(driver, db):
    db.close()
    driver.quit()

db, cursor, driver = initProgram()
exeProgram(db, cursor, driver)
endProgram(driver, db)