from models import Message
from fastapi import FastAPI

app = FastAPI()
hash_table = dict()

@app.post('/lab1', status_code=200)
def post(message: Message):
    hash_table[message.uuid] = message.msg
    print(message)


@app.get('/lab1')
def get():
    return '[{}]'.format(', '.join(hash_table.values()))
