import sqlite3
conn = sqlite3.connect('FaceNetdb.db')
cursor = conn.execute('SELECT NAME FROM Suspects''')
pro = []
for row in cursor:
    row=list(row)
    pro.append(row)
print(pro)
flat_list = [item for sublist in pro for item in sublist]
print('merged',flat_list)