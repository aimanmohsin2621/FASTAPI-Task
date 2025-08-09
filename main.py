from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}

# ✅ Define the data model
class Task(BaseModel):
    task_name: str

# ✅ Use the model in the POST endpoint
@app.post("/create-task")
async def create_task(task: Task):
    now = datetime.now()
    return {
        "task_name": task.task_name,
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S")
    }