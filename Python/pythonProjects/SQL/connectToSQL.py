import pyodbc as odbc

driverName = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-E81B4RQ'
DATABASE_NAME = "certWebApp"

connectionStr = f"""
    DRIVER={{{driverName}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""


con = odbc.connect(connectionStr)


def read(con):
    print("Read")
    cmd = "SELECT * FROM loginInfo"
    reader = con.cursor()
    reader.execute(cmd)
    for row in reader:
        print(f"\r {row}")

def insert(con):
    print("Insert")
    writer = con.cursor()
    writer.execute("INSERT INTO loginInfo VALUES ('dyl.pickle@cvtechonline.net', 'Password2')")
    con.commit()

def update(con):
    print("Update")
    writer = con.cursor()
    writer.execute("update loginInfo SET pass = 'bomb.com' WHERE pass = 'Password2'")
    con.commit()


#insert(con)

#update(con)

read(con)