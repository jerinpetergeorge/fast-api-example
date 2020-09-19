import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "application:app",  # or import app instance here
        host="0.0.0.0",
        port=6022,
        reload=True,
        debug=True
    )
