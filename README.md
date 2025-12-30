# MemoryBase

Simple single threaded database HTTP Server

SQLite3 `:memory:` database wrapped with Flask

  `/test/client.py` can be used as an example in python

**Requirements:**
```
pip install Flask
pip install requests
```

**Endpoints:**
| METHOD | ENDPOINT | DESCRIPTION | JSON |
| --- | --- | --- | --- |
| `POST` | `/execute` | execute SQL query | `{query str, data list}` |
| `GET` | `/load` | loads database from drive | `NULL` |
| `GET` | `/save` | saves `:memory:` database to drive | `NULL` |
| `GET` | `/tables` | get database tables | `NULL` |
