# -*- coding: utf-8 -*- 

'''
Created on 2016年4月19日

@author: Administrator
'''
import unittest
import time
from appium import webdriver

global driver

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param1=None,param2=None):
 
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param1 = param1
        self.param2 = param2
    @staticmethod
    def parametrize(testcase_klass, param1=None,param2=None):
  
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param1=param1,param2=param2))
            
        return suite
    
    @classmethod
    def setUpClass(self):
        print "类方法调用者：",self.__name__
        desired_caps={}

        desired_caps['deviceName'] = 'YHWWSOTSUKHMIJYD'

        desired_caps['platformName']='Android'

        desired_caps['platformVersion']='5.0.2'

        desired_caps['appPackage'] = 'com.togo.apps'  #被测App的包名
        desired_caps['unicodeKeyboard']="True"
        desired_caps["resetKeyboard"]="True"
#        desired_caps["/Users/zhao/Downloads/togo_160226_r3027_v1.1.3_demo.apk"]
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        
    @classmethod
    def tearDownClass(self):

        self.driver.quit()

#    def setUp(self):
#      print ("setup")

#    def tearDown(self):
#      print ("teardown")
      
    def test_awipePage(self):
         
         try:
            self.driver.find_element_by_id("com.togo.apps:id/cover_image")
            
         except EOFError:
            print ('no such element')
         time.sleep(3)
         found = False
         pageCount = 5
         currentPage = 0
         while (found == False and currentPage < pageCount):
             found = True
             currentPage += 1
             try:
               go=self.driver.find_element_by_id("com.togo.apps:id/main_go_image")
             except Exception:
               found = False
             if found==True:
               break
        
             self.driver.swipe(1060,20,10,20)
          
         
         go.click()
    