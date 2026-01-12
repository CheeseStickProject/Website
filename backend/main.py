from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


import uvicorn

app = FastAPI()


app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
app.mount("/templates", StaticFiles(directory="frontend/templates"), name="templates")

@app.get("/")
def home():
    with open("frontend/templates/index.html") as f:
        return HTMLResponse(f.read())


if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)