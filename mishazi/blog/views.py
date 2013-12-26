#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2013-12-26 17:00:21
# @Last Modified by:   LiSnB
# @Last Modified time: 2013-12-26 17:05:40
# @Email: lisnb.h@gmail.com# Create your views here.

from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)