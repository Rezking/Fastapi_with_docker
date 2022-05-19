from fastapi import FastAPI
import uvicorn

app = FastAPI()
print('hi')
@app.get('/')
def hello():
    text = {'text':'hello world'}
    return text

@app.get('/item/{item_id}')
def retrieve(item_id):
    item= {item_id:'This is just me trying to work with Docker'}
    return item

