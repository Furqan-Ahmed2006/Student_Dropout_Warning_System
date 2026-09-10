# Student Dropout Warning System

A machine learning–powered web application designed to identify students who may be at risk of dropping out. The project helps institutions make earlier, data-driven interventions by analyzing student-related factors and providing a warning signal through an easy-to-use Streamlit interface.

## Live Demo

[Try the app here](https://studentdropoutwarningsystem-nzwrgriktyakulxespnpxm.streamlit.app/)

## Overview

Student dropout is a major challenge for educational institutions. This project aims to support early intervention by predicting potential dropout risk using historical and academic indicators. The system is built primarily in Jupyter Notebook for model development and includes a Python-based Streamlit app for deployment.

## Features

- Predicts student dropout risk using a trained machine learning model
- Simple and interactive Streamlit web interface
- Data preprocessing and model evaluation workflow
- Designed to support early warning and intervention efforts
- Easy to extend with additional features or datasets

## Technologies Used

- **Jupyter Notebook** — model training, experimentation, and analysis
- **Python** — application logic and deployment support
- **Streamlit** — web app interface
- **Machine Learning** — prediction and classification workflow

## Project Structure

```text
Student_Dropout_Warning_System/
├── notebooks/
├── app.py
├── requirements.txt
├── README.md
└── ...
```

> Note: The exact structure may vary depending on the files in the repository.

## How It Works

1. The model is trained on student-related data.
2. Relevant features are processed and prepared for prediction.
3. The Streamlit app accepts input values from the user.
4. The model generates a dropout risk prediction.
5. The result is displayed as a warning or risk indicator.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
git clone https://github.com/Furqan-Ahmed2006/Student_Dropout_Warning_System.git
cd Student_Dropout_Warning_System
pip install -r requirements.txt
```

### Run the App Locally

```bash
streamlit run app.py
```

If your main Streamlit file has a different name, replace `app.py` with that file.

## Usage

1. Open the app.
2. Enter the required student details.
3. Click the prediction button.
4. View the dropout warning result.

## Future Improvements

- Add model explainability features
- Improve UI/UX design
- Support larger and more diverse datasets
- Add downloadable prediction reports
- Include confidence scores for predictions

## Contributing

Contributions are welcome. If you'd like to improve the project, feel free to fork the repository and submit a pull request.

## License

Add your preferred license here if one is not already included in the repository.

## Author

**Furqan Ahmed**

---

Built to help educators identify at-risk students earlier and take timely action.