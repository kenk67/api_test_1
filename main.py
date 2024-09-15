from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    data: str

@app.post("/input")
async def receive_input(data: InputData):
    if data.data == "Hi":
        return {"message": "Hello"}
    elif data.data == "What":
        return {"message": "What is it ?"}
    else:
        return {"message": "Noo input"}

#something else
#print
# Remove hosts
# Removed hosts reload
#testing commandline

@app.get("/testing")
async def hello():
    return {"message": "BG3"}