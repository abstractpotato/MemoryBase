from sqlite3 import Error, connect
from atexit import register
from io import StringIO
from traceback import format_exc

class MemoryBase:

    def __init__(self):
        self.connection = connect(":memory:", check_same_thread=False)

    def disk_load(self):
        disk_conn = connect("database/database.db")
        tempfile = StringIO()
        for line in disk_conn.iterdump():
            tempfile.write('%s\n' % line)
        disk_conn.close()
        tempfile.seek(0)
        self.connection = connect(":memory:", check_same_thread=False)
        self.connection.cursor().executescript(tempfile.read())
        self.connection.commit()
        return {"msg": "loaded from disk"}

    def disk_save(self):
        disk_conn = connect("database/blockchain.db")
        self.connection.backup(disk_conn)
        disk_conn.close()
        return {"msg": "saved to disk"}

    def on_close(self):
        print(self.disk_save())
        self.connection.close()

    def execute(self, query):
        try:
            cursor = self.connection.cursor()
            result = cursor.execute(query)
            if "SELECT" not in query and "PRAGMA" not in query:
                self.connection.commit()
                return []
            else:
                return result.fetchall()
        except Error as e:
            return {
                "msg": "query_error",
                "error": str(e),
                # "traceback": str(format_exc())
                }, 500

    def get_tables(self):
        return self.execute("SELECT name FROM sqlite_master WHERE type='table';")

    def command(self, cmd):
        match cmd:
            case "load":
                return self.disk_load()
            case "save":
                return self.disk_save()
            case "tables":
                return self.get_tables()
        return []
