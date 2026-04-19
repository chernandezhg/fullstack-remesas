from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.remittance import Remittance
from app.schemas.remittance import RemittanceCreate
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/")
def create_remittance(
    data: RemittanceCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    new_remittance = Remittance(
        amount=data.amount,
        receiver_name=data.receiver_name,
        sender_id=user.id
    )

    db.add(new_remittance)
    db.commit()
    db.refresh(new_remittance)

    return new_remittance


@router.get("/")
def get_remittances(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return db.query(Remittance)\
        .filter(Remittance.sender_id == user.id)\
        .all()


@router.delete("/{id}")
def delete_remittance(
    id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    remittance = db.query(Remittance).filter(
        Remittance.id == id,
        Remittance.sender_id == user.id
    ).first()

    if not remittance:
        raise HTTPException(status_code=404, detail="No encontrada")

    db.delete(remittance)
    db.commit()

    return {"message": "Eliminada"}