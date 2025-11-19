# 🚰 Water Potability Prediction API

Machine Learning Zoomcamp – Midterm Project

This project predicts whether water is **potable** (safe to drink) or **not potable** using a trained **XGBoost classifier**.

The model is deployed as a **FastAPI** service running inside a **Docker** container, following the recommended ML Zoomcamp deployment workflow.

-----

## 📌 Project Overview

| Component | Detail |
| :--- | :--- |
| **Goal** | Predict if water is potable based on 9 chemical indicators. |
| **Model** | `XGBoostClassifier` (`water.json`) |
| **API** | FastAPI REST endpoint (`/predict`) |
| **Containerization** | Docker |
| **Deployment** | Render Web Service |
| **Input** | JSON with water quality measurements |
| **Output** | Human-readable prediction (“Water is POTABLE / NOT POTABLE”) |

-----

## 📁 Project Structure

```
midterm_deployment/
│
├── app.py               # FastAPI application
├── Dockerfile           # Docker instructions
├── requirements.txt     # Python dependencies
├── water.json           # Trained XGBoost model
└── README.md            # Project documentation
```

-----

## 🔧 Installation (Local)

1.  **Clone repo**
    ```bash
    git clone https://github.com/<your-username>/water-api.git
    cd water-api
    ```
2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run API locally**
    ```bash
    uvicorn app:app --reload
    ```
    Open in browser:
    👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

-----

## 🧪 Example API Usage

**POST** `/predict`

**Sample Input:**

```json
{
  "ph": 7.2,
  "Hardness": 214.0,
  "Solids": 15000.0,
  "Chloramines": 7.5,
  "Sulfate": 300.0,
  "Conductivity": 400.0,
  "Organic_carbon": 10.0,
  "Trihalomethanes": 80.0,
  "Turbidity": 3.5
}
```

**Sample Output:**

```json
{
  "prediction": "Water is POTABLE (SAFE to drink)"
}
```

-----

## 🐳 Run with Docker (Local)

1.  **Build Docker image**
    ```bash
    docker build -t water-api .
    ```
2.  **Run container**
    ```bash
    docker run -p 8000:8000 water-api
    ```
    Visit:
    👉 **http://localhost:8000/docs**

-----

## 🌐 Deployment on Render (Docker)

1.  Create GitHub repo and push these files.
2.  Go to **Render** → “New Web Service.”
3.  Select the repo containing this `Dockerfile`.
4.  Render auto-detects it as a Docker service.
5.  Choose:
      * **Instance:** Free
      * **Region:** Singapore (closest to India)
6.  Click Deploy.

Your live API will appear at:

**https://\<your-render-app\>[.onrender.com/docs](https://www.google.com/search?q=https://.onrender.com/docs)**

-----

## 📊 Model Details

| Detail | Specification |
| :--- | :--- |
| **Algorithm** | `XGBoostClassifier` |
| **Training Split** | 60% train / 20% validation / 20% test |
| **Evaluation** | Accuracy + Human-readable output |
| **Saved As** | `water.json` (XGBoost native format) |

### 🎯 Features Used

| Feature | Description |
| :--- | :--- |
| `ph` | Acidity/alkalinity level |
| `Hardness` | Hardness of water |
| `Solids` | Total dissolved solids |
| `Chloramines` | Water disinfectant chemical |
| `Sulfate` | Sulfate concentration |
| `Conductivity` | Electrical conductivity |
| `Organic_carbon` | Organic carbon content |
| `Trihalomethanes` | Toxic chemical from chlorination |
| `Turbidity` | Water clarity |

-----

## 🏁 Final Notes

Learned a lot and and still a lot to learn :)