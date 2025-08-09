# Court Data Fetcher – Internship Task 1

A Flask-based web application that demonstrates the workflow of fetching and displaying Indian court case details based on user input.  
The system is built with a modular design so it can be easily connected to live data sources or official court portals.

---

## 📌 Features
- Clean HTML form for entering *Case Type, **Case Number, and **Filing Year*
- Backend processing using *Python Flask*
- Displays:
  - Parties involved
  - Filing date
  - Next hearing date
  - Order/judgment PDF link
- All search requests are stored in a *SQLite database*
- Error handling for invalid or incomplete inputs

---

## 🛠 Tech Stack
- *Backend:* Python, Flask  
- *Frontend:* HTML (Bootstrap)  
- *Database:* SQLite  
- *Parsing Framework Ready:* BeautifulSoup (for integrating with live sources)

---

## ⚙ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/court_data_app.git
cd court_data_app
pip install -r requirements.txt
python app.py
http://127.0.0.1:5000