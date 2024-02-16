from fastapi import FastAPI

app = FastAPI()

students = {}

@app.post("/students/")
def create_student(student_id: int, name: str, age: int, sex: str, height: float):
    student = {"id": student_id, "name": name, "age": age, "sex": sex, "height": height}
    students[student_id] = student
    return student

@app.get("/students/{student_id}")
def read_student(student_id: int):
    return students[student_id]

@app.get("/students/")
def read_students():
    return students

@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int, sex: str, height: float):
    student = {"id": student_id, "name": name, "age": age, "sex": sex, "height": height}
    students[student_id] = student
    return student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return students.pop(student_id)
