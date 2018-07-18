#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import pymysql
from pyquery import PyQuery
from time import ctime,sleep
import requests
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def getData(shopId,area,cityName,firstName,description):
    print shopId,area,cityName,firstName,description
    db = pymysql.connect(host="localhost", user="root",
                         password="xxxxx", db="yaya", port=3306)

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    sql_insert = 'insert into shopInfo (shopId,area,cityName,firstName,description) values("%d","%s","%s","%s","%s")' % (shopId,area,cityName,firstName,description)
    print sql_insert
    try:
        cur.execute(sql_insert)
        # 提交
        db.commit()
    except Exception as e:
        # 错误回滚
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':

    for num in range(14533, 14600):
       r = requests.get('XXX', {'custom': num})
       html = r.json()
       result = html['result']
       getData (result['shopId'], result['area'], result['cityName'],result['firstName'],result['description'])