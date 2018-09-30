import pymysql

con = pymysql.connect('localhost:8889',
    'root',
    'root', 
    'python',
    unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock"
)

cursor = con.cursor()
sql = """
    create table data(
        id int(11) auto_increment primary key,
        fname varchar(200)not null,
        lname varchar(200)not null,
        mname varchar(200)not null
    )

    """
cursor.execute(sql)
con.commit()
con.close()
