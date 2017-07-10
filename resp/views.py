#coding:utf-8

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


import json
import logging

from resp.testdata import getResp


logger = logging.getLogger()




@csrf_exempt
def respBad(request):
    logger.info("**"*30)
    if request.method == "POST":
        honorType=""
        req_body =  request.body 
        if isinstance(req_body, str):
            try:
                res_body_json = json.loads(req_body)
                logger.info(type(res_body_json))
                honorType = res_body_json.get("honorType",None)
            except Exception,e:
                logger.error(e)
                return HttpResponse(u"%s" % e) 
        elif isinstance(req_body, dict):
            honorType = req_body.get("honorType",None)
            
        return whichHonor(request, honorType)
            
    logger.info(u"非POST请求，请求未处理")
    return HttpResponse(u"非POST请求，请求未处理")


    
    
def whichHonor(request,honorType):
    if honorType == "JXL_TB_GATHER_DATA":
        taobao = getResp("taobao")
        if taobao:
            json_string = json.dumps(taobao,indent=4,ensure_ascii=False)
            logger.info(json_string)
            return HttpResponse(json_string) 
    elif honorType == "MOXIE_REPORT_DATA_CARRIER":
        moxie = getResp("moxie")
        if moxie:
            json_string = json.dumps(moxie,indent=4,ensure_ascii=False)
            logger.info(json_string)
            return HttpResponse(json_string)
    else:
        return HttpResponse(u"请求未处理")