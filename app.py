from flask import Flask, request
from atexit import register
from modules.memorybase import MemoryBase

import endpoints.main as main
import endpoints.execute as execute

app = Flask(__name__)
app.debug = False
app.database = MemoryBase()
app.database.disk_load()

register(app.database.on_close)

main.run(app)
execute.run(app, request)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1430)
