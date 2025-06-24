# 🩺 Disease Prediction Web App

A simple yet powerful **Machine Learning + Flask web application** that predicts a user's disease based on selected symptoms. This project demonstrates how ML models can be deployed into real-world applications using Python and Flask.

---

## 🚀 Features

- 🔬 Predicts disease using user-input symptoms
- 🤖 Trained with Decision Tree Classifier on a custom dataset
- 🖥️ Web interface built using Flask & Bootstrap
- ✅ Input validation: accepts only binary values (0 or 1)
- 🎨 Modern and responsive UI with conditional result styling:
  - 🟢 **Healthy** result shown in green
  - 🔴 All other diseases shown in red

---

## 📸 Screenshot

![Screenshot 2025-06-24 153146](https://github.com/user-attachments/assets/07f31ba3-eea4-444f-abea-e0d7f251526b)


---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **scikit-learn**
- **HTML/CSS + Bootstrap**
- **Pickle** (for model serialization)

---

## 📁 Project Structure
├── app.py # Flask backend
├── train_model.py # Model training script
├── disease_model.pkl # Trained ML model
├── dataset.csv # Input dataset
├── templates/
│ └── index.html # Frontend (Flask template)
└── requirements.txt # Python dependencies

---

## ⚙️ Setup Instructions

## ⚙️ Setup Instructions

### 1. Clone the Repository
git clone https://github.com/your-username/disease-prediction-app.git
cd disease-prediction-app

###2. Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

###3. Install Dependencies
pip install -r requirements.txt

###4. Train the Model
python train_model.py

###5. Run the Flask App
python app.py
Visit http://127.0.0.1:5000 to use the app.

📌 Sample Inputs
Symptom	Input (0 or 1)
Fever	1
Fatigue	0
Headache	1

📄 License
This project is open source and available under the MIT License.

🙋‍♀️ Author
Tulsi Datt Saraswat
• 🌐 [LinkedIn](https://www.linkedin.com/in/tulsi-datt-saraswat-57ba74284/) 
• 🐙 [GitHub](https://github.com/TulsiDattSaraswat)

⭐ Show Your Support
If you liked this project, don't forget to ⭐ the repository and share your feedback!











