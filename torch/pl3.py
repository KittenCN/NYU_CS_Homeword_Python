import requests
from requests.exceptions import RequestException
import csv
from bs4 import BeautifulSoup as bs
import SqliteHelper as sh

def write_to_file(item):
    file_name = "PLS.csv"
    # "a"为追加模式（添加）
    # utf_8_sig格式导出csv不乱码
    with open(file_name, "a", encoding="utf_8_sig", newline="") as f:
        fieldnames = ["期号", "中奖号码", "开奖日期"]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writerow(item)

def get_page():
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        # url = "http://www.lottery.gov.cn/historykj/history_" + str(i) + ".jspx?_ltype=pls"
        url = "https://datachart.500.com/pls/history/inc/history.php?limit=15116&start=04001&end=99999"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            print("return code is %s" % (str(response.status_code)))
            return None

    except RequestException:
        print("访问异常")

def parse_html(html):
    soup = bs(html, 'lxml')  # 创建网页解析器对象
    i = 0
    #查找网页里的tr标签,从第4个tr读到倒数第2个tr,因为通过对网页分析,前三个和最后一个tr没用
    for item in soup.select('tr')[3:-1]:  # 把查到的tr组成一个列表,item是列表指针,for每循环一次,item就选下一个tr,读完列表本循环结束,函数就结束,
        try:   # 不加try和except有的值是&nbsp,是网页里的空白键,会出错,加上调试命令忽略错误,后边统一处理             
            yield{  # yield作用是得到数据立即返回给调用函数,但不退出本循环本函数
                    'issue':item.select('td')[i].text,  # item查到的第0个td是开奖期号,写到time列
                    'WinningNumbers':item.select('td')[i + 1].text,  # 0+1个td是中奖号码
                    'sum':item.select('td')[i + 2].text,  # 总和数
                    'Totalsales':item.select('td')[i + 3].text,  # 总销售额
                    'Direct':item.select('td')[i + 4].text,  # 直选中奖注数
                    'Direct_bonus':item.select('td')[i + 5].text,  # 直选总奖金
                    'three_selection':item.select('td')[i + 6].text,  # 组选3中奖注数
                    'three_selection_bonus':item.select('td')[i + 7].text,  # 组选3总奖金
                    'six__selection':item.select('td')[i + 8].text,  # 组选6中奖数
                    'six__selection_bonus':item.select('td')[i + 9].text,  # 组选6总奖金
                    'time':item.select('td')[i + 10].text  # 开奖日期
                    #一组数据读完马上把值返回给调用函数,但没有退出本函数和本循环,
                    #调用函数得到数据,写到excel对象里,然后又回到这里,本次循环结束,开始下一次循环,item列表指针
            }
        except IndexError:
            pass             

def parse_one_page(get_html):
    _db = sh.Connect("pl3.db")
    plsData = []
    if get_html is not None:
        print("正在写入...")
        for item in parse_html(get_html):
            pls = {}
            #下边的if是为了去掉列表里的乱码&nbsp,在网页里显示为空白,用0代替
            if item['three_selection'] == '&nbsp':
                item['three_selection'] = '0'
                item['three_selection_bonus'] = '0'
            else:
                item['six__selection'] = '0'
                item['six__selection_bonus'] = '0'
            strData = "".join(item['WinningNumbers'].split())
            pls["OriIndex"] = item['issue']
            pls["OriDate"] = item['time']
            pls["OriData"] = strData
            pls["SortData"] = getSortData(strData)
            pls["SumData"] = getSumData(strData)
            pls["OE"] = getOE(strData)
            pls["BS"] = getBS(strData)
            plsData.append(pls)
    _db.table('pl3').data(plsData).add()
    _db.close()
    print("写入完成")

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
    parse_one_page(get_page())

def replaceCount(index):
    _db = sh.Connect("pl3.db")
    _data = _db.table('pl3').findAll()
    _pridata = [0] * 1000
    sumcount = 0
    for i in range(index):
        _pridata[int(_data[i]['SortData'])] += 1
    for i in range(index):
        if _pridata[i] > 1:
            sumcount += _pridata[i]
    _db.close()
    return round(sumcount / index, 4) * 100

def smartCount():
    smartList = [27,35,37,38,45,47,56,57,58,67,78,126,129,136,138,156,167,236,238,239,249,256,259,267,269,346,347,348,349,356]
    _db = sh.Connect("pl3.db")
    _data = _db.table('pl3').findAll()
    sumcount = 0
    for i in range(len(_data)):
        if int(_data[i]['SortData']) in smartList:
            sumcount += 1
    _db.close()
    return round(sumcount / len(_data), 4) * 100

if __name__ == "__main__":
    while True:
        print("")
        select = input("请选择操作:\n1.爬取数据\n2.处理数据\n3.退出\n")
        if select == "1":
            crawler()
            print("")
        elif select == "2":
            print("近100期重复率:" + str(replaceCount(100)) + "%")
            print("近50期重复率:" + str(replaceCount(50)) + "%")
            print("近30期重复率:" + str(replaceCount(30)) + "%")
            print("近10期重复率:" + str(replaceCount(10)) + "%")
            print("")
            print("总智能重复率:" + str(smartCount()) + "%")
            print("")
        elif select == "3":
            break