# -*- coding:utf-8 -*-
# Created by yanlei on 16-8-16 at 上午9:39

from mrq.task import Task
import urllib2


class Fetch(Task):
    def run(self, params):
        with urllib2.urlopen(params["url"]) as f:
            t = f.read()
            return len(t)
