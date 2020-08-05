import uvicorn

from application import demo_app

if __name__ == "__main__":
    uvicorn.run(demo_app, host="0.0.0.0", port=6022)
