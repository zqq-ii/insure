# -*- coding: utf-8 -*-
from Manual_Testing.common import RandomData
import time, datetime, random, string, json, calendar
from dateutil.relativedelta import relativedelta


class RandomStr:
    """
    生成随机字符
    """
    chars = {
        'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        # 'lower': 'abcdefghijklmnopqrstuvwxyz',
        'digit': '0123456789',
        # 'punct': r'''!@#$%^&*''',
    }

    def __init__(self, length=26, *contents):
        self.kinds = {}
        self.length = length
        if len(contents) == 0:
            self.kinds = None
        else:
            for content in contents[0]:
                kind = content.split(':')[0]
                if len(content.split(':')) == 1:
                    self.kinds[kind] = 0
                else:
                    self.kinds[kind] = int(content.split(':')[1])

    def create(self, rs=None):
        res = ''
        charset = ''
        if self.kinds is None:
            charset = ''.join(c for c in RandomStr.chars.values())
        else:
            if self.length < sum(num for num in rs.kinds.values()):
                print('规则不符，生成失败。')
            else:
                for kind, num in rs.kinds.items():
                    if num == 0:
                        pass
                    else:
                        for i in range(num):
                            res += random.choice(RandomStr.chars[kind])
                    charset += RandomStr.chars[kind]
        for i in range(self.length - len(res)):
            res += random.choice(charset)
        str_list = list(res)
        random.shuffle(str_list)
        return 'TENSER' + ''.join(str_list)


def CustomRandomStr(custom="ZDY", length=13):
    """
    随机生成字符串(由大写字母,小写字母,数字组成)
    :param custom: 自定义开头
    :param length: 生成随机数的的总字符长度
    :return:
    """
    random_str = ''.join(random.sample(string.ascii_letters + string.digits, length))
    return str(custom) + random_str


def JsonFormatting(FormattingJson):
    """
    Json格式化
    """  # ensure_ascii默认是True会将中文变为unicode编码
    JsonFormatting = json.dumps(FormattingJson, indent=4, ensure_ascii=False, separators=(',', ': '))
    return JsonFormatting


def newIdNum(year=random.randint(1974, 2001), month=random.randint(1, 12), day=random.randint(1, 29), sex=None):
    """
    生成指定年,月,日,性别的身份证号码
    :param birthyear: 年
    :param birthmonth: 月
    :param birthday: 日
    :param sex: 性别
    :return:
    """
    while True:
        codelist = RandomData.codelist  # 设置地区
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3',
                     '10': '2'}  # 校验码映射
        # 身份证前6位
        try:
            id = codelist[random.randint(0, len(codelist))]  # 地区项
        except:
            id = '110101'
        # 7-10位，出生年份
        try:
            birthdayStr = str(year).zfill(4) + str(month).zfill(2) + str(day).zfill(2)
            id = id + birthdayStr
        except:
            id = id + '19900307'
        # 最后4位的随机前3位
        try:
            sign = random.randint(1, 999)
            id = id + str(sign).zfill(3)  # 顺序号简单处理
        except:
            id = id + '465'
        # 计算校验码,拼接身份证并返回
        sum_1 = 0
        for a in range(0, 17):
            sum_1 += int(id[a]) * weight[a]
        index_id = sum_1 % 11
        result_id = id + str(checkcode[str(index_id)])  # 最终号码
        if sex == "女":
            gender = int(result_id[16])
            if gender % 2 == 0:
                return result_id
            else:
                pass
        elif sex == "男":
            gender = int(result_id[16])
            if gender % 2 != 0:
                return result_id
            else:
                pass
        else:
            return result_id
        sum = 0  # 校验身份证号码
        for i in range(17):
            sum += int(result_id[i]) * weight[i]
        result = sum % 11
        if result in checkcode.keys():
            if str(checkcode.get(result)) == str(result_id[-1]):
                return result_id
            else:
                pass


def Birthday(id_card=newIdNum()):
    """获取身份证中的日期"""
    year = id_card[6:10]
    month = id_card[10:12]
    day = id_card[12:14]
    return ("{}{}{}000000".format(year, month, day))

def qwer(id_card):
    year = int(id_card[6:10])
    month = int(id_card[10:12])
    day = int(id_card[12:14])
    birth_date = datetime.date(year, month, day)
    age = datetime.date.today().year - birth_date.year
    return age


def Nickname():
    """随机生成姓名"""
    surname_list = RandomData.surname_list  # 姓
    name_list = RandomData.name_list  # 名
    surname = random.choice(surname_list)
    name = random.choice(name_list)
    nickname = surname + name
    return nickname


def Mobilephone():
    """随机生成手机号"""
    phone = ''
    phone += str(random.choice(RandomData.phone_number))
    ran = ''
    for i in range(8):
        ran += str(random.randint(0, 9))
    phone += ran
    return phone


def Mailbox():
    """随机生成邮箱"""
    email_suf = random.choice(['@163.com', '@qq.com', '@126.com', '@sina.com', '@sina.cn', '@soho.com', '@yeah.com'])
    phone = Mobilephone()
    email = phone + email_suf
    return email


def BankCard():
    """随机生成银行卡号"""
    card_id = '62'
    for i in range(17):
        ran = str(random.randint(0, 9))
        card_id += ran
    return card_id


# 随机生成企业名称
def EnterpriseName():
    prefix = ['ABC', 'XYZ', 'ACME', 'BEST', 'TOP']
    suffix = ['Corp', 'Inc', 'Ltd', 'LLC']
    return random.choice(prefix) + ' ' + random.choice(string.ascii_uppercase) + random.choice(
        string.ascii_lowercase) + ' ' + random.choice(suffix)


# 随机生成统一社会信用代码
def CreditCode():
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(18))


def Execution_Time():
    """用于打印程序执行时间"""
    Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间
    return Time


def Time():
    """当前时间;可用于保单出单时间或实时生效"""
    Time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 获取当前时间
    return Time


def Tomorrow(day=1):
    """某天后零正时;可用于保单生效期,财险报案,理赔,出单即生效等场景时间"""
    Tomorrow = (datetime.datetime.now() - datetime.timedelta(days=-day)).strftime('%Y%m%d000000')
    return Tomorrow


def TomorrowPresently(day=1):
    """某天后截止时间,到秒(零时用,有点问题)"""
    Tomorrow = (datetime.datetime.now() - datetime.timedelta(days=-day)).strftime('%Y%m%d%H%M%S')
    return int(Tomorrow) - 1


def SeveralDays(day=1):
    """某天后最后截止时间;可用于保单失效,财险报案,理赔,出单即生效等场景时间"""
    Tomorrow = (datetime.datetime.now() - datetime.timedelta(days=-day)).strftime('%Y%m%d235959')
    return Tomorrow


def SeveralMonths(day=1, month=1):
    """距今某月后最后一天截止时间;可用于保单失效期"""
    date = (datetime.datetime.now() - datetime.timedelta(days=-day))
    new_date = (date + relativedelta(months=month))
    current_date = (new_date - datetime.timedelta(days=+1)).strftime('%Y%m%d235959')
    return current_date


def SeveralYears(day=1, year=1):
    """
    (距今某年后最后某天截止时间;可用于保单失效期)
    1,注意失效时间如果在2月份,2月小于29天时传入的最大天数为29;
    2,例:T+30场景,失效在2月该2月最大28天,那么这里传入的应该就是29
    """
    date = (datetime.datetime.now() - datetime.timedelta(days=-day))
    new_date = (date - datetime.timedelta(days=1)).strftime('%Y%m%d235959')
    timeArray = time.strptime(new_date, "%Y%m%d%H%M%S")
    timeStamp = (time.mktime(timeArray))  # 转化为时间戳
    start_year = int(time.strftime('%Y', time.localtime(timeStamp))) + year
    Hour_minute_second = time.strftime('%m%d235959', time.localtime(timeStamp))
    current_date = '{}{}'.format(start_year, Hour_minute_second)
    return current_date


def Yesterday(day=1):
    """某天前此时"""
    # day = day
    Yesterday = (datetime.datetime.now() - datetime.timedelta(days=day)).strftime('%Y%m%d%H%M%S')
    return Yesterday


def Weeklytime(Week=1):
    """某周最后一天截止时间"""
    Weeklytime = (datetime.datetime.now() - datetime.timedelta(weeks=-Week)).strftime('%Y%m%d235959')
    return Weeklytime


def monthtime():
    """本月最后一天时间截止时间"""
    month = (datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month + 1, 1) - datetime.timedelta(
        days=1)).strftime('%Y%m%d235959')
    return month


def Issue_tp(day=-2):
    """(太平_碎屏责任险)出单时间"""
    Issue_tp = (datetime.datetime.now() - datetime.timedelta(days=-day)).strftime('%Y%m%d235900')
    return Issue_tp


def Tomorrow_tp(day=-1):
    """(太平_碎屏责任险)生效时间/出单即生效出单时间"""
    Tomorrow_tp = (datetime.datetime.now() - datetime.timedelta(days=-day)).strftime('%Y%m%d000050')
    return Tomorrow_tp


def SeveralMonths_tp(day=0, month=1):
    """距今某月后最后一天截止时间;可用于保单失效期"""
    date = (datetime.datetime.now() - datetime.timedelta(days=-day))
    new_date = (date + relativedelta(months=month))
    current_date = (new_date - datetime.timedelta(days=+1)).strftime('%Y%m%d000049')
    return current_date


def SeveralYears_tp(day=0, year=1):
    """(太平_碎屏责任险)失效时间"""
    date = (datetime.datetime.now() - datetime.timedelta(days=-day))
    new_date = (date - datetime.timedelta(days=+1)).strftime('%Y%m%d000049')
    timeArray = time.strptime(new_date, "%Y%m%d%H%M%S")
    timeStamp = (time.mktime(timeArray))  # 转化为时间戳
    start_year = int(time.strftime('%Y', time.localtime(timeStamp))) + year
    Hour_minute_second = time.strftime('%m%d000049', time.localtime(timeStamp))
    current_date = '{}{}'.format(start_year, Hour_minute_second)
    return current_date


if __name__ == '__main__':
    for i in range(10):
        print(newIdNum(1998, 1, 7, "男"))  # 随机生成身份证

    print(Time(), Tomorrow(), SeveralYears())
