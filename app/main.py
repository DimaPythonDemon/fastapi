from fastapi import FastAPI
my_ip = "192.168.33.98"
app = FastAPI()


@app.get("/")
def root():
    return ''
