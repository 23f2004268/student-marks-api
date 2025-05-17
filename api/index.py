from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

with open('q-vercel-python.json') as f:
    students_data = json.load(f)

@app.get("/api")
async def get_marks(name: List[str] = Query(None)):
    if not name:
        return {"error": "Please provide at least one name"}
    
    marks = []
    for student_name in name:
        mark = next((student["marks"] for student in students_data 
                     if student["name"].lower() == student_name.lower()), None)
        marks.append(mark)
    return {"marks": marks}

@app.get("/")
async def root():
    return {"message": "Use /api?name=Name to get marks"}
