
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from dependencies import get_db
from dto import sign_dto
from fastapi import APIRouter, Depends
from service import sign_service

router = APIRouter(
    prefix="/api/v1/sign",
    tags=["sign"]
)


@router.post("/up")
async def sign_up(reqDTO: sign_dto.ReqSignUp, db: Session = Depends(get_db)) -> JSONResponse:
    return sign_service.sign_up(reqDTO, db)
