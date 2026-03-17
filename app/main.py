from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"status": "online"}


@app.get("/health")
def health():
    return {"status": "ok"}
