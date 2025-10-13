# Blood Pressure Analyzer 🩺

Machine learning application to classify blood pressure stage and suggest medication, based on user inputs (age, weight, gender, lifestyle, etc.).

---

## Table of Contents

- [Motivation](#motivation)  
- [Features](#features)  
- [Project Structure](#project-structure)  
- [Data](#data)  
- [Model & Training](#model--training)  
- [Usage](#usage)  
- [Requirements](#requirements)  
- [Running Locally](#running-locally)  
- [Possible Improvements & Future Work](#possible-improvements--future-work)  
- [License](#license)  

---

## Motivation

High blood pressure (hypertension) is a major health risk globally. Early classification and intervention are crucial to prevent complications. This tool provides a lightweight interface to estimate a user’s blood pressure class and suggest possible medication support.

---

## Features

- GUI form to accept user inputs (age, gender, weight, etc.)  
- Predicts blood pressure **stage / class**  
- Suggests medications (or classes of medications)  
- Uses a trained, serialized model for inference  
- Sample datasets included for training/testing  

---

## Project Structure

```

/
├── .vscode/
├── Blood Pressure Model.py
├── FinalData.csv
├── checkup.csv
├── model_pickle/
├── reg_form_UI.py
├── requirements.txt
└── Screenshot (562).png

````

Here’s what each piece does:

| File / Folder | Description |
|----------------------|-----------------------------------------------------------|
| `.vscode/` | VSCode workspace or settings files |
| `Blood Pressure Model.py` | Script to preprocess data, train model, evaluate, and save model |
| `FinalData.csv` | Processed / cleaned dataset used for training |
| `checkup.csv` | Raw or supplementary data for preprocessing or testing |
| `model_pickle/` | Directory storing serialized model files (pickle) |
| `reg_form_UI.py` | GUI front-end that captures user input and makes predictions |
| `requirements.txt` | List of Python dependencies |
| `Screenshot (562).png` | Example screenshot of the UI / output |

---

## Data

- **FinalData.csv**: the cleaned and feature‑engineered data used for training / validation  
- **checkup.csv**: raw / additional data source (before cleaning)  

You should document in code or a separate notebook how you handled missing values, encoding categorical features, normalization/scaling, feature selection, etc.

---

## Model & Training

- The **Blood Pressure Model.py** script handles:  
  1. Loading datasets  
  2. Preprocessing (scaling, encoding, splitting into train/test)  
  3. Training a classification model to map user inputs → BP category & medication suggestion  
  4. Evaluating performance (accuracy, confusion matrix, possibly cross‑validation)  
  5. Serializing the trained model into `model_pickle/`

- The UI (`reg_form_UI.py`) loads the pickled model and uses it for inference on new data.

If you have performance metrics (accuracy, precision, recall, ROC curves), include them here.

---

## Usage

1. Launch the UI:  
```bash
   python reg_form_UI.py
````

2. Fill in the form fields (age, gender, weight, etc.)
3. Submit → the app outputs:

   * Predicted **blood pressure stage / class**
   * Suggested **medication(s) / classes**

Include the screenshot (`Screenshot (562).png`) in the README so users see what the UI looks like.

---

## Requirements

Dependencies are listed in `requirements.txt`. Example:

```
numpy
pandas
scikit-learn
tkinter
```

To install:

```bash
pip install -r requirements.txt
```

---

## Running Locally

1. Clone the repository

```bash
   git clone https://github.com/Mehmaam99/Blood-Pressure-Analyzer.git
   cd Blood-Pressure-Analyzer
```
2. (Optional) Create & activate a virtual environment

```bash
   python -m venv venv
   source venv/bin/activate   # (Linux/macOS)
   venv\Scripts\activate      # (Windows)
```
3. Install dependencies

```bash
   pip install -r requirements.txt
```
4. (Optional) Retrain the model

```bash
   python "Blood Pressure Model.py"
```
5. Run the GUI

```bash
   python reg_form_UI.py
```

---

## Possible Improvements & Future Work

* **Input validation** in the GUI (e.g. numeric-only, bounds checking)
* **Error handling** (model not found, invalid inputs)
* More robust **preprocessing pipeline** (e.g. pipelines in `sklearn`)
* **Hyperparameter tuning** and cross-validation
* **Model interpretability** (feature importance, SHAP values)
* Adding **unit tests** and integration tests
* Deploy as a **web app** (Flask, Django, Streamlit)
* Expand to accept **continuous or real-time data** (e.g. from wearables)
* Add logging / audit trail for predictions

---

## License

You should decide and add a license (e.g. MIT, Apache 2.0). Also create a `LICENSE` file in the root.

---

## Acknowledgments

* The Python / ML ecosystem (pandas, scikit-learn, etc.)
* Any tutorials, sample projects, or research papers that inspired parts of this work
