from pydantic import BaseModel, Field
from typing import Optional

class RemittanceCreate(BaseModel):
    amount: float = Field(gt=0)
    receiver_name: str
    note: Optional[str] = None