from fastapi import FastAPI
import main as pmp
app = FastAPI()

@app.get("/")
def read_root():
    a = pmp.func()
    return {"message": "Hello, {a}!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.post("/create/")
def create_item(data: dict):
    return {"message": "Item created", "data": data}