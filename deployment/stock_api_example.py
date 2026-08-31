from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Stock Forecast Demo")

class StockRequest(BaseModel):
    price: float
    momentum: float = 0.0

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict_stock(req: StockRequest):
    # Simple heuristic example only; replace with trained model logic in production.
    forecast = req.price * (1 + req.momentum * 0.05)
    return {
        "input_price": req.price,
        "momentum": req.momentum,
        "forecast_price": round(forecast, 4)
    }

# Run with: uvicorn deployment.stock_api_example:app --reload
