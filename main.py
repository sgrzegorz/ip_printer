from fastapi import FastAPI, APIRouter, Request
import uvicorn 


app = FastAPI()

@app.get("/")
def status(request : Request):
    client_host = request.client.host
    with open('file.txt','a+') as file:
        file.write(f'{client_host}\n')
    return {"client_host" : client_host}

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8081)