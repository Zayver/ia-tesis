from fastapi import FastAPI 
from contextlib import asynccontextmanager
import time
import py_eureka_client.eureka_client as eureka_client
from dataclasses import dataclass

@dataclass
class Model:
    number: int
    description: str
    percent: float


app = FastAPI()



@app.get("/predict")
def model_test(number: int) -> int:
    time.sleep(1)
    return number+5

@app.get("/train")
def nose() -> str:
    time.sleep(2)
    return "train"

@app.get("/complex")
def test() -> Model:
    return Model(number=5, description="Esto es una descripcion", percent=0.7)


def get_server_info():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
    print(s.getsockname())

if __name__ == "__main__":
    ip = get_server_info()
    eureka_client.init(eureka_server="http://localhost:8761",
                app_name="model1-service",
                instance_port=8000,
                metadata={"MICROSERVICE-TYPE": "MODEL"},
                instance_host=ip
    )
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
    
