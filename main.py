from fastapi import FastAPI

app = FastAPI()

@app.post("/input")
async def receive_input(data: str):
    if data == "Hi":
        return {"message": "Hello"}
    else:
        return {"message": "No input"}
