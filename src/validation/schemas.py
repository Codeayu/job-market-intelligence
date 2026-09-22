from pydantic import BaseModel, Field

class Product(BaseModel):
    id: int = Field(gt=0)
    title: str=Field(min_length=1)
    price: float = Field(ge=0)
    rating: float = Field(default=0, ge=0,le=5)
    category: str= Field(min_length=1)