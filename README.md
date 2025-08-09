# FastAPI Assignment with Docker

## 📌 Overview
This project is a simple **FastAPI** application created as part of an assignment.  
It includes:
- A **GET endpoint** returning a welcome message.
- A **POST endpoint** that receives a task name and returns it with the current date and time.
- **Swagger UI** for interactive API testing.
- **Docker containerization** for running the app in an isolated environment.

---

## 🛠️ Technologies Used
- Python 3.11
- FastAPI
- Uvicorn
- Docker

---

## 📂 Project Structure
FASTAPI-Task/
│
├── main.py # FastAPI app with GET and POST routes
├── requirements.txt # Project dependencies
├── Dockerfile # Docker configuration
└── README.md # Project documentation

---

## 🚀 How to Run Locally (Without Docker)

1. **Clone the repository**
   ```bash
   git clone https://github.com/aimanmohsin2621/FASTAPI-Task.git
   cd FASTAPI-Task
2.Install dependencies
bash
pip install -r requirements.txt
3.Run the application
bash
uvicorn main:app --reload
4.Open Swagger UI

Go to: http://127.0.0.1:8000/docs

🐳 Running with Docker
1.Build the Docker image
bash
docker build -t fastapi-task .
2.Run the container
bash
docker run -d -p 8000:8000 fastapi-task
3.Access the app
Swagger UI: http://localhost:8000/docs
📜 API Endpoints
GET /
Returns a welcome message.

json
{
  "message": "Hello from FastAPI!"
}
POST /create-task
Accepts a JSON body with a task_name and returns the task name, date, and time.

Request:
json
{
  "task_name": "My First Task"
}
Response:
json
{
  "task_name": "My First Task",
  "date": "2025-08-09",
  "time": "14:35:21"
}