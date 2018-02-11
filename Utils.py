def startConnection(database):
    server = 'skynetcapital.database.windows.net'
    username = 'amhardy94'
    password = 'Skynetcapital2017'
    driver = '{ODBC Driver 13 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER=' + driver + ';PORT=1433;SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    print "TEST"
    return cnxn
def closeConnection(conn):
  conn.close()
