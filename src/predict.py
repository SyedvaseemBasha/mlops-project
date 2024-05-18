from fastapi import FastAPI, Request
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load('models/house_price_model.pkl')

@app.post('/predict')
async def predict(request: Request):
    data = await request.json()
    df = pd.DataFrame(data)
    predictions = model.predict(df)
    return {"predictions": predictions.tolist()}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
