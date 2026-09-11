# 🎓 Student Dropout Early Warning System

An end-to-end Machine Learning web application designed to predict student attrition early, enabling educational institutions to intervene proactively and improve retention rates.

---

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR_LIVE_APP_URL)

👉 https://studentdropoutwarningsystem-nzwrgriktyakulxespnpxm.streamlit.app/

---

## 📌 Project Overview

Student retention is a key success metric for academic institutions. This project leverages historical student performance, demographic details, and behavioral metrics to train predictive models that flag high-risk students early in the academic lifecycle.

### Key Features
* **Early Risk Identification:** Predicts whether a student is likely to drop out or graduate based on current academic indicators.
* **Interactive UI:** Built using Streamlit for seamless data input and instant risk evaluation.
* **Automated Uptime Pipeline:** Integrated Playwright CI/CD automation via GitHub Actions to maintain 24/7 live app status.

---

## 🛠️ Tech Stack & Tools

* **Programming Language:** Python 3.10
* **Machine Learning & Analytics:** Scikit-Learn, Pandas, NumPy
* **Web Framework:** Streamlit
* **CI/CD & Automation:** GitHub Actions, Playwright

---

## 📁 Repository Structure

```text
├── .github/workflows/   # Automated CI/CD pipeline (Keep-alive workflow)
├── Data_cleaning.ipynb  # Exploratory Data Analysis & Preprocessing
├── app.py               # Streamlit Dashboard UI & inference script
├── keep_alive.py        # Playwright ping script for 24/7 uptime
├── model.pkl            # Trained Classification Model
├── scaler.pkl           # Feature Scaling Artifact
├── requirements.txt     # Environment dependencies
└── README.md            # Project Documentation
