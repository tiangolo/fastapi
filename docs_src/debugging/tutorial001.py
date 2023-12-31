from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}
