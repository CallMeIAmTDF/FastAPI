import json

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocket

app = FastAPI()
# connect_user = {}
# products = [
#     {
#         "name": "Iphone",
#         "price": 1000
#     },
#     {
#         "name": "Samsung",
#         "price": 10
#     }
# ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # can alter with time
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#
# @app.websocket("/products/{status}")
# async def add_product(status: str, websocket: WebSocket):
#     await websocket.accept()
#     temp = 1
#     for i in list(connect_user.keys()):
#         if i.startswith(status):
#             temp += 1
#     connect_user[status + str(temp)] = websocket
#     print(connect_user)
#     try:
#         while True:
#             product = await websocket.receive_text()
#             name, price = [product.split(":")[0], product.split(":")[1]]
#             for user, user_ws in connect_user.items():
#                 if user.startswith("get"):
#                     await user_ws.send_text(f"{name}:{price}:{status + str(temp)}")
#     except:
#         del connect_user[status + str(temp)]
#         await websocket.close()


# @app.websocket("/ws/{user_id}")
# async def sendMessage(user_id: str, websocket: WebSocket):
#     await websocket.accept()
#     connect_user[user_id] = websocket
#     try:
#         while True:
#             data = await websocket.receive_text()
#             for user, user_ws in connect_user.items():
#                 if user != user_id:
#                     await user_ws.send_text(data)
#     except:
#         del connect_user[user_id]
#         await websocket.close()
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/getScore/{code}")
async def get_score(code: str):
    url = f"https://diemthi.vnanet.vn/Home/SearchBySobaodanh?code={code}&nam=2024"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=str(exc))
        data = response.json()["result"]
    return data
