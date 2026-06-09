# 🏠 PropCast Agent
### AI-Powered Real Estate Forecasting Platform
**Microsoft Agents League Hackathon 2026 — Creative Apps / GitHub Copilot Track**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-5.2-green?style=flat-square&logo=django)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.8-orange?style=flat-square&logo=scikit-learn)
![Groq](https://img.shields.io/badge/Groq-LLaMA3-yellow?style=flat-square)
![GitHub Copilot](https://img.shields.io/badge/Built%20with-GitHub%20Copilot-black?style=flat-square&logo=github)

---

## 🚀 What is PropCast Agent?

PropCast Agent is an AI-powered real estate forecasting web application that helps buyers, sellers, and investors make smarter property decisions in the Hyderabad market. It combines **Machine Learning price prediction (92% accuracy)**, **interactive data visualisation**, and **Groq LLaMA-powered AI insights** — all in one platform.

Built entirely using **GitHub Copilot** as an AI development partner throughout the entire development process.

---

## 🧠 The Problem It Solves

The Indian real estate market — especially Hyderabad — is booming. But:

- Property prices are **unpredictable and scattered** across platforms
- Buyers rely on **agent guesswork** instead of data
- There is **no easy tool** to analyse market trends without expertise
- First-time buyers and investors **miss opportunities** due to lack of insights

**PropCast Agent fixes this** by giving anyone — technical or not — a data-driven platform to understand, predict, and act on real estate market trends.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📤 CSV Upload | Upload any Hyderabad property dataset |
| 📊 Market Statistics | Instant descriptive analytics — avg price, price/sqft, distributions |
| 📈 Interactive Charts | Plotly-powered charts — price trends, area comparisons, BHK analysis |
| 🤖 ML Price Predictor | Random Forest model with **92% accuracy** |
| 💬 AI Chat Assistant | Ask anything about the market — powered by Groq LLaMA 3 |
| 🧾 AI Summary & Insights | Auto-generated market insights from your dataset |
| 🔍 Property Comparison | Side-by-side comparison view with Plotly charts |
| 📄 PDF Export | Download a full report — charts, predictions, insights |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.2 |
| ML Model | Scikit-learn (Random Forest Regressor) |
| Data Processing | Pandas, NumPy |
| Charts | Plotly |
| AI / LLM | Groq API (LLaMA 3) |
| PDF Export | ReportLab |
| Database | SQLite |
| AI Dev Tool | GitHub Copilot (VS Code) |

---

## 📁 Project Structure

```
PropCast-Agent/
│
├── PropCast/               # Django app — views, models, URLs
├── core/                   # Core settings and configuration
├── templates/              # HTML templates
│   ├── compare.html        # Property comparison view
│   └── properties_list.html
├── media/                  # Uploaded CSV files (auto-created, gitignored)
├── sample_properties.csv   # Sample Hyderabad dataset to get started
├── create_sample.py        # Script to generate sample data
├── manage.py               # Django entry point
├── requirements.txt        # All Python dependencies
├── Dockerfile              # Docker configuration
├── COMPARISON_FEATURE_GUIDE.md
└── PropCast_Complete_Guide.pdf
```

---

## ⚙️ How to Run Locally

### Prerequisites

Make sure you have the following installed on your system:

- **Python 3.10 or above** → [Download here](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** → [Download here](https://git-scm.com/)
- A **Groq API key** (free) → [Get one here](https://console.groq.com/)

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/rahulachari/PropCast-Agent.git
cd PropCast-Agent
```

---

### Step 2 — Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal — that means it's active.

---

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

This installs everything — Django, Pandas, Scikit-learn, Plotly, Groq, ReportLab, and all other required packages.

---

### Step 4 — Set Up Environment Variables

Create a `.env` file in the root folder:

```bash
# Windows
echo. > .env

# Mac / Linux
touch .env
```

Open the `.env` file and add:

```
GROQ_API_KEY=your_groq_api_key_here
SECRET_KEY=your_django_secret_key_here
DEBUG=True
```

> 🔑 Get your free Groq API key at [console.groq.com](https://console.groq.com/)
> 
> 🔐 For Django SECRET_KEY, you can generate one by running:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

---

### Step 5 — Run Database Migrations

```bash
python manage.py migrate
```

---

### Step 6 — Start the Server

```bash
python manage.py runserver
```

Open your browser and go to:
```
http://127.0.0.1:8000
```

🎉 PropCast Agent is now running locally!

---

## 📂 Sample Dataset

A sample Hyderabad property dataset is included in the repo — `sample_properties.csv`.

Use this to test the app immediately after setup:
1. Open the app in your browser
2. Upload `sample_properties.csv`
3. Explore stats, charts, predictions, and AI insights

You can also generate a fresh sample dataset by running:
```bash
python create_sample.py
```

---

## 🤖 GitHub Copilot — The AI Development Partner

This entire project was built using **GitHub Copilot** in VS Code as an AI-assisted development tool. Copilot helped with:

- Writing Django views and URL routing
- Building optimised Pandas data pipelines
- Completing Scikit-learn ML pipeline code
- Generating Plotly chart configurations
- Debugging and refactoring throughout development

> GitHub Copilot didn't just autocomplete — it accelerated the entire development workflow, making it possible to build a full-stack AI platform within the hackathon timeline.

---

## 📊 ML Model Details

- **Algorithm:** Random Forest Regressor
- **Library:** Scikit-learn 1.8
- **Accuracy:** 92%
- **Features used:** Area (sq ft), Location, BHK, Property Type, Amenities
- **Data:** Hyderabad real estate dataset (cleaned with Pandas)

---

## 🔑 Required API Keys

| Service | Purpose | How to Get |
|---|---|---|
| Groq API | AI chat, summaries, insights | [console.groq.com](https://console.groq.com/) — Free tier available |

---

## 🐳 Run with Docker (Optional)

If you prefer Docker:

```bash
docker build -t propcast-agent .
docker run -p 8000:8000 propcast-agent
```

Then open `http://localhost:8000`

---

## 👤 About the Developer

**Rahul Achari**
B.Tech CSE Graduate — The Apollo University, Chittoor, Andhra Pradesh

- 🐙 GitHub: [github.com/rahulachari](https://github.com/rahulachari)
- 🌐 Portfolio: [rahulachari.github.io](https://rahulachari.github.io)

---

## 🏆 Hackathon

Built for the **Microsoft Agents League Hackathon 2026**
Track: 🎨 Creative Apps / GitHub Copilot
Submission Deadline: June 14, 2026

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
