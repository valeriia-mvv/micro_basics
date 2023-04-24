import random
import uuid
import requests
from models import FacadePostMessage
from fastapi import FastAPI

MESSAGES_SERVICE = 'http://127.0.0.1:8004/lab3'

LOGGING_SERVICE = ('http://127.0.0.1:8001/lab3','http://127.0.0.1:8002/lab3','http://127.0.0.1:8003/lab3')


def get_host():
    return random.choice(LOGGING_SERVICE)


app = FastAPI()


@app.get('/facade_service/')
def get():
    message_response = requests.get(MESSAGES_SERVICE)
    logging_response_text = requests.get(get_host())
    return logging_response_text.text.strip('"') + ': ' + message_response.text.strip('"')


@app.post("/facade_service/", status_code=200)
def post(msg: FacadePostMessage):
    requests.post(url=get_host(), json={'uuid': str(uuid.uuid4()), 'msg': msg.msg})
    
