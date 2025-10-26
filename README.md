# CI/CD Pipeline Demo - Task Management API

A Flask-based REST API demonstrating automated CI/CD pipeline implementation with GitHub Actions, pytest, SonarQube, Docker, and Heroku.

## 📋 Project Overview

This project implements a complete CI/CD pipeline that automates:
- Unit testing with pytest
- Code quality analysis with SonarQube
- Containerization with Docker
- Deployment to Heroku
- Discord notifications for build status

## 🚀 Features

- **RESTful API**: Complete CRUD operations for task management
- **Health Monitoring**: Built-in health check endpoint
- **Comprehensive Testing**: Unit tests with >80% coverage
- **Automated Pipeline**: GitHub Actions workflow for CI/CD

## 📁 Project Structure

```
cicd-demo/
├── .github/
│   └── workflows/
│       └── main.yml          # CI/CD pipeline configuration
├── app.py                     # Flask application
├── test_app.py               # Pytest unit tests
├── requirements.txt          # Python dependencies
├── Dockerfile                # Container configuration
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

## 🛠️ Technology Stack

- **Backend**: Flask 3.0.0
- **Testing**: Pytest 7.4.3
- **CI/CD**: GitHub Actions
- **Code Quality**: SonarQube
- **Containerization**: Docker
- **Deployment**: Heroku
- **Notifications**: Discord Webhook

## 📦 Installation

### Prerequisites
- Python 3.9+
- Git
- Docker (optional, for containerization)

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cicd-demo.git
cd cicd-demo
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## 🧪 Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=app --cov-report=html
```

View coverage report:
```bash
open htmlcov/index.html
```

## 📡 API Endpoints

### General Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information and available endpoints |
| GET | `/health` | Health check status |

### Task Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks` | Get all tasks |
| GET | `/api/tasks/<id>` | Get specific task |
| POST | `/api/tasks` | Create new task |
| PUT | `/api/tasks/<id>` | Update task |
| DELETE | `/api/tasks/<id>` | Delete task |

### Example Usage

**Get all tasks:**
```bash
curl http://localhost:5000/api/tasks
```

**Create a task:**
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "New Task", "completed": false}'
```

**Update a task:**
```bash
curl -X PUT http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Task", "completed": true}'
```

**Delete a task:**
```bash
curl -X DELETE http://localhost:5000/api/tasks/1
```

## 🔄 CI/CD Pipeline

The pipeline automatically triggers on every push to the repository:

1. **Checkout Code**: Repository code is checked out
2. **Install Dependencies**: Python packages installed
3. **Run Tests**: Pytest executes all unit tests
4. **Code Quality**: SonarQube analyzes code quality
5. **Build Docker**: Container image created
6. **Deploy**: Application deployed to Heroku
7. **Notify**: Discord receives build status

## 🐳 Docker

Build Docker image:
```bash
docker build -t cicd-demo .
```

Run container:
```bash
docker run -p 5000:5000 cicd-demo
```

## 🚢 Deployment

The application is automatically deployed to Heroku when:
- Tests pass successfully
- Code quality gates are met
- Docker image builds successfully

Production URL: `https://your-app-name.herokuapp.com`

## 📊 Code Quality

Code quality is monitored using SonarQube with the following gates:
- Code coverage > 80%
- No critical or blocker issues
- Maintainability rating A
- Security rating A

## 🔔 Notifications

Discord webhook sends notifications for:
- ✅ Successful builds and deployments
- ❌ Failed tests or quality gates
- 🚀 Deployment status updates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is created for educational purposes as part of a capstone project.

## 👥 Author

Your Name - Capstone Project 2025

## 🙏 Acknowledgments

- Flask documentation
- GitHub Actions documentation
- Docker documentation
- Heroku documentation
- SonarQube community
