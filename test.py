#-*-coding=utf-8-*-
#author:shichao
import requests
import unittest
import json

class MyTest(unittest.TestCase):     #封装测试环境的初始化和还原的类
    def setUp(self):                 #放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！
        print("start test")          #打印出start test
        pass
    def tearDown(self):              #与setUp()相对
        print("end test")            #打印出end test
        pass
class test_xxx_get(MyTest):          #把这个接口封装一个类，下面的方法是具体的测试用例
    '''接口信息例如**功能'''          #这个描述接口名称，""" 文字 可打印在输出台
    def test_***_get(self):
        '''testcase001：***'''         #这个描述接口用例名称
        self.url = "http://***.***.***/api/xxx/get"  #请求url
        self.headers = {"Content-Type":"application/json"} #请求头
        self.data = {                            #请求参数写入data
            "token": "abcdefg",
            "id": 1,
            "param": {
                "QuId": 14 
            }
        }    #self.用在方法属性中，表示是该方法的属性，不会影响其他方法的属性。
        r = requests.post(url = self.url,json = self.data,headers = self.headers)
        #return r.json()
        print (self.r.text)
        print (self.r.status_code)
        self.assertIn("true",self.r.text)     #断言判断接口返回是否符合要求，可以写多个断言！

if __name__=="__main__":
    unittest.main()
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(MyTest("test_xxx_get"))   
    # suiteTest.addTest(MyTest("test_xxx_get_002"))

# 按照一定时间格式获取当前时间(防止测试报告覆盖)
now = time.strftime(u'%Y-%m-%d-%H-%M-%S')
# 确定生成报告的路径
report_file = "自定义本地存储路径" + now + "_test_report.html"
with open(report_file, 'wb') as report:
    runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=u'title',
                                           description=u'描述',
                                           tester=u'测试人员')
    # runner = unittest.TextTestRunner()
    runner.run(suiteTest)
    report.close()