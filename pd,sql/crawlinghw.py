from readline import insert_text
import pandas as pd
import pymysql
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import urllib.request
import os
import time

#onestop 페이지 접근
def getDriver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.get("https://www.kumoh.ac.kr/_common/login/login.do?Return_Url=https://onestop.kumoh.ac.kr")
    return driver

#아이디와 비밀번호 입력 후 로그인
def logIn(driver):
    element = driver.find_element(By.XPATH, '//*[@id="member_id"]').send_keys('')
    element = driver.find_element(By.XPATH, '//*[@id="member_pw"]').send_keys('')
    element = driver.find_element(By.XPATH, '//*[@id="loginForm"]/fieldset/div/input').click()
    driver.implicitly_wait(3)

#개설강좌조회 메뉴로 이동
def moveMenu(driver):
    driver.switch_to.frame("LeftFrame")
    time.sleep(3)
    element = driver.find_element(By.XPATH, '//*[@id="LEFT_MENU.ls_메뉴명1"]').click()
    driver.implicitly_wait(3)
    element = driver.find_element(By.XPATH, '//*[@id="LEFT_MENU.ls_메뉴명14"]').click()
    element = driver.find_element(By.XPATH, '//*[@id="LEFT_MENU.ls_메뉴명26"]').click()
    driver.switch_to.parent_frame()
    driver.switch_to.frame("w_cre_s9241")
    time.sleep(3)

#개설강좌 엑셀 파일 다운
def downloadFile(driver):
    element = driver.find_element(By.XPATH, '//*[@id="Form_버튼.pb_조회"]').click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, '//*[@id="Form_버튼.pb_엑셀"]').click()
    time.sleep(3)

#파일 다운 전체코드 실행
def exeGetFile():
    driver = getDriver()
    logIn(driver)
    moveMenu(driver)
    downloadFile(driver)
    time.sleep(5)
    driver.close()

#DB 연결
def connectDB():
    db = pymysql.connect(host='', 
        port=, 
        user='', 
        passwd='', 
        db='',
        charset='utf8')
    return db

#다운 받은 엑셀 파일 열어서 셋팅 후 딕셔너리 형태로 변환
def openFile():
    temp = pd.read_excel('파일 경로/' + 'test.xlsx', index_col=0)
    n = 'None'
    a = temp.fillna(n)
    b = a.iloc[:,0:13]
    insert_data = b.to_dict('records')
    return insert_data

#sql qeury문
def setQuery():
    placeholders = ', '.join(['%s'] * 13)
    columns = '`년도`, `학기`, `교과목_종류`, `교육과정명`, `이수_대상_학년`, `이수_구분`, `교과목명`, `학점`, `개설교과목코드`, `담당교수`, `수강학과`, `강의시간강의실`, `제한_인원`, `수강_인원`, `수강_꾸러미`'
    sql_query = "INSERT INTO xe_kumohtime ( %s ) VALUES (2023, '1', %s )" % (columns, placeholders)
    return sql_query

#DB에 저장
def saveDB(cursor, insert_data):
    sql = setQuery()
    for i in range(len(insert_data)):
        cursor.execute(sql, list(insert_data[i].values()))
        print("SAVED" + str(i))

#DB에 저장하는 전체 코드 실행
def exeSaveDB():
    db = connectDB()
    cursor = db.cursor()
    insert_data = openFile()
    saveDB(cursor, insert_data)
    db.commit()


exeGetFile()
exeSaveDB()