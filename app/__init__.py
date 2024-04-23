import uvicorn

if __name__ == '__main__':
    uvicorn.run("app.main:app", reload=True, reload_dirs='D:/fastapidima', port=8000, host="127.0.0.1")