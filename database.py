# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:50:14 2018
@author: Firdauz_Fanani
"""

import pymysql.cursors
import time
import datetime
import Main

# Connect to the database
def data(insertdata):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='alpr',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)


    try:
        with connection.cursor() as cursor:
            # Create a new record
            ceksql= "SELECT COUNT(plat_no) AS cekplat FROM `track_plat` WHERE plat_no=%s AND DATE(`waktu_datang`) = DATE(CURDATE())"
            cursor.execute(ceksql, (insertdata))
            checking = cursor.fetchone()
            print(checking)
            if checking.get('cekplat')<1:
                sql = "INSERT INTO `track_plat`(`plat_no`) SELECT text_plat FROM plat_nomor WHERE plat_nomor.text_plat=%s"
                cursor.execute(sql, (insertdata))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
        return True

    finally:
        connection.close()

def updatetime(insertdata):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='alpr',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)


    try:
        with connection.cursor() as cursor:
            # Create a new record
            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            ceksql= "UPDATE `track_plat` SET waktu_pergi=%s WHERE plat_no=%s"
            cursor.execute(ceksql, (timestamp,insertdata))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
        return True

    finally:
        connection.close()

def check(insertdata):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='alpr',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        # Create a new record
        ceksql= "SELECT COUNT(plat_no) AS cekplat FROM `track_plat` WHERE plat_no=%s AND DATE(`waktu_datang`) = DATE(CURDATE())"
        cursor.execute(ceksql, (insertdata))
        checking = cursor.fetchone()
        print(checking)
        if checking.get('cekplat')==1:
            return True
