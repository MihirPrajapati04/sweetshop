
# 🍬 Sweet Shop Management System

A simple and robust **Sweet Shop Inventory Management System** built using Python, TDD principles, SQLite, and a modern Streamlit-based frontend.

This project was developed as a kata assignment with a strong focus on:
- ✅ Clean code architecture (OOP)
- ✅ Full Test-Driven Development (TDD)
- ✅ Modular, extensible services
- ✅ A user-friendly web interface (Streamlit)

---

## 🛠️ Tech Stack

| Layer         | Tech                |
|---------------|---------------------|
| Language      | Python 3.8+         |
| Database      | SQLite              |
| Backend Logic | Pure Python OOP     |
| Testing       | `unittest` (TDD)    |
| Frontend      | Streamlit           |

---

## 📁 Folder Structure

```

sweetshop/
├── database/
│   └── db.py                  # DBManager class (handles SQLite connection)
├── models/
│   └── sweet.py               # Sweet dataclass model
├── sweetshop/
│   ├── add\_service.py         # Add sweets
│   ├── view\_service.py        # View all sweets
│   ├── search\_service.py      # Name search
│   ├── category\_search\_service.py  # Category search
│   ├── price\_search\_service.py     # Price range search
│   ├── delete\_service.py      # Delete sweet by ID
│   ├── inventory\_service.py   # Purchase / Restock logic
│   └── sweetshop\_app.py       # ✅ Streamlit frontend
├── tests/
│   └── test\_\*.py              # Unit tests for each service
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. 📦 Install Dependencies

```bash
pip install -r requirements.txt
````

### 2. 🚀 Run the App (Frontend)

```bash
streamlit run sweetshop/sweetshop_app.py
```

> This will open your browser with the Sweet Shop UI.

---

## 🧪 Running Tests

This project is built using **pure TDD** — all logic was tested *before* implementation.

To run tests:

```bash
python -m unittest discover tests/
```

---

## 🧰 Features

### ✅ Admin Panel Capabilities

* Add new sweets
* View all inventory
* Search sweets:

  * by name
  * by category
  * by price range
* Purchase sweets (updates quantity)
* Restock sweets
* Delete sweets

### ✅ Inventory Rules

* Raises errors for invalid IDs
* Prevents purchasing when stock is insufficient
* Handles empty result cases gracefully

---

## ✨ Optional Frontend Highlights

* Responsive layout with `st.tabs()`
* Inline success/error messages
* Form-driven UI for each action
* Table views for search and listings
* No HTML or JS needed — all in Python

---

## 🚀 Deployment

Want to deploy for free?

You can deploy this app in minutes on [Streamlit Cloud](https://streamlit.io/cloud):

1. Push this project to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"New app"**
4. Link your GitHub repo and select `sweetshop/sweetshop_app.py` as entry point
5. Done! 🎉

---

## 📌 Notes

* This project follows **Test-Driven Development strictly**:

  * First failing test → then passing logic → then refactor.
* Each service class is modular and testable.
* You can extend this system for:

  * Authentication
  * Graphical reports
  * CSV import/export
  * Multi-user support

---

## 👨‍💻 Author

**Mihir Prajapati**
LDCE, Computer Engineering
Developed for Incubyte Kata Assignment

---

## 📜 License

This project is open-source and free to use for educational and non-commercial purposes.

````

---

## 📎 Also include `requirements.txt`

```txt
streamlit
````

(Add others like `pytest`, etc., if you use them.)

---

Would you like me to also generate:

* A `setup.sh` or `Makefile` to automate setup?
* A Loom/YouTube-ready script if you're recording a demo?
