from sql_db_conn import *
db = sql_db()
db.sql_conn()
#r =db.db_date()
v = "driver_details_"+ db.db_date()
print(v)

#a = input("enter table to be updated\n")
#b = input("enter column name seperated by comma\n")
#b = b.split()
#c = input("enter values seperated by comma\n")

#db.sql_insert(a,b,c)
sa 	="driver_details_"+ db.db_date()

s 	= input("col\n")
#s = s.split(",")
s1 	=input("col2\n")
#s1 = s1.split(",")
s2	=input("table1\n")
s3  =input("table2\n")
d 	=input('Enter common columns')
d 	=d.split(',')
s4	=d[0]
s5	=d[1]
db.sql_create_table(sa,s,s1,s2,s3,s4,s5)



