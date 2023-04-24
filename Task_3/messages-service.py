from fastapi import FastAPI

app = FastAPI()


@app.get('/lab3')
def get():
    return  "It's worked"
