from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=2, examples=["Coffee"])
    price: float = Field(gt=0, examples=[4.5])
    in_stock: bool = True


class Item(ItemCreate):
    id: int
