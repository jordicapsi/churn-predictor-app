# 🧠 Customer Churn Predictor App (Streamlit Deployment)

🔗 **Live App:** [Try it here](https://jordicapsi-churn-predictor-app-appapp-cwscar.streamlit.app/)

This is a lightweight web app built with **Streamlit** that predicts the probability of a bank customer leaving (churning) based on profile data. The backend uses a **logistic regression model** trained on real-world customer churn data.


---

## 🚀 Quickstart

### 📦 Requirements

Make sure Python 3 is installed, then install the required packages:

```bash
pip install -r requirements.txt
```

### ▶️ Run the app locally

```bash
streamlit run app/app.py
```

Then open the local URL in your browser (usually [http://localhost:8501](http://localhost:8501)).

---

## 📁 Project Structure

```text
churn-app/
├── app/
│   └── app.py               # Streamlit app
├── model.pkl                # Trained logistic regression model
├── scaler.pkl               # Scaler for input features
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 📊 Features Used in Prediction

- Age  
- Balance  
- Estimated Salary  
- Number of Products  
- Tenure  
- Credit Score  
- Is Active Member

---

## 🔮 Output

When values are entered, the app returns:

- **Probability of churn** (e.g., 72%)
- A risk message:
  - ✅ Low Risk of Churn
  - ⚠️ High Risk of Churn

---

## 🧠 Model Overview

- Algorithm: Logistic Regression
- Preprocessing: Feature scaling with `StandardScaler`
- Exported using `joblib`
- Model trained on reduced set of variables for performance and deployment

---

## 🐳 Docker Deployment
This project includes a Docker configuration to allow anyone to run the Streamlit app in a fully reproducible environment — no manual setup required.

### 📦 Build the Docker image
Open a terminal in the root folder and run:

```bash
docker build -t churn-app .
```

This creates a Docker image named churn-app.

### 🚀 Run the container
Start the app with:

```bash
docker run -p 8501:8501 churn-app
```

Then open your browser at:
http://localhost:8501

### ✅ Why use Docker?

- Same behavior across any machine
- No need to install Python or packages
- Mimics production deployment
- Adds technical depth to a data analyst's portfolio

---

## 🙋 Why this project?

This app is part of a portfolio designed to:

- Demonstrate end-to-end ML deployment
- Translate statistical modeling into usable business tools
- Apply mathematical reasoning to feature selection and interpretation

---

## 👨‍💻 Author

**Jordi Capsi**  
_Mathematician & Aspiring Data Analyst_  
🔗 [GitHub Profile](https://github.com/jordicapsi)

---



