# 🚗 Ride Sharing Platform – Scalable Microservices Architecture

## 🧑‍💻 Team Members

- Muhammad Haiqal Dwikusuma – 22/496221/PA/21330  
- Kevin Beckham Hotama - 22/496130/PA/21308

---

## 📘 Project Overview

This project is a proof-of-concept **ride-sharing platform** built using **FastAPI**, designed following microservice principles. Each component is independently containerized with **Docker** and communicates over RESTful APIs. The project demonstrates scalability, service separation, and optimized performance using **Redis caching**.

---

## 🏗️ Architecture Highlights

Our system consists of multiple microservices:

- **🧍 User Service** – Manages user registration, login, and profiles.
- **🚕 Ride Service** – Handles ride creation, ride status, and ride listings.
- **💸 Payment Service** – Simulates payment confirmation and transaction logging.
- **🧠 Redis Caching** – Used across services for faster data retrieval.
- **🔀 API Gateway / Reverse Proxy** – (Optional future enhancement)
- **🛢️ Databases**:
  - MongoDB (User & Ride services)
  - PostgreSQL (Payment service)

Each service is containerized using Docker and orchestrated with `docker-compose`.

---

## 🔧 Tech Stack

| Layer             | Tech                     |
|------------------|--------------------------|
| Backend Framework| FastAPI (Python)         |
| Database         | MongoDB, PostgreSQL      |
| Caching          | Redis                    |
| Containerization | Docker, Docker Compose   |
| API Format       | RESTful JSON APIs        |

---

## ⚙️ How to Run Locally

### 1. Prerequisites

- Docker & Docker Compose installed

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/ride-sharing-platform.git
cd ride-sharing-platform
```

### 3. Run All Services

```bash
docker-compose up --build
```

### 4. Test Services (Example with HTTPie or Curl)

```bash
# Create a user
http POST localhost:8001/users username=haiqal password=secret

# Create a ride
http POST localhost:8002/rides id=ride123 driver="haiqal" status="available"

# Confirm payment
http POST localhost:8003/payments ride_id=ride123 amount=50000
```

---

## 📁 Project Structure

```
ride-sharing-platform/
├── user-service/
│   ├── main.py
│   └── routers/
│       └── user.py
│   └── services/
│       ├── db.py
│       ├── cache.py
│       └── auth.py
│
├── ride-service/
│   ├── main.py
│   └── routers/
│       └── ride.py
│   └── services/
│       ├── db.py
│       ├── cache.py
│       └── auth.py
│
├── payment-service/
│   ├── main.py
│   └── routers/
│       └── payment.py
│   └── services/
│       ├── db.py
│       ├── cache.py
│       └── auth.py
│
├── redis_cache.py
├── docker-compose.yml
└── README.md
```

---

## 🧪 Example Cache Usage

Redis is used to store recent queries (e.g., ride status). The `redis_cache.py` file contains utility functions:

```python
# redis_cache.py

import redis
import json

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)
CACHE_TTL = 300  # seconds

def get_from_cache(key: str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None

def set_cache(key: str, value: dict, ttl: int = CACHE_TTL):
    redis_client.set(key, json.dumps(value), ex=ttl)
```

---

## 📸 Screenshots

> _(Optional: Add screenshots of API testing or Postman results here if desired)_

---

## 📈 Future Improvements

- Add authentication tokens using JWT
- API Gateway for unified routing
- Frontend dashboard using React.js
- Integration with real payment API (e.g., Stripe)

---

## 📚 References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Redis Documentation](https://redis.io/)
- [PostgreSQL Documentation](https://www.postgresql.org/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)

---

## 📝 License

MIT License © 2025 – Ride Sharing Team
