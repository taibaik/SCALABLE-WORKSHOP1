from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis_cache import get_from_cache, set_cache

app = FastAPI()

# ------------------ RIDE SERVICE ------------------

FAKE_RIDES_DB = {}

class RideCreate(BaseModel):
    id: str
    driver: str
    status: str

@app.post("/rides")
async def create_ride(ride: RideCreate):
    if ride.id in FAKE_RIDES_DB:
        raise HTTPException(status_code=400, detail="Ride already exists")
    FAKE_RIDES_DB[ride.id] = ride.dict()
    set_cache(f"ride:{ride.id}", ride.dict())
    return {"message": "Ride created", "ride": ride.dict()}

@app.get("/rides/{ride_id}")
async def get_ride(ride_id: str):
    cache_key = f"ride:{ride_id}"
    ride = get_from_cache(cache_key)
    if ride:
        print(f"Ride Cache HIT: {cache_key}")
        return ride
    ride = FAKE_RIDES_DB.get(ride_id)
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    set_cache(cache_key, ride)
    return ride

# ------------------ USER SERVICE ------------------

FAKE_USERS_DB = {}

class UserCreate(BaseModel):
    id: str
    name: str
    role: str

@app.post("/users")
async def create_user(user: UserCreate):
    if user.id in FAKE_USERS_DB:
        raise HTTPException(status_code=400, detail="User already exists")
    FAKE_USERS_DB[user.id] = user.dict()
    set_cache(f"user:{user.id}", user.dict())
    return {"message": "User created", "user": user.dict()}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    cache_key = f"user:{user_id}"
    user = get_from_cache(cache_key)
    if user:
        print(f"User Cache HIT: {cache_key}")
        return user
    user = FAKE_USERS_DB.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    set_cache(cache_key, user)
    return user
