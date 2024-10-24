from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Welcome to the Replicate Image Generation API!"}

# Add more routes here as needed
