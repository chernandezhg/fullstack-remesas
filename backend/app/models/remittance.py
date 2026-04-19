from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db.database import Base

class Remittance(Base):
    __tablename__ = "remittances"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    receiver_name = Column(String, nullable=False)

    sender_id = Column(Integer, ForeignKey("users.id"))

    status = Column(String, default="pending")

    currency = Column(String, default="USD")
    note = Column(String, nullable=True)