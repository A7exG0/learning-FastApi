from fastapi import FastAPI
import os 
import json 

app = FastAPI()

@app.post("/calculate")
async def sum():
    # Получаем путь к файлу с числами 
    file_path = os.path.join(os.path.dirname(__file__), "numbers.json")

    # Получаем числа из файла
    with open(file_path, "r", encoding="utf-8") as file:
        numbers = json.load(file)

    # Получаем сумму двух чисел
    return {"result": int(numbers['num1']) + int(numbers['num2'])}