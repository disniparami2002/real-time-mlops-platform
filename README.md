# 🚀 Real-Time AI Prediction Platform with Automated MLOps Pipeline

## 📌 Project Overview

This project implements a production-grade Real-Time AI Prediction Platform for customer churn prediction using modern MLOps practices.

The system supports:

- ✅ Real-time predictions
- ✅ Automated retraining
- ✅ MLflow experiment tracking
- ✅ Data drift monitoring
- ✅ Docker containerization
- ✅ CI/CD automation
- ✅ Cloud deployment
- ✅ Monitoring dashboard

This project simulates how enterprise AI systems are built, deployed, monitored, and continuously improved in real-world environments.

---

# 🏗️ System Architecture

![Architecture Diagram](images/architecture.png)

---

# ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Scikit-Learn | Machine Learning |
| FastAPI | Real-Time Prediction API |
| MLflow | Experiment Tracking |
| Docker | Containerization |
| GitHub Actions | CI/CD Automation |
| Streamlit | Monitoring Dashboard |
| Apache Airflow | Automated Retraining |

---

# 📂 Project Structure

```bash
real-time-mlops-platform/
│
├── .github/workflows/
│   └── ci.yml
│
├── airflow/dags/
│   └── retrain_pipeline.py
│
├── api/
│   └── app.py
│
├── dashboard/
│   └── dashboard.py
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── images/
│   ├── architecture.png
│   ├── swagger_ui.png
│   ├── mlflow_dashboard.png
│   ├── streamlit_dashboard.png
│   ├── github_actions.png
│   └── prediction_result.png
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── train.py
│   └── drift_monitor.py
│
├── docs/
│   ├── technical_documentation.md
│   └── Final_Project_Report.pdf
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🤖 Machine Learning Pipeline

The ML pipeline includes:

1. Data ingestion
2. Data preprocessing
3. Model training
4. Model evaluation
5. MLflow experiment tracking
6. Model serialization
7. API deployment
8. Drift monitoring
9. Automated retraining

---

# ⚡ FastAPI Prediction API

## API Endpoint

```bash
POST /predict
```

## Run FastAPI Server

```bash
uvicorn api.app:app --reload
```

## Swagger Documentation

```bash
http://127.0.0.1:8000/docs
```

---

# 📊 MLflow Experiment Tracking

MLflow was integrated for:

- Accuracy tracking
- Parameter logging
- Artifact storage
- Experiment comparison

## Run MLflow UI

```bash
mlflow ui --workers 1
```

## Open MLflow Dashboard

```bash
http://127.0.0.1:5000
```

---

# 📈 Data Drift Monitoring

The system compares incoming data with training data to detect drift.

Implemented using:

- Statistical comparison
- Mean difference analysis
- Monitoring dashboard alerts

## Drift Monitoring File

```bash
src/drift_monitor.py
```

---

# 🔄 Automated Retraining Pipeline

Apache Airflow DAG automates:

- Model retraining
- Scheduled execution
- Training workflow orchestration

## Pipeline File

```bash
airflow/dags/retrain_pipeline.py
```

---

# 🐳 Docker Containerization

Docker was used to containerize the FastAPI application for portable deployment.

## Build Docker Image

```bash
docker build -t churn-api .
```

## Run Docker Container

```bash
docker run -p 8000:8000 churn-api
```

---

# 🔁 CI/CD Pipeline

GitHub Actions automates:

- Build validation
- Dependency installation
- CI workflow execution

## Workflow File

```bash
.github/workflows/ci.yml
```

---

# ☁️ Live Cloud Deployment

The monitoring dashboard was deployed using Streamlit Cloud for public access and live monitoring.

## 🔗 Live Dashboard URL

https://real-time-mlops-platform-eeywujbeavtjvqb69sfwrd.streamlit.app/

---

# 📊 Monitoring Dashboard Features

The Streamlit dashboard provides:

- System monitoring
- Drift monitoring
- Dataset visualization
- MLflow status
- Model statistics
- Real-time monitoring metrics

---

# 📸 Project Screenshots

## Swagger API Testing

![Swagger UI](images/swagger_ui.png)

---

## MLflow Experiment Tracking

![MLflow Dashboard](images/mlflow_dashboard.png)

---

## Streamlit Monitoring Dashboard

![Streamlit Dashboard](images/streamlit_dashboard.png)

---

## GitHub Actions CI/CD

![GitHub Actions](images/github_actions.png)

---

## Prediction Output

![Prediction Result](images/prediction_result.png)

---

# 🧪 Testing & Validation

System testing included:

- Swagger API testing
- Browser testing
- Real-time prediction validation
- Dashboard verification

---

# 🚧 Challenges Faced

- Airflow compatibility issues on Windows
- MLflow configuration issues
- Dependency conflicts
- Cloud deployment limitations
- Docker environment setup

---

# 🔮 Future Improvements

Future enhancements may include:

- Kubernetes deployment
- Real-time streaming pipelines
- Advanced drift detection
- Model rollback system
- User authentication
- Database integration

---

# 👨‍💻 Author

Disni Parami

## GitHub Profile

https://github.com/disniparami2002

---

# ⭐ Conclusion

This project demonstrates a complete end-to-end enterprise-style MLOps workflow including:

- Real-time AI predictions
- Automated retraining
- Drift monitoring
- Experiment tracking
- Cloud deployment
- CI/CD automation

The platform simulates modern production AI system architecture and lifecycle management.