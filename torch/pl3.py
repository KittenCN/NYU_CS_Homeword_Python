import requests
from requests.exceptions import RequestException
import csv
from bs4 import BeautifulSoup as bs
import SqliteHelper as sh
import numpy

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
        # url = "http://www.lottery.gov.cn/historykj/history_" + str(i) + ".jspx?_ltype=pls"
        url = "https://datachart.500.com/pls/history/inc/history.php?limit=15116&start=04001&end=04011"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            print("return code is %s" % (str(response.status_code)))
            return None

    except RequestException:
        print("访问异常")

def parse_one_page(get_html, intMaxPage):
    _db = sh.Connect("pl3.db")
    plsData = []
    for i in range(intMaxPage):
        print("正在写入")
        data = bs(get_html[i], "lxml")
        data = data.select("tr")
        data = numpy.array(data)
        for content in data[3, len(data) - 1]:
            pls = {}
            all_tr = content.find_all("td")
            # pls["期号"] = all_tr[0].get_text()
            # pls["中奖号码"] = all_tr[1].get_text()
            # pls["开奖日期"] = all_tr[10].get_text()
            # write_to_file(pls)
            strData = "".join(all_tr[1].get_text().split())
            # _db.table("pl3").add({
            #     "OriIndex": all_tr[0].get_text(),
            #     "OriDate": all_tr[10].get_text(),
            #     "OriData": strData,
            #     "SortData": getSortData(strData),
            #     "SumData": getSumData(strData),
            #     "OE": getOE(strData),
            #     "BS": getBS(strData)
            # })
            pls["OriIndex"] = all_tr[0].get_text()
            pls["OriDate"] = all_tr[7].get_text()
            pls["OriData"] = strData
            pls["SortData"] = getSortData(strData)
            pls["SumData"] = getSumData(strData)
            pls["OE"] = getOE(strData)
            pls["BS"] = getBS(strData)
            plsData.append(pls)
    _db.table('pl3').data(plsData).add()
    _db.close()

def getOE(_data):
    listData = list(_data)
    odd = 0
    even = 0
    for i in range(3):
        if int(listData[i]) % 2 == 0:
            even += 1
        else:
            odd += 1
    return str(odd) + ":" + str(even)

def getBS(_data):
    listData = list(_data)
    big = 0
    small = 0
    for i in range(3):
        if int(listData[i]) < 5:
            small += 1
        else:
            big += 1
    return str(big) + ":" + str(small)

def getSortData(_data):
    listData = list(_data)
    listData.sort()
    return "".join(listData)

def getSumData(_data):
    listData = list(_data)
    SumData = 0
    for i in range(3):
        SumData += int(listData[i])
    return SumData

def getMaxPage(get_html):
    data = bs(get_html, "lxml")
    ans = data.select("option ")
    return len(ans)

def crawler():
    # intMaxPage = getMaxPage(get_page(1))
    intMaxPage = 1
    htmls = []
    for i in range(1, intMaxPage + 1):
        print("正在爬取")
        # parse_one_page(get_page(i))
        htmls.append(get_page(i))
    parse_one_page(htmls, intMaxPage)

if __name__ == "__main__":
    crawler()