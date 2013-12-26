#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2013-12-26 17:00:21
# @Last Modified by:   LiSnB
# @Last Modified time: 2013-12-26 17:59:38
# @Email: lisnb.h@gmail.comfrom django.db import models

from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=127)
	body=models.TextField()
	publish_datetime=models.DateTimeField(auto_now=True)
	last_modify_datetime=models.DateTimeField(auto_now=True)
	author=models.CharField(max_length=50)
	# lastedition=models.ForeignKey(Article)
	# nextedition=models.ForeignKey(Article)

	def __unicode__(self):
		return self.title
