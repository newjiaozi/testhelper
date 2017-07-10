#coding:utf-8
'''
Created on 2017年2月20日

@author: ldl
'''


from django import forms
import datetime,time

class CheckPlanForms(forms.Form):    
    count_choices = (
                    (3,u'3期',),
                    (6,u'6期'),
                    (9,u'9期'),
                    (12,u'12期'),
                    (18,u'18期'),
                    (24,u'24期'),
                    (36,u'36期'),
                    ([6,6],u'6+6期'),
                    ([6,12],u'6+12期'),
                    ([6,18],u'6+18期'),
                    ([9,15],u'9+15期'),
                    ([12,24],u'12+24期'),                    
                    )
    count = forms.ChoiceField(choices = count_choices,label=u'借款期数')
    money =  forms.FloatField(label=u'借款金额',min_value=1)
    kt = forms.FloatField(label=u'砍头息')
    lv = forms.FloatField(label=u'年化利率')



class CreateRepaementForms(forms.Form):
    env_choice = (
                  ('stb',u'stb环境'),
                  ('sit',u'sit环境'))
    
    env = forms.ChoiceField(choices= env_choice,label = u'环境') 
    mobile = forms.IntegerField(max_value=18999999999,min_value=1,label = u'手机号')




class CodisFlushForms(forms.Form):
    env_choice = (
                  (['http://10.3.1.6:8081/system/redis/table.json',['http://10.3.1.6:8081/system/auth/login.json','admin','qwe123']],u'stb环境'),
                  (['http://server.sit.maiyafenqi.com/system/redis/table.json',['http://server.sit.maiyafenqi.com/system/auth/login.json','admin','qwe123']],u'sit环境'),
                  (['http://server.pre.maiyafenqi.com/system/redis/table.html',['http://server.pre.maiyafenqi.com/system/auth/login.json','cuidongzhu','cdz-2256836']],u'pre环境'),
                  (['http://server.maiyafenqi.com/system/redis/table.json',['http://server.maiyafenqi.com/system/auth/login.json','cuidongzhu','cdz-2256836']],u'prd环境'),)
    
    table_choice = (
                    ('ORD_ORDER','ORD_ORDER'),
                    ('ORD_ORDER_PART','ORD_ORDER_PART'),
                    ('ORD_USER','ORD_USER'),
                    ('ORD_USER_ACCOUNT','ORD_USER_ACCOUNT'),
                    ('ORD_USER_DETAIL','ORD_USER_DETAIL'),
                    ('ORD_USER_HONOR','ORD_USER_HONOR'),
                    ('ORD_AUTH_STATUS','ORD_AUTH_STATUS'),
                    )

    
    env = forms.ChoiceField(choices=env_choice,label=u'环境')
    table = forms.ChoiceField(choices=table_choice,label=u'表名')
    


class TimesTampForms(forms.Form):
    unixtime_data = forms.IntegerField(label=u'unixtime转北京时间',required=False,initial=time.mktime(datetime.datetime.today().timetuple()))
    bjtime_data = forms.DateTimeField(label=u'北京时间转unixtime',required=False,initial=datetime.datetime.today(),input_formats=["%Y-%m-%d %H:%M:%S"])



class Base64ImageForms(forms.Form):
    image_file = forms.FileField(label=u'图片') 
    
    
    
class ImageBase64Forms(forms.Form):
    base64_text = forms.CharField(widget=forms.Textarea,label=u"base64数据")
    
    
class InterfaceTestForms(forms.Form):
    
    method_choice = (("POST","POST"),
                     ("GET","GET"))    
    url = forms.URLField(label=u'请求地址') 
    method = forms.ChoiceField(choices=method_choice,label=u"请求方法")
    counts = forms.IntegerField(label=u"请求次数",min_value=1,initial=1)
    data = forms.CharField(widget = forms.Textarea,label=u"请求数据",required=False)
 
 
class ChangeMoneyForms(forms.Form):
    env_choice =((['cuidongzhu','cdz-2256836'],u"prd环境"),)
    env = forms.ChoiceField(label=u"环境",choices=env_choice)
    orderno = forms.CharField(label=u'订单编号')
    principal = forms.IntegerField(label=u"金额",min_value=1,max_value=100)
   
class Params2DictForms(forms.Form):
    params = forms.CharField(widget=forms.Textarea,label=u"参数")  
    
    
    
class GetRateUUIDForms(forms.Form):
    env_choice = (([['http://10.3.1.6:8081/system/auth/login.json','admin','qwe123'],"http://server.stb.maiyafenqi.com/a/shop/rateTable/getShopRateHeaderList.json"],u"stb环境"),
                  ([['http://server.sit.maiyafenqi.com/system/auth/login.json','admin','qwe123'],"http://server.sit.maiyafenqi.com/shop/rateTable/getShopRateHeaderList.json"],u"sit环境"),
                  ([['http://server.pre.maiyafenqi.com/system/auth/login.json','cuidongzhu','cdz-2256836'],"http://server.pre.maiyafenqi.com/shop/rateTable/getShopRateHeaderList.json"],u"pre环境"),
                  ([['http://server.maiyafenqi.com/system/auth/login.json','cuidongzhu','cdz-2256836'],"http://server.maiyafenqi.com/shop/rateTable/getShopRateHeaderList.json"],u"prd环境"),)  
    
    env = forms.ChoiceField(label=u"环境",choices=env_choice)
    shopid = forms.IntegerField(label=u"商户ID")   