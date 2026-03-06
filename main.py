from fastapi import FastAPI
app = FastAPI(title="API Алексеевой", version="1.0.0")

@app.get("/")
def home():
    return {"message": "Привет, мир!", "author": "Алексеева"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/about")
def about():
    return {"name": "Алексеева", "project": "Учебный проект FastAPI"}