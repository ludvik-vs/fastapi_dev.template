from pydantic import BaseModel

class TestBase(BaseModel):
    name: str

    class Config:
        from_attributes = True