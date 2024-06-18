from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os 

app = FastAPI()

@app.get("/")
async def rout_index():
    file_path = os.path.join(os.path.dirname(__file__), "index.html")
    
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return HTMLResponse(content=content)