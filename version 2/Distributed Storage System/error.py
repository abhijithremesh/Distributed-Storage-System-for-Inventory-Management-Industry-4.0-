import mysql.connector
import sys
import numpy 

articlenum = sys.argv[1]

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Peace@123",
  database="distributedstorage"
)
cursor = db.cursor()
sql = "SELECT unit_weight FROM inventorydb WHERE article_number="+articlenum;
# sql = "SELECT unit_weight FROM inventorydb WHERE article_number='708763'";

cursor.execute(sql)
unitWeight= cursor.fetchall()
uweight = unitWeight[0]
u = uweight[0]
arr = []

for i in range(1,101):
    for j in numpy.arange(-0.4,0.5,0.1):
        j = round(j,2)
        a = i*u + j
        a = round(a,2)
        arr.append(a)

print(arr)












