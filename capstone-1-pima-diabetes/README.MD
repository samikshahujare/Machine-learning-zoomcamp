# Pima Indians Diabetes Risk Prediction  
### ML Zoomcamp – Capstone Project 1

This project implements an **end-to-end machine learning system** to predict the **probability of diabetes risk** using clinical health indicators.

The focus is on **production-grade ML engineering**, including:
- reproducible training
- model selection
- API-based inference
- Docker containerization
- cloud deployment on Render

---

## 🚀 Live Demo (Deployed on Render)

- **API Docs (Swagger UI):**  
  https://pima-diabetes-capstone.onrender.com/docs

Use the `/predict` endpoint to test predictions directly from the browser.

---

## 🧠 Problem Description

Early screening for diabetes helps prioritize preventive care and medical attention.  
Given routine, non-invasive health measurements, the goal is to estimate the **probability of diabetes**.

⚠️ This system is intended for **educational and screening purposes only** and **must not be used for medical diagnosis**.

---

## 📊 Dataset

**Pima Indians Diabetes Dataset**

- Rows: 768  
- Features: 8 numerical medical attributes  
- Target: `Outcome`  
  - `0` → Non-diabetic  
  - `1` → Diabetic  

### Features used for inference
- Pregnancies  
- Glucose  
- BloodPressure  
- SkinThickness  
- Insulin  
- BMI  
- DiabetesPedigreeFunction  
- Age  

---

## 🔍 Exploratory Data Analysis (EDA)

EDA was performed to:
- inspect feature distributions
- analyze class imbalance
- identify zero-valued medical measurements
- examine feature correlations

The analysis revealed weak linear relationships and moderate class imbalance, motivating the use of **tree-based ensemble models**.

---

## 🤖 Modeling Approach

A **Pareto-optimal strategy** was used (few strong models instead of many weak ones).

### Models trained
1. Logistic Regression (baseline, interpretable)  
2. Random Forest (non-linear baseline)  
3. Gradient Boosting / XGBoost (high-performance ensemble)

### Evaluation Metric
- **ROC-AUC**

The best-performing model is automatically selected and saved as a single artifact:

model.bin


---

## 📁 Project Structure



capstone-1-pima-diabetes/
├── data/
│ └── pima_data.csv
├── notebooks/
│ └── Pima_Indians_Dataset_Capstone_1.ipynb
├── train.py
├── predict.py
├── test.py
├── model.bin
├── pyproject.toml
├── uv.lock
├── Dockerfile
└── README.md


This structure ensures **clarity, reproducibility, and deployability**.

---

## ⚙️ Environment & Dependencies

Dependency management is handled using **uv** for deterministic and locked environments.

### System Requirements
- Python ≥ 3.10  
- Git  
- Docker (for deployment)

---

## 🛠️ Setup Instructions (Local)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/samikshahujare/Machine-learning-zoomcamp.git
cd Machine-learning-zoomcamp/capstone-1-pima-diabetes

2️⃣ Install uv
pip install uv


Verify:

python -m uv --version

3️⃣ Install dependencies
python -m uv sync


This installs all dependencies from uv.lock.

🏋️ Model Training
python -m uv run python train.py


This will:

train multiple models

evaluate using ROC-AUC

select the best model

save it as model.bin

🌐 Run the API Locally
Start FastAPI server
python -m uv run uvicorn predict:app --host 0.0.0.0 --port 9696

Available endpoints

POST /predict

Interactive API docs at:

http://localhost:9696/docs

Test the API
python -m uv run python test.py

🐳 Docker Usage
Build Docker image
docker build -t pima-diabetes .

Run container
docker run -p 9696:9696 pima-diabetes


Then open:

http://localhost:9696/docs

☁️ Deployment on Render (Docker)
Steps

Go to Render → New → Web Service

Connect GitHub repository

Choose Docker as environment

Set Root Directory:

capstone-1-pima-diabetes


Set Port:

9696

Deploy

Render builds the Docker image and exposes a public API.
