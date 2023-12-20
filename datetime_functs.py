import datetime
import pytz

def dater():
    data = datetime.datetime.now()
    print(data)

def todayy():
    h = datetime.datetime.today()
    print(h)

def utc():
    ss = datetime.datetime.utcnow()
    print(ss)

def utc_changer():
    data = datetime.datetime.now(tz=pytz.utc)
    changed = data.astimezone(pytz.timezone('Asia/Tashkent'))
    print(changed)

def ready_1():
    data = datetime.datetime.now()
    print(data.strftime('%b, %d, %y'))

def ready_2():
    data = datetime.datetime.now()
    print(data.strftime('%y, %m, %d'))

def ready_3():
    data = datetime.datetime.now()
    print(data.strftime('%f, %z, %j'))

def datatime_date_01():
    hhh = datetime.date.today()
    print(hhh)
def datatime_date_02():
    dateee = datetime.date.today()
    hhh = datetime.date.isoweekday(dateee)
    print(hhh)
dater()
utc_changer()
ready_1()
ready_2()
ready_3()
utc()
datatime_date_01()
datatime_date_02()