import requests, json
import time

# ==============================================================================
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = (end_time - start_time) * 1000
        print(f"Function '{func.__name__}' took {round(total_time, 4)} ms.")
        return result
    return wrapper
# ==============================================================================

host = "http://localhost:1430"

@timeit
def execute(query):
    text = requests.post(f'{host}/execute', json={"query": query}).text
    return json.loads(text)

@timeit
def load():
    text = requests.get(f'{host}/load').text
    return json.loads(text)

@timeit
def save():
    text = requests.get(f'{host}/save').text
    return json.loads(text)

@timeit
def tables():
    text = requests.get(f'{host}/tables').text
    return json.loads(text)

@timeit
def table_cols(table_name):
    return execute(f"PRAGMA table_info({table_name})")
