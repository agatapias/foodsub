from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.future import select
from models import Offer, Meal
from schemas import OfferCreate

class OfferService():

    async def get_db(self):
        async with SessionLocal() as session:
            yield session

    async def createOffer(self, offer: OfferCreate):
        db: AsyncSession = Depends(self.get_db)
        meals = []
        for meal in offer.meals:
            db_meal = Meal(
                name= meal.name,
                description = meal.description
            )
            meals.append(db_meal)
        db_offer = Offer(
            name=offer.name,
            duration=offer.duration,
            pricePerDay=offer.pricePerDay,
            meals=meals
        )
        db.add(db_offer)
        await db.commit()
