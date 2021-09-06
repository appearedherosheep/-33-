import requests
from bs4 import BeautifulSoup
from time import time, localtime


def call_ymd():
    a = localtime(time())
    year = a.tm_year
    mon = a.tm_mon
    day = a.tm_mday
    return year*10000+mon*100+day


def call_hmin():
    a = localtime(time())
    hour = a.tm_hour
    return hour


def pretty_date():
    a = localtime(time())
    return f'{a.tm_year}년 {a.tm_mon}월 {a.tm_mday}일'


def tidy(Text):
    word_list = Text.split()
    res = " ".join(word_list)
    return res


def build_menu_list(li, list):
    for i in li:
        res = i.text
        res = res.replace(" ", "")
        list.append(res)


def extract_str(menu, List):
    for a in range(1, len(menu)):
        string = menu[a].split('.')
        string = string[0]
        string = ''.join([i for i in string if not i.isdigit()])
        List.append(string)


def main_scraper(date):
    URL = f'http://school.cbe.go.kr/cbs-h/M01050705/list?ymd={date}'

    result = requests.get(URL)
    html = result.text
    soup = BeautifulSoup(html, "html.parser")
    li = soup.select('li.tch-lnc-wrap')

    menu = []
    build_menu_list(li, menu)
    return menu


def return_breakfast(date):
    li_menu = main_scraper(date)
    max_menu_num = len(li_menu)
    menu_breakfast = []
    menu_breakfast.append(f'{date}')

    if max_menu_num == 0:
        menu_breakfast.append("업데이트 중...")
    elif max_menu_num == 2 or max_menu_num == 3:
        breakfast = li_menu[0].split()
        extract_str(breakfast, menu_breakfast)
    breakfast_list = ''
    for i in range(len(menu_breakfast)):
        breakfast_list = breakfast_list + '\n' + menu_breakfast[i]

    return breakfast_list


def return_lunch(date):
    li_menu = main_scraper(date)
    max_menu_num = len(li_menu)
    menu_lunch = []
    menu_lunch.append(f'{date}')

    if max_menu_num == 0:
        menu_lunch.append("업데이트 중...")

    elif max_menu_num == 2 or max_menu_num == 3:
        lunch = li_menu[1].split()
        extract_str(lunch, menu_lunch)

    lunch_list = ''
    for i in range(len(menu_lunch)):
        lunch_list = lunch_list + '\n' + menu_lunch[i]

    return lunch_list


def return_dinner(date):
    li_menu = main_scraper(date)
    max_menu_num = len(li_menu)
    menu_dinner = []
    menu_dinner.append(f'{date}')

    if max_menu_num == 0:
        menu_dinner.append("업데이트 중...")

    elif max_menu_num == 2 or max_menu_num == 1:
        menu_dinner.append("도시락 개꿀❤\n아님 말고~")

    elif(max_menu_num == 3):
        dinner = li_menu[2].split()
        extract_str(dinner, menu_dinner)

    dinner_list = ''
    for i in range(len(menu_dinner)):
        dinner_list = dinner_list + '\n' + menu_dinner[i]

    return dinner_list
