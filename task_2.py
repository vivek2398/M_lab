import MySQLdb
import intercom

def connection():
    conn = MySQLdb.connect(host="some_server.net",
                           user="root",
                           passwd="blasduhasdbiiu",
                           db = "sql9167459")
    c = conn.cursor()

    return c, conn

def insert_users():
    c, conn = connection()
    c.execute("SELECT * FROM user")
    content = c.fetchone()

    while content is not None:
        intercom.user.create(user_id=content[0], name=content[1], email=content[2])
        content = fetchone()
