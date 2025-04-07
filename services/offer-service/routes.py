from fastapi import APIRouter
from schemas import OfferCreate
from service import OfferService
from database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()
offerService = OfferService()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/create-offer/")
async def create_offer(offer: OfferCreate, db: AsyncSession = Depends(get_db)):
    await offerService.createOffer(offer, db)
    return {"message": "User created successfully"}
