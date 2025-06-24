# 😃 Emoji Finder App

An interactive app that suggests relevant emojis based on the text you type!  
Powered by **FastAPI**, **Sentence Transformers**, **FAISS**, and a sleek **Streamlit** frontend.

---

## 🔧 Features

- 🔍 Suggests emojis for every word in your input
- 💬 Live emoji prediction as you type
- 🚀 Fast inference using FAISS and SentenceTransformer embeddings
- 🌐 REST API backend with FastAPI
- 🧑‍💻 User-friendly frontend with Streamlit

---

## 📁 Folder Structure

emoji-finder-app/
├── backend/
│ ├── app.py # FastAPI backend
│ ├── data/
│ │ ├── process_emojis_no_duplicates.csv
│ │ └── text_embeddings.pkl # Auto-generated on first run
│ └── static/ # Optional (index.html if using browser frontend)
│
├── frontend/
│ └── streamlit_app.py # Streamlit frontend
│
├── requirements.txt # Backend dependencies
├── frontend_requirements.txt # Frontend dependencies
└── README.md # This file


---

## 📦 Installation

### 🔙 Backend Setup (FastAPI)

1. **Navigate to backend folder**:
    ```bash
    cd backend
    ```

2. **Install dependencies**:
    ```bash
    pip install -r ../requirements.txt
    ```

3. **Run FastAPI server**:
    ```bash
    uvicorn app:app --reload
    ```

- The backend will run on `http://localhost:8000`

---

### 🎨 Frontend Setup (Streamlit)

1. **Open a new terminal** and navigate to frontend:
    ```bash
    cd frontend
    ```

2. **Install Streamlit dependencies**:
    ```bash
    pip install -r ../frontend_requirements.txt
    ```

3. **Run the app**:
    ```bash
    streamlit run streamlit_app.py
    ```

- The app will open in your browser (usually at `http://localhost:8501`)

---

## 🧠 How It Works

- `process_emojis_no_duplicates.csv` contains text and associated emoji.
- Embeddings are generated using `all-mpnet-base-v2` (from Sentence Transformers).
- FAISS is used to find the most semantically similar word in the dataset.
- As you type in the Streamlit app, it queries the FastAPI backend for the best emoji matches.

---

## ✅ Requirements

### Backend
- Python 3.8+
- fastapi
- uvicorn
- sentence-transformers
- faiss-cpu
- pandas, numpy

### Frontend
- streamlit
- requests

---

## 🛠️ TODO (Optional Enhancements)

- [ ] Add descriptions or tooltips for each emoji
- [ ] Support sentence-level emoji prediction
- [ ] Deploy backend (e.g., Render or Railway)
- [ ] Deploy frontend (e.g., Streamlit Community Cloud)

---

## 📸 Demo

_You can add a GIF or screenshot here showing the app in action._

---

## 📃 License

MIT License — free to use, modify, and distribute.

---

## 🤝 Contributing

Contributions are welcome! Please open issues or pull requests.

