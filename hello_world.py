from fastapi import FastAPI

app = FastAPI()

@app.get("/") # декоратор
async def root():
    return {"message": "Hello world!"}