# -*- coding: utf-8 -*- 
'''
Created on 2016年4月19日

@author: Administrator
'''
import unittest
import time
from ParametrizedTestCase import ParametrizedTestCase
    
class TestLogin(ParametrizedTestCase):
    '''
    def test_something(self):
        print 'param1 =', self.param1
        print 'param2 =', self.param2
        self.assertEqual(1, 1)
    
        if self.param:
            print "true"
        else :
            print "false"
    
#class TestTwo(ParametrizedTestCase):    
    def test_something_else(self):
         print 'param1 =', self.param1
         print 'param2 =', self.param2
         self.assertEqual(2, 2)
    '''
    def test_login(self):
        print 'param1 =', self.param1
        print 'param2 =', self.param2
        self.driver.find_element_by_id("com.togo.apps:id/register_phone_edit").send_keys(self.param2)  

        self.driver.find_element_by_id("com.togo.apps:id/register_getverifycode_text").click()
         
        self.driver.find_element_by_id("com.togo.apps:id/register_verifycode_edit").send_keys('1290')
      
        self.driver.find_element_by_id("com.togo.apps:id/register_button").click()
                
        if self.param1 :
            self.driver.find_element_by_id("com.togo.apps:id/improve_userinfo_nick_edit").click()
            self.driver.find_element_by_id("com.togo.apps:id/improve_userinfo_nick_edit").send_keys("user")
            self.driver.find_element_by_id("com.togo.apps:id/improve_userinfo_email_edit").click()
            self.driver.find_element_by_id("com.togo.apps:id/improve_userinfo_email_edit").send_keys("test@mail.com")
            self.driver.find_element_by_id("com.togo.apps:id/improve_userinfo_next_button").click()
            self.assertEquals(self.driver.find_element_by_id("com.togo.apps:id/header_title").text(),"驾照认证")
            self.driver.find_element_by_id("com.togo.apps:id/driver_license_bind_upload_button").click()
            self.driver.find_element_by_id("com.android.camera:id/v6_shutter_button_internal").click()
            time.sleep(3)
            self.driver.find_element_by_id("com.android.camera:id/v6_btn_done").click()
            time.sleep(3)
            self.driver.find_element_by_id("com.togo.apps:id/driver_license_bind_button").click()
            time.sleep(3)
            self.assertEquals(self.driver.find_element_by_id("com.togo.apps:id/header_title").text(),"信用认证")
            self.driver.find_element_by_id("com.togo.apps:id/header_right_text").click()
            self.assertTrue(self.driver.find_element_by_id("com.togo.apps:id/main_go_image").is_displayed())
        else :
            self.assertTrue(self.driver.find_element_by_id("com.togo.apps:id/main_go_image").is_displayed())   
    
##用法-测试

suite = unittest.TestSuite()
suite.addTest(ParametrizedTestCase.parametrize(TestLogin, param1=False,param2='11500000000'))
unittest.TextTestRunner(verbosity=2).run(suite)