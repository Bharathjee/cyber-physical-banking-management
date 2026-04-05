# Cyber Physical Banking Management System

[![Docker](https://img.shields.io/badge/Docker-%2300aced?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Bharathjee/cyber-physical-banking-management)

## 🚀 Features

- **Admin Panel**: Create customer accounts (ID + Password)
- **Customer Portal**: View balance, deposit, withdraw
- **Role-Based Auth**: Separate admin/customer dashboards  
- **Dockerized**: Production-ready deployment
- **Responsive UI**: Cyberpunk theme

## 🎮 Demo Flow

```
1. Admin Login: admin / admin123
2. Admin → Create Customer: cust001 / pass123 + details  
3. Customer Login: cust001 / pass123
4. Customer → View balance / Deposit / Withdraw
```

## 🛠 Quick Start

### Local
```bash
pip install -r requirements.txt
python app.py
```

### Docker
```bash
docker-compose up --build
```

**Live**: http://localhost:5000

## 📁 Structure
```
├── app.py (Flask + role auth)
├── models/ (User, Customer, CustomerUser)
├── templates/ (admin/customer dashboards)  
├── static/style.css (cyberpunk theme)
├── Dockerfile + docker-compose.yml
```

## 🔧 Tech Stack
- **Backend**: Flask, Gunicorn
- **Container**: Docker
- **Storage**: In-memory (Redis/PostgreSQL ready)

## 📄 License
MIT - Free to use & modify

