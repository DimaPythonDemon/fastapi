from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

my_ip = "192.168.33.98"
app = FastAPI()


def get_html(name: str):
    path = "templates/html/" + name + ".html"
    html = open(path, "r").read()
    return html


@app.get("/")
def root():
    return HTMLResponse(get_html("start"))
