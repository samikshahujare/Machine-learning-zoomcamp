import pickle
from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict
import uvicorn

MODEL_PATH = "model.bin"
app = FastAPI(title="Pima Diabetes Risk Prediction")

# Load model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

class Patient(BaseModel):
    # Use ge (greater than or equal) and le (less than or equal) to limit impossible values
    pregnancies: int = Field(..., ge=0, le=20, description="Number of times pregnant")
    glucose: float = Field(..., ge=0, le=300, description="Plasma glucose concentration")
    bloodpressure: float = Field(..., ge=0, le=200, description="Diastolic blood pressure (mm Hg)")
    skinthickness: float = Field(..., ge=0, le=100, description="Triceps skin fold thickness (mm)")
    insulin: float = Field(..., ge=0, le=1000, description="2-Hour serum insulin (mu U/ml)")
    bmi: float = Field(..., ge=0, le=70, description="Body mass index")
    diabetespedigreefunction: float = Field(..., ge=0, le=3, description="Diabetes pedigree function")
    age: int = Field(..., ge=0, le=120, description="Age in years")

    # Sample values for FastAPI /docs (Swagger UI)
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "pregnancies": 2,
                "glucose": 120.5,
                "bloodpressure": 72.0,
                "skinthickness": 35.0,
                "insulin": 0.0,
                "bmi": 33.6,
                "diabetespedigreefunction": 0.627,
                "age": 45
            }
        }
    )

class Prediction(BaseModel):
    diabetes_probability: float
    diabetes: bool

@app.post("/predict", response_model=Prediction)
def predict(patient: Patient):
    # Data is automatically validated by Pydantic before reaching this block
    data = [list(patient.model_dump().values())]
    prob = model.predict_proba(data)[0, 1]

    return Prediction(
        diabetes_probability=round(float(prob), 4),
        diabetes=bool(prob >= 0.5)
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)


# patient.model_dump() -> {'pregnancies': 2, 'glucose': 120.5, ...}
# .values()           -> dict_values([2, 120.5, ...])
# list(...)           -> [2, 120.5, ...]
# [list(...)]         -> [[2, 120.5, ...]] (The 2D array the model expects)

