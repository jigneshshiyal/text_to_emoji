from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer

import faiss
import numpy as np
import pandas as pd
import pickle
import os
from pathlib import Path

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static directory for HTML/JS/CSS
STATIC_DIR = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Define data and model paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
CSV_PATH = DATA_DIR / "process_emojis_no_duplicates.csv"
PKL_PATH = DATA_DIR / "text_embeddings.pkl"

# Global variables
df = None
model = None
index = None

def load_data_and_embeddings():
    global df, model, index

    # Load dataset
    df = pd.read_csv(CSV_PATH)

    # Load sentence transformer model
    model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

    # Load or compute embeddings
    if PKL_PATH.exists():
        with open(PKL_PATH, "rb") as f:
            text_embeddings = pickle.load(f)
        print("✅ Loaded precomputed embeddings.")
    else:
        print("⚙️ Generating new embeddings...")
        text_embeddings = model.encode(df["text_name"], convert_to_numpy=True, show_progress_bar=True)
        text_embeddings = text_embeddings / np.linalg.norm(text_embeddings, axis=1, keepdims=True)
        with open(PKL_PATH, "wb") as f:
            pickle.dump(text_embeddings, f)
        print("✅ Embeddings saved.")

    # Initialize FAISS index
    d = text_embeddings.shape[1]
    index = faiss.IndexFlatIP(d)
    index.add(text_embeddings)

# Load data/model/index at startup
load_data_and_embeddings()

def find_closest_match(query: str) -> str:
    query_embedding = model.encode([query], convert_to_numpy=True)
    query_embedding /= np.linalg.norm(query_embedding, axis=1, keepdims=True)
    _, indices = index.search(query_embedding, 1)
    return df.iloc[indices[0][0]]["emoji"]

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_path = STATIC_DIR / "index.html"
    if html_path.exists():
        return HTMLResponse(content=html_path.read_text(), status_code=200)
    return HTMLResponse(content="<h1>index.html not found</h1>", status_code=404)

@app.get("/find_emoji")
def get_emoji(query: str = Query(..., description="Input text to find relevant emoji")):
    words = query.strip().split()
    emojis = [find_closest_match(word) for word in words]
    return {"query": query, "emojis": " ".join(emojis)}
