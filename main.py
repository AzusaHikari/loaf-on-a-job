import time
from numberToChinese import to_chinese
import datetime


def 获取周末():
    周末 = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    while 周末.weekday() != 5 and 周末.weekday() != 6:
        周末 += one_day
    return str(周末)


def 距离(day1, day2):
    return int((time.mktime(time.strptime(day1, "%Y-%m-%d"))-time.mktime(time.strptime(day2, "%Y-%m-%d")))/(24*60*60))


今天 = str(datetime.date.today())
print("【摸鱼办】提醒您：", time.strftime('%Y年%m月%d日', time.localtime(time.time())), "早上好，摸鱼人！即使今天是开工", to_chinese(距离(今天, "2022-02-06")),
      "天，也一定不要忘记摸鱼哦！有事没事起身去茶水间，去厕所，去廊道走走别总在工位坐着，钱是老板的，但健康是自己的。", sep="")
print("距离【周末】还有：{0}天".format(距离(获取周末(), 今天)))
print("距离【中秋】还有：{0}天".format(距离("2022-09-10", 今天)))
print("距离【国庆】还有：{0}天".format(距离("2022-10-01", 今天)))
print("距离【元旦】还有：{0}天".format(距离("2023-01-01", 今天)))
print("距离【春节】还有：{0}天".format(距离("2023-01-21", 今天)))
