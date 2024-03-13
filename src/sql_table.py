# !/usr/bin/python3
# coding: utf-8

import pymysql

## 建库和建表
my_connect = pymysql.connect(
    host='localhost',
    user='lixiang',
    passwd='lixiang',
    charset='utf8'
)

cur = my_connect.cursor()

## 开始建库
cur.execute("create database books_table character set utf8;")

## 使用库
cur.execute("use books_table;")

## 建表
cur.execute("create table blogs(id char(20), user_id char(20), name char(20), )character set utf8;")
