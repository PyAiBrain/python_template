# 🛠 Starter Package for Python Projects

## 📌 Features
- ✅ **Modular project with configurable `config.json`**  
- ✅ **Extended argument parser with `add_arg()`**  
- ✅ **Logging with colors & file logging**  
- ✅ **File and folder operations**  
- ✅ **Custom time format parser**  
- ✅ **Easy installation & usage**  

---

## 📂 **Project Structure**
===

my_project/
│── config/
│   ├── config.json    # Configuration file
│   ├── loader.py      # Configuration manager
│── core/
│   ├── logger.py      # Logging system
│   ├── parser.py      # Time format parser
│── utils/
│   ├── file_ops.py    # File and folder operations
│── cli/
│   ├── arguments.py   # CLI arguments with `add_arg()`
│── main.py            # Entry point
│── requirements.txt   # Dependencies
│── .env               # Environment variables
│── README.md          # Documentation
===

---

## 🚀 **Installation**
### 1️⃣ **Create a Virtual Environment**
===

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
===

### 2️⃣ **Install Dependencies**
===

pip install -r requirements.txt
===

### 3️⃣ **Start the Project**
===

python main.py --debug
===

---

## 🔧 **Examples**
### 🟢 **Logging**
===

python main.py --debug
===

### 🟢 **Write to a File**
===

python main.py --file example.txt --text "Hello World"
===

### 🟢 **Read from a File**
===

python main.py --file example.txt
===

---

## ⚙ **Extension**
1️⃣ **Add new arguments with `add_arg()`**  
2️⃣ **Adjust configuration in `config.json`**  
3️⃣ **Add your own modules in `core/` or `utils/`**  

---

## 📜 **License**
MIT License © 2025
