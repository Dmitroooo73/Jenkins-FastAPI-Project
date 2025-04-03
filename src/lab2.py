from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"mmm"}


@app.get("/favicon.ico")
async def favicon():
    return {"mm"}


@app.post("/get_summ")
async def summa(first: int, second: int):
    return first + second


@app.post("/get_sub")
async def sub(first: int, second: int):
    return first - second


@app.post("/get_mult")
async def mult(first: int, second: int):
    return first * second


@app.post("/get_div")
async def div(first: int, second: int):
    return first / second

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
