from fastapi import FastAPI
from sample.apis import sample

app = FastAPI()
app.include_router(sample.router)
