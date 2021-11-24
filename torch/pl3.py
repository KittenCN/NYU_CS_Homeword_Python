import requests
from requests.exceptions import RequestException
import csv
from bs4 import BeautifulSoup as bs

def write_to_file(item):
    file_name = "PLS.csv"
    # "a"为追加模式（添加）
    # utf_8_sig格式导出csv不乱码
    with open(file_name, "a", encoding="utf_8_sig", newline="") as f:
        fieldnames = ["期号", "中奖号码", "开奖日期"]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writerow(item)

def get_page(i):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        url = "http://www.lottery.gov.cn/historykj/history_" + str(i) + ".jspx?_ltype=pls"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            print("return code is %s" % (str(response.status_code)))
            return None

    except RequestException:
        print("访问异常")

def parse_one_page(get_html):
    pls = {}
    data = bs(get_html, "lxml")
    data = data.find("tbody").find_all("tr")
    for content in data:
        all_tr = content.find_all("td")
        pls["期号"] = all_tr[0].get_text()
        pls["中奖号码"] = all_tr[1].get_text()
        pls["开奖日期"] = all_tr[10].get_text()
        write_to_file(pls)

def crawler():
    for i in range(1, 283):
        parse_one_page(get_page(i))

if __name__ == "__main__":
    crawler()