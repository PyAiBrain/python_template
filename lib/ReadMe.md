# 🛠 Starter-Paket für Python-Projekte

## 📌 Features
✅ **Modulares Projekt mit konfigurierbarem `config.json`**  
✅ **Erweiterter Argumentparser mit `add_arg()`**  
✅ **Logging mit Farben & Datei-Logging**  
✅ **Datei- und Ordneroperationen**  
✅ **Custom-Zeitformat-Parser**  
✅ **Einfache Installation & Nutzung**  

---

## 📂 **Projektstruktur**
```
my_project/
│── config/
│   ├── config.json    # Konfigurationsdatei
│   ├── loader.py      # Konfigurationsmanager
│── core/
│   ├── logger.py      # Logging-System
│   ├── parser.py      # Zeitformat-Parser
│── utils/
│   ├── file_ops.py    # Datei- und Ordneroperationen
│── cli/
│   ├── arguments.py   # CLI-Argumente mit `add_arg()`
│── main.py            # Einstiegspunkt
│── requirements.txt   # Abhängigkeiten
│── .env               # Umgebungsvariablen
│── README.md          # Dokumentation
```

---

## 🚀 **Installation**
### 1️⃣ **Virtuelle Umgebung erstellen**
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2️⃣ **Abhängigkeiten installieren**
```
pip install -r requirements.txt
```

### 3️⃣ **Projekt starten**
```
python main.py --debug
```

---

## 🔧 **Beispiele**
### 🟢 **Logging**
```
python main.py --debug
```

### 🟢 **Datei schreiben**
```
python main.py --file example.txt --text "Hallo Welt"
```

### 🟢 **Datei lesen**
```
python main.py --file example.txt
```

---

## ⚙ **Erweiterung**
1️⃣ **Neue Argumente mit `add_arg()` hinzufügen**  
2️⃣ **Konfiguration in `config.json` anpassen**  
3️⃣ **Eigene Module in `core/` oder `utils/` hinzufügen**  

---

## 📜 **Lizenz**
MIT License © 2025
