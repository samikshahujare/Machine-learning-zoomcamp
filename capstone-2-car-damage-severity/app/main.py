from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

from app.inference import predict

app = FastAPI(
    title="Car Damage Severity API",
    version="1.0"
)


@app.post("/predict")
async def predict_damage(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    return predict(image)
