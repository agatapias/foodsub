from fastapi import APIRouter
from schemas import OfferCreate
from service import OfferService

router = APIRouter()
offerService = OfferService()

@router.post("/create-offer/")
async def create_offer(offer: OfferCreate):
    await offerService.createOffer(offer)
    return {"message": "User created successfully"}
