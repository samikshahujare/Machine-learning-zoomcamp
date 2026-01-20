```markdown
# Car Damage Severity Prediction (ML Zoomcamp Capstone)

This project predicts the **severity of car damage from images** and classifies it into one of three categories:
- **Minor**
- **Moderate**
- **Severe**

It is developed as **Capstone Project 2** for the **Machine Learning Zoomcamp** and deployed as a **production-ready machine learning API**.

---

## 📌 Problem Statement

Vehicle damage assessment for insurance claims is often:
- Manual
- Time-consuming
- Subjective

The objective of this project is to **automate car damage severity classification** using a deep learning model and expose it through a **REST API** that can be integrated into real-world applications such as insurance claim systems and vehicle inspection tools.

---

## 📊 Dataset

- **Source:** Kaggle – Car Damage Severity Dataset  
- **Classes:** Minor, Moderate, Severe  
- **Input:** RGB images of damaged cars  

The dataset is organized into class-wise directories and used for supervised image classification.

---

## 🧠 Model

- **Architecture:** Convolutional Neural Network (CNN)
- **Framework:** TensorFlow
- **Optimization:** Exported to **TensorFlow Lite (TFLite)** for lightweight and fast inference

### Training Environment
- Model training and experimentation were performed using **Kaggle Notebooks**
- Python 3.10 with TensorFlow support
- The trained `.tflite` model is used directly for inference in production

> **Note:**  
> Model training is not re-run locally due to TensorFlow version compatibility.  
> The exported TFLite model is used for deployment and inference.

---

## ⚙️ Tech Stack

- Python
- TensorFlow Lite
- FastAPI
- Docker
- Render (Cloud Deployment)

---

## 🚀 API Service

The trained model is served using **FastAPI** and provides an endpoint for image-based prediction.

### Endpoint
```

POST /predict

````

### Input
- Image file (`.jpg` or `.png`)

### Output (Example)
```json
{
  "predicted_class": "moderate",
  "confidence": 0.87
}
````

---

## 🐳 Run Locally Using Docker

### Build the Docker image

```bash
docker build -t car-damage-service .
```

### Run the container

```bash
docker run -p 8080:8080 car-damage-service
```

### Open API documentation

```
http://localhost:8080/docs
```

The Swagger UI can be used to test the prediction endpoint.

---

## 🌍 Live Deployment

The application is deployed on **Render** using Docker.

### 🔗 Live API URL

```
https://car-damage-severity-api.onrender.com/docs
```

This endpoint provides:

* Public access
* Interactive Swagger documentation
* Live inference

---

## 📁 Project Structure

```
capstone-2-car-damage-severity/
├── app/
│   ├── main.py
│   ├── inference.py
│   └── labels.py
├── model/
│   └── car_damage_model.tflite
├── Dockerfile
├── pyproject.toml
├── uv.lock
├── README.md
└── car-damage-severity-prediction.ipynb
```

---

## ✅ Project Status

* Model trained and evaluated
* TFLite model exported
* FastAPI inference service implemented
* Dockerized application
* Successfully deployed on Render
* Public API endpoint available

This project fully satisfies the requirements for the **Machine Learning Zoomcamp Capstone**.

---

## 📌 How to Use (Quick)

1. Open the live link:

   ```
   https://car-damage-severity-api.onrender.com/docs
   ```
2. Select **POST /predict**
3. Upload a car damage image
4. Execute the request
5. View the predicted severity and confidence score

---

## 🏁 Conclusion

This project demonstrates an **end-to-end machine learning workflow**, including:

* Problem definition
* Model training and optimization
* API development
* Containerization with Docker
* Cloud deployment

The solution is **reproducible, scalable, and production-ready**, making it suitable for real-world deployment and evaluation.

````



