from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_api_version
from app.schemas import Item, ItemCreate

router = APIRouter(prefix="/items", tags=["items"])

ApiVersion = Annotated[str, Depends(get_api_version)]

items_db: list[Item] = [
    Item(id=1, name="Notebook", price=12.5, in_stock=True),
    Item(id=2, name="Pen", price=1.5, in_stock=False),
]


@router.get("", response_model=list[Item])
async def list_items(api_version: ApiVersion) -> list[Item]:
    """Return all items and show a simple dependency."""
    return items_db


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int, api_version: ApiVersion) -> Item:
    for item in items_db:
        if item.id == item_id:
            return item

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item {item_id} was not found",
    )


@router.post("", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate, api_version: ApiVersion) -> Item:
    new_item = Item(id=len(items_db) + 1, **item.model_dump())
    items_db.append(new_item)
    return new_item
