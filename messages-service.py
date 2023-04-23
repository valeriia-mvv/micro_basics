from fastapi import FastAPI

app = FastAPI()


@app.get('/lab1')
def get():
    return "It's worked"
