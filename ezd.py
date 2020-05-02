from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def group_to_eng(group):
    if (group == "А"):
        return "A"
    elif (group == "Б"):
        return "B"
    elif (group == "В"):
        return "C"
    elif (group == "Г"):
        return "D"
    elif (group == "Д"):
        return "E"


def successs():
    print("Оценки выставлены!")


def auth(driver, ezd_login, ezd_password):
    driver.get("https://dnevnik.mos.ru/")
    driver.implicitly_wait(10)
    driver.find_element_by_partial_link_text("УЧИТЕЛЯ").click()
    driver.implicitly_wait(10)
    login = driver.find_element_by_xpath("//input[1]")
    login.send_keys(ezd_login)
    password = driver.find_element_by_xpath("//input[@type='password']")
    password.send_keys(ezd_password)
    driver.find_element_by_xpath("//button[@class='b-login__btn']").click()
    driver.implicitly_wait(10)


def put(url, name, mark, group, driver, day_id):
    driver.get(url)
    time.sleep(5)
    if(int(mark) == 2):
        print(group, name, mark, "не выставлено, 2 не буду выставлять")
        return False
    elif(day_id == "none"):
        print(group, name, mark, "не выставлено, даты нет")
        return False
    else:
        driver.find_element_by_xpath("//div[2]/div/md-icon").click()
        try:
            name_element = driver.find_element_by_partial_link_text(name.title())
            id = name_element.get_attribute("href")[42:]
            print(id)
            id_url = "//journal-cell[@id='" + id + "-" + day_id + "-0']/div"
            driver.find_element_by_xpath(id_url).click()
            time.sleep(1)
            driver.find_element_by_xpath("//md-menu[@class='md-menu _md _3Q492']").click()

            time.sleep(1)
            driver.find_element_by_xpath("//md-menu-item[@title='Домашняя работа']").click()
            driver.find_element_by_name("journalMarkValue").click()
            driver.find_element_by_name("journalMarkValue").clear()
            driver.find_element_by_name("journalMarkValue").send_keys(int(mark))
            driver.find_element_by_xpath("//md-dialog-content/main/form/div[5]/button/span").click()
            time.sleep(1)
            driver.execute_script("scrollBy(0,-500);")
            print(group, name, mark)
            return True
        except NoSuchElementException:
            print(group, name, mark, "не выставлено, нет такой фамилии")
            return False
