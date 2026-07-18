# 🌿 Agro Doctor: AI Agriculture Ecosystem

Agro Doctor is a premium, full-stack digital ecosystem designed to transform Indian agriculture. It combines deep-learning computer vision for disease diagnosis with a direct-to-farm marketplace and AI-driven expert guidance.

---

## ⚡ Quick Start (Run Locally)

To get the entire ecosystem running (both the Next.js frontend and the FastAPI Python backend), execute the single startup runner script at the root directory:

### 🍎 For macOS & Linux:
```bash
python3 run.py
```

### 🪟 For Windows:
```cmd
python run.py
```

*Or alternatively, run using npm:*
```bash
npm start
```

This single command automatically performs the following:
- Creates a virtual environment in `backend/venv` (if missing).
- Installs all backend Python packages from `backend/requirements.txt`.
- Installs all frontend node packages in `frontend/` (if missing).
- Clears existing processes on ports 3000 and 8000.
- Launches the Next.js App (`http://localhost:3000`) and the FastAPI backend (`http://localhost:8000`) concurrently.

---

## 🔐 Login Credentials (Demo)
The platform is protected with banking-grade security. Use the following credentials to access the full dashboard:
- **Username**: `admin`
- **Password**: `agro123`

---

## 🔥 Key Features

### 📸 AI Crop Diagnosis
- **Neural Scan**: Instantly identify plant diseases with high-confidence inference.
- **Spectrum Analysis**: Visual "Bio-Spectral" scanner UI.
- **Certified PDF Reports**: Download official diagnosis reports with Root Cause & Organic/Chemical Cures.

### � Premium Marketplace
- **Direct-to-Farm**: Buy certified high-yield seeds and organic fertilizers.
- **Amazon-Style UX**: Rich product images and integrated shopping cart.
- **Automatic Invoicing**: Generate professional PDF bills with Estimated Delivery and **Usage Instructions** for every item.

### 🤖 AI Chat Assistant
- **Expert Guidance**: 24/7 AI-powered assistant for farming queries.
- **Localized Advice**: Context-aware suggestions for soil and pest management.

---

## 🛠 Tech Stack
- **Frontend**: Next.js 15, Tailwind CSS, Framer Motion, Lucide Icons, html2canvas, jsPDF.
- **Backend**: Node.js, Express.
- **AI Service**: Python, FastAPI, TensorFlow/Keras.

---

## � Contributing
Developed with ❤️ by the Agro Doctor Team to empower the backbone of our nation.




run code in terminal 

py run.py