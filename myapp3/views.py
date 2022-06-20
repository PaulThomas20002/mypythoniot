# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unicodedata import name

from django.shortcuts import render
import mysql.connector
con=mysql.connector.connect(host = "localhost",
user = "root",
password = "",
database="dbname"
)
c=con.cursor()


# Create your views here.
def registration(request):
    c.execute("select * from registration")
    result = c.fetchall();
    print(result)
    if request.POST:
        name=request.POST["t1"]
        age=request.POST["t2"]
        dob=request.POST["t3"]
        mail=request.POST["t4"]
        phone=request.POST["t5"]
        c.execute("insert into registration values(%s,%s,%s,%s,%s)",[name,age,dob,mail,phone])
        con.commit()
    c.execute("select * from registration")
    result = c.fetchall();
    return render(request,"index.html",{"res":result})
    con.close()