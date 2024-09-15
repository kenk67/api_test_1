from fastapi import FastAPI

app = FastAPI()

@app.post("/input")
async def receive_input(data: str):
    if data == "Hi":
        return {"message": "Hello"}
    elif data == "What":
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