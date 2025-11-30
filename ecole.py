from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# IMPORTANT: Add CORS middleware BEFORE any routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

class Student(BaseModel):
    id: int
    name: str
    grade: str

students = [
    Student(id=1, name="Alice", grade="A"),
    Student(id=2, name="Bob", grade="B"),
]

@app.get("/students/")
def get_students():
    return students

@app.post("/students/")
def create_student(student: Student):
    students.append(student)
    return student

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for idx, s in enumerate(students):
        if s.id == student_id:
            students[idx] = student
            return student
    return {"error": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for idx, s in enumerate(students):
        if s.id == student_id:
            del students[idx]
            return {"message": "Student deleted"}
    return {"error": "Student not found"}
