import pymssql
import DataFile

def Pint_line():
    print("------------------------------------------------")

def print_data ():
    serverName = 'DESKTOP-VNAOJGN'
    userName = 'samwel'
    passWord = '0000'
    conn = pymssql.connect(serverName, userName, passWord, "webdb" , autocommit=True)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM job')
    row = cursor.fetchone()
    Pint_line()
    while row:
        print("Job Title \t : {}\nCompany Name : {}\nLocation\t : {}\nsince\t     : {}\nType\t     : {} " .format(row[1], row[2] , row[3] ,row[4] , row[5] ))
        Pint_line()
        row = cursor.fetchone()
    conn.close()

def insert_all ():
    serverName = 'DESKTOP-VNAOJGN'
    userName = 'samwel'
    passWord = '0000'
    conn = pymssql.connect(serverName, userName, passWord, "webdb" , autocommit=True)
    cursor = conn.cursor()
    for i in range(len(DataFile.Titles)):
         cursor.execute(
             "INSERT INTO job  VALUES ('{Title}', '{Companys}', '{Locations}' , '{Sinces}' , '{type}' )".format(Title=DataFile.Titles[i] , Companys=DataFile.Companys[i] , Locations=DataFile.Locations[i] ,  Sinces=DataFile.Sinces[i] , type=DataFile.Type[i])
              )
    conn.close()


def Delete_all () :
    serverName = 'DESKTOP-VNAOJGN'
    userName = 'samwel'
    passWord = '0000'
    conn = pymssql.connect(serverName, userName, passWord, "webdb", autocommit=True)
    cursor = conn.cursor()
    cursor.execute(
        "delete from job")
    conn.close()
