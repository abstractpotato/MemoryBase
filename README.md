# MemoryBase

Simple single threaded database for small projects

SQLite3 `:memory:` database wrapped with Flask

**Requirements:**
```
pip install Flask
```

**Endpoints:**
| METHOD | ENDPOINT | DESCRIPTION | JSON |
| --- | --- | --- | --- |
| `POST` | `/execute` | execute query | `{query str, data list}` |
| `GET` | `/load` | loads database from drive | `[]` |
| `GET` | `/save` | saves `:memory:` database to drive | `[]` |
| `GET` | `/tables` | get database tables | `[]` |
