# AI Dropout Prediction System

A machine learning-powered web application designed to predict the likelihood of student dropout based on key academic and personal indicators.

## 📌 Overview

This project utilizes a pre-trained Machine Learning model to assess the risk of a student dropping out. It analyzes factors such as **Attendance**, **GPA**, and **Financial Stress** to provide a probability score and personalized recommendations.

The system consists of:
- **Backend**: A Flask API that handles data processing and serves predictions.
- **Frontend**: An interactive Streamlit dashboard for easy user interaction.

## 🛠️ specific Tech Stack

- **Python** (Core Logic)
- **Flask** (API Backend)
- **Streamlit** (User Interface)
- **Scikit-learn** (Machine Learning Model)
- **Pandas & NumPy** (Data Processing)

## 🚀 Getting Started

### Prerequisites
Ensure you have Python installed. You can check by running:
```bash
python --version
```

### Installation

1. Clone the repository (or navigate to the project directory):
   ```bash
   cd path/to/project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ usage

To run the application, you need to start both the backend server and the frontend interface.

### 1. Start the Flask Backend
Open a terminal and run:
```bash
python app.py
```
*The API will start running at `http://127.0.0.1:5000`*

### 2. Launch the Streamlit Frontend
Open a **new** terminal window and run:
```bash
streamlit run frontend.py
```
*The application should automatically open in your browser at `http://localhost:8501`*

## 🔮 How it Works
1. Enter the student's **Attendance %** (slider).
2. Input the current **GPA**.
3. Rate the **Financial Stress** level (1-10).
4. Click **Predict**.
5. View the **Dropout Probability**, **Risk Level**, and actionable **Recommendations**.

## 📂 Project Structure
- `app.py`: Flask application serving the ML model.
- `frontend.py`: Streamlit User Interface.
- `model_training.py`: Script used to train the model (if applicable).
- `dropout_model.pkl`: Serialized pre-trained ML model.
- `requirements.txt`: Python dependencies.
