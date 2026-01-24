# 🌿 Agro Doctor: AI Agriculture Ecosystem

Agro Doctor is a premium, full-stack digital ecosystem designed to transform Indian agriculture. It combines deep-learning computer vision for disease diagnosis with a direct-to-farm marketplace and AI-driven expert guidance.

---

## ⚡ Quick Start (Run Locally)

To get the entire ecosystem running, you need to start three services in separate terminal windows:

### 1. AI Inference Service (Python/FastAPI)
The brain of the system, responsible for neural network inference on crop images.
```bash
cd ai_service
# If venv is already created:
source venv/bin/activate
python main.py
```
*Runs on: `http://localhost:8000`*

### 2. Backend API (Node.js/Express)
Manages the marketplace, product inventory, and user data.
```bash
cd backend
npm install  # (First time only)
node server.js
```
*Runs on: `http://localhost:5000`*

### 3. Frontend Web App (Next.js 15)
The premium, interactive user interface.
```bash
cd agro-doctor-app/frontend
npm install  # (First time only)
npm run dev
```
*Runs on: `http://localhost:3000`*

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
