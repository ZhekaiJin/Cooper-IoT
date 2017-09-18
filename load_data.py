import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='my_db')
cursor = mydb.cursor()

csv_data = csv.reader(file('data_log.csv'))
csv_data.next()
query = 'INSERT INTO sensor_data(Time,\
Light, Temperature, Humidity) VALUES(%s,\
%s,%s,%s)'

for row in csv_data:
    cursor.execute(query,row)

#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"
