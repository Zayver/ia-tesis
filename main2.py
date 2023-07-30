from fastapi import FastAPI, Query
from contextlib import asynccontextmanager
import time
import py_eureka_client.eureka_client as eureka_client
from dataclasses import dataclass

@dataclass
class Model:
    number: int
    number2: int
    number3: int

app = FastAPI(description="Modelo 2 de prueba para el eureka server", title="Modelo 2")



@app.get("/predict", description = "Hace un predit de un MODEL DE IA")
def model_test(number: int = Query(title="Numero x", description="Numero para hacer ciertas cosas", example=5)) -> float:
    time.sleep(1)
    return number/3

@app.get("/train")
def nose() -> int:
    time.sleep(2)
    return 2

@app.get("/complex")
def test() -> Model:
    return Model(1, 2 , 3)



def get_server_info():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
    print(s.getsockname())

if __name__ == "__main__":
    ip = get_server_info()
    eureka_client.init(eureka_server="http://localhost:8761",
                app_name="model2-service",
                instance_port=8001,
                metadata={"MICROSERVICE-TYPE": "MODEL"},
                instance_host=ip
    )
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8001)
    
