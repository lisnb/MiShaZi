#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2013-12-26 17:00:21
# @Last Modified by:   LiSnB
# @Last Modified time: 2013-12-26 20:08:27
# @Email: lisnb.h@gmail.com# Create your views here.

from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    t=get_template('template_root.html')
    c=Context({'current_time':now})
    html=t.render(c)
    return HttpResponse(html)

def add_article(request):
	return render_to_response('template_article_add.html')