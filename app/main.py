from fastapi import FastAPI, HTTPException, Query
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.fib import fibonacci

app = FastAPI(title="Fibonacci API")

@app.get("/fib")
def get_fibonacci(
    n: int = Query(..., description="1 以上の整数")
):
    try:
        result = fibonacci(n)
        return {"result": result}
    except ValueError as exc:
        # 1) JSON の形、2) HTTP ステータス 400 を保証
        raise HTTPException(status_code=400, detail=str(exc))

@app.exception_handler(HTTPException)
async def custom_handler(_, exc):
    """PDF 指定どおりのエラーボディを統一して返す。"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": exc.status_code, "message": exc.detail},
    )

@app.exception_handler(RequestValidationError)
async def validation_error_handler(_, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"status": 400, "message": "Bad request."},
    )