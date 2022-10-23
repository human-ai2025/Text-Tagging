import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/msg")
def index():
    return { "message": "Up and running"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)