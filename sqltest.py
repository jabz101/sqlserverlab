import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TESTSQLCLUSTER;'
                      'Database=AdventureWorks2016;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()


#cursor.execute('SELECT * FROM AdventureWorks2016.HumanResources.Department where DepartmentID = 17')
#for row in cursor:
#    print(row)

cursor.execute('''
                INSERT INTO AdventureWorks2016.HumanResources.Department (Name, GroupName, ModifiedDate)
                VALUES ('Ninja' ,'Clan', '2021-01-15 00:00:00:000')
                ''')
conn.commit()

#cursor.execute('''
#                 DELETE FROM AdventureWorks2016.HumanResources.Department
#                 WHERE [Name] in ('Ninja', 'Ninja2')
#                 ''')
#conn.commit()

cursor.execute('SELECT * FROM AdventureWorks2016.HumanResources.Department')
for row in cursor:
    print(row)

conn.close()
