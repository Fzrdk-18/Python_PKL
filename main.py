from http.client import IM_USED
from tkinter.messagebox import NO
from fastapi import FastAPI, Request, Response
from ListenMsg import ListenMsg
import uvicorn
from koneksi import koneksi1 as koneksi
from pydantic import BaseModel
import requests
import json

app = FastAPI()

    
@app.get('/hello')
@app.post('/hello')
async def hello_world():
    return 'hello world'


@app.post('/template')
async def template (request: Request):
    try:
        request_json_data = await request.json()
    except Exception as ex:
        print('format bukan json')
        return 'FORMAT BUKAN JSON'

    print(request_json_data)
    request_json_data['Request']='OK'

    print(request_json_data)
    response_json_data = {
        "Nomor Transaksi": "0001",
        "Nama User": "Budi",
        "Nama Barang": "Indomie Goreng",
        "Quantitas Barang": "2",
        "Harga Satuan": "3450",
        "Total Harga": "6900"
    }

    return response_json_data
class hit(BaseModel):
    payload = { "nokontrak" : "4630100086" }
 

@app.post('/open-api/{path}')
async def mapping_api(path: str, request: Request, baseParam:hit):
    
    conn = koneksi.buka_koneksi2()
    cursor = conn.cursor()
    cursor.execute("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE")
    print(conn)
    if conn is None:
        return 'KONEKSI DB PROBLEM'

    try:
        request_json_data = await request.json()
    except Exception as ex:
        print('format bukan json')
        return 'FORMAT BUKAN JSON'

    ls_method = path

    listenMsg = ListenMsg(conn)

    response_listen = await listenMsg.handler(ls_method, request_json_data)

    koneksi.tutup_koneksi(conn)
    return response_listen
if __name__ == "__main__":
    ls_data = ""
    uvicorn.run("main:app", reload=True, debug=True)

