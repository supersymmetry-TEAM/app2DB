import sqlite3
import ast

with open('/home/ubuntu/dataSet/NUTDATA.txt', 'r') as f:
    mylist = ast.literal_eval(f.read())
print(sqlite3)
conn = sqlite3.connect("/home/ubuntu/venv/app2DB/db.sqlite3")
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

ap ='INSERT INTO nutfood_nutdata VALUES'
bp = ''
ep = ''
cp =' ON CONFLICT ("NUM") DO NOTHING'

for j in range(len(mylist)): #len(mylist)
    for i in range(1000):

        ak = (ast.literal_eval(mylist[j][i]))
        bp = list(ak)
        for k in range(len(bp)):
            if type(bp[k]) == int:
                continue
            a=bp[k].replace("'",'')
            a=a.replace("'",'')
            bp[k]=a
        bp.append(0)
        bp = str(tuple(bp))
        c.execute(ap+bp)
        print(bp)
        print(str(j)+"~~~~~~~~~~~"+str(i))


conn.commit()
conn.close()
