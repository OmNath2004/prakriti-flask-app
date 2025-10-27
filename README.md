

## 🧠 How to Set Up and Run Locally (Windows Guide)

Follow these instructions to run the **Prakriti Self-Assessment Flask App** on your local system.

### 🧩 1. Prerequisites

Before starting, ensure you have:

* **Python 3.8+** installed (run `python --version` to verify)
* **pip** (comes with Python)
* **Command Prompt** or **PowerShell**

Optional but recommended:

* **Visual Studio Code** for easy editing and running.

---

### ⚙️ 2. Clone or Download the Project

You can either:

**Option A – Clone via Git:**

```bash
git clone https://github.com/YOUR_USERNAME/prakriti-flask-app.git
cd prakriti-flask-app
```

**Option B – Manual Setup:**
Create a folder named `prakriti-flask-app` and add these files:

```
app.py
requirements.txt
/templates/questionnaire.html
/static/style.css
```

Paste the provided contents into each file.

---

### 🧱 3. Create a Virtual Environment

In the project folder, run:

```bash
python -m venv venv
```

Then activate it:

**Command Prompt:**

```bash
venv\Scripts\activate
```

**PowerShell (if you get a policy error):**

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\Activate.ps1
```

---

### 📦 4. Install Dependencies

Once the environment is active, install Flask:

```bash
pip install -r requirements.txt
```

If you don’t have the file yet, just run:

```bash
pip install Flask==3.0.3
```

---

### 🚀 5. Run the Flask App

Start the local development server:

```bash
python app.py
```

You’ll see:

```
 * Running on http://127.0.0.1:5000
```

Open your browser and go to 👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

### 🧭 6. Using the App

1. Fill in the **Prakriti Self-Assessment Questionnaire**.
2. Submit the form.
3. View your personalized Ayurvedic report (Vata, Pitta, Kapha).
4. Click **“Print Report”** to save it as a PDF.
5. Click **“Back to Questionnaire”** to retake it.

---

### 🛠️ 7. Troubleshooting

| Problem                                        | Possible Fix                                                                |
| ---------------------------------------------- | --------------------------------------------------------------------------- |
| `ModuleNotFoundError: No module named 'flask'` | Activate the virtual environment and run `pip install flask`                |
| `OSError: [Errno 98] Address already in use`   | Change port in `app.py` → `app.run(debug=True, port=5050)`                  |
| Browser not loading                            | Ensure server is running and URL is correct                                 |
| Template not found                             | Make sure the `templates/` folder name is correct (Flask is case-sensitive) |

---

### 🧰 8. Project Structure

```
prakriti-flask-app/
├── app.py
├── requirements.txt
├── templates/
│   └── questionnaire.html
└── static/
    └── style.css
```

---

### 💡 9. Customization Ideas

* Add “Download Report as PDF” using **ReportLab** or **WeasyPrint**
* Store responses using **SQLite** or **MongoDB**
* Deploy to **Render**, **Vercel**, or **PythonAnywhere**

