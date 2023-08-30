import pymysql


def connect():
    conn = pymysql.connect(
        port=3306,
        host="83.220.175.75",
        user="edwica_root",
        password="b00m5gQ40WB1",
        database="edwica"
    )
    return conn

