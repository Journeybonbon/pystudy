from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import urllib.request
import os
import time

#해당 디렉토리가 없으면 디렉토리 생성
def makeDir(path):
    if not os.path.exists(path):
        os.makedirs(path)

#이미지 저장
def saveImages(element, save_path):
    file_name = 1
    for my_href in element:
        src = my_href.get_attribute("src")
        if "data:image/gif;" in src:
            continue
        new_path = save_path + str(file_name) +'.jpg'
        urllib.request.urlretrieve(src, new_path)
        print(src)
        print("Saved ! " + str(file_name))
        file_name += 1

#검색창으로 이동
def goHome():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.get("https://www.naver.com")
    return driver

#이미지 탭에 들어가서 xpath 가져오기
def Searching(driver, v):
    element = driver.find_element(
            By.XPATH, '//*[@id="query"]').send_keys(v)
    element = driver.find_element(
                By.XPATH, '//*[@id="search_btn"]').click()
    element = driver.find_element(
                By.XPATH, '//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()
    driver.implicitly_wait(3)
    element = driver.find_elements(
            By.XPATH, '//*[@id="main_pack"]/section[2]/div/div[1]/div[1]/div/div/div[1]/a/img')
    return element

#검색값 입력
def getPath(v):
    save_path = '{images파일의 경로}' + v + "/"
    makeDir(save_path)
    return save_path

#이미지 가져오기
def downloadImgs(v):
    driver = goHome()
    images = Searching(driver, v)
    save_path = getPath(v)
    saveImages(images, save_path)
    time.sleep(2)
    driver.quit()

v = ["고양이", "강아지", "토끼", "말"]
for i in v:
    downloadImgs(i)