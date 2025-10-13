# 🩸 Blood Pressure Analyzer

A machine learning project that predicts a person’s **blood pressure stage** and gives **medication suggestions** based on user inputs such as age, gender, and weight.

---

## 🔍 Project Overview

This project is built using **Python** and **Machine Learning**.  
It has a **simple form-based interface** that takes user details and predicts:

- Blood Pressure Stage (Normal, Stage 1, or Stage 2)
- Recommended Medication

The goal is to make basic **health prediction** automated using ML.

---

## 🧠 How It Works

The project has three main parts:

1. **Frontend (Form UI)**  
   File: `reg_form_UI.py`  
   - Collects user input (like age, gender, weight)  
   - Sends data to the ML model for prediction  

2. **Backend / Model Logic**  
   File: `Blood Pressure Model.py`  
   - Loads the trained machine learning model (`model_pickle`)  
   - Processes input and predicts the BP stage and medication  

3. **Dataset**  
   Files: `FinalData.csv` and `checkup.csv`  
   - Contain real or sample data used to train and test the model  

---

## ⚙️ How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/Mehmaam99/Blood-Pressure-Analyzer.git
cd Blood-Pressure-Analyzer
