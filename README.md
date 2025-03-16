# 🚀 Credit Card Fraud Detection using Machine Learning  

![Python](https://img.shields.io/badge/Python-3.8-blue) ![Flask](https://img.shields.io/badge/Flask-API-orange) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-RandomForest-green)

## 📌 Overview  
This project is a **Credit Card Fraud Detection system** that uses **Machine Learning** to detect fraudulent transactions.  
The model is trained on an **imbalanced dataset** using **Random Forest** and **SMOTE** to improve accuracy.  

---

## 📂 Dataset  
- The dataset used is from **Kaggle's Credit Card Fraud Detection**.  
- **Download Link**: [Click Here](https://www.kaggle.com/mlg-ulb/creditcardfraud)  
- The dataset contains **284,807 transactions**, out of which **492 are fraudulent**.  

---

## ⚙️ Technologies Used  
| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Programming Language |
| **Flask** | API Development |
| **Scikit-Learn** | Machine Learning Models |
| **SMOTE** | Handling Imbalanced Data |
| **Matplotlib & Seaborn** | Data Visualization |
| **Render** | Cloud Deployment |

---

## 🎯 Features  
✅ Handles **imbalanced fraud data** using **SMOTE**  
✅ Uses **Random Forest** for high accuracy  
✅ **REST API** for real-time fraud detection  
✅ Can be deployed on **Render / AWS / Railway**  

---

## 🚀 How to Run Locally  
Follow these steps to run the project on your system.  

### **🔹 Step 1: Clone Repository**  
```bash
git clone https://github.com/Kkamble21/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection
```

### **🔹 Step 2: Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **🔹 Step 3: Run Flask API**  
```bash
python app.py
```

### **🔹 Step 4: Test API**  
You can send a **POST request** to test fraud detection:  
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features": [0.1, -2.1, 1.5, ..., 0.3]}'
```

---

## 🌐 API Endpoints  
| Method | Endpoint | Description |  
|--------|---------|-------------|  
| **POST** | `/predict` | Predicts if a transaction is **Fraudulent** or **Legitimate** |  

---

## 📡 Deployment on Render  
### **Follow these steps to deploy the project on Render:**  
1️⃣ **Sign up on** [Render](https://render.com/)  
2️⃣ **Create a New Web Service**  
3️⃣ **Connect GitHub Repo**  
4️⃣ **Set Start Command:**  
```bash
pip install flask joblib
python app.py
```
5️⃣ **Deploy and Get Public API URL** 🎉  

---

## 📜 License  
This project is **open-source** and available under the **MIT License**.  

---

## 🤝 Contributing  
Contributions are always welcome! 🎯  

1️⃣ Fork the repository  
2️⃣ Create a new branch (`feature-branch`)  
3️⃣ Commit changes and push to GitHub  
4️⃣ Open a Pull Request  

---

## 📬 Contact  
👤 **Kshitij Dhanaji Kamble**  
📧 Email: `your-email@example.com`  
🔗 GitHub: [Kkamble21](https://github.com/Kkamble21)  
