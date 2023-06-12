from pydantic import BaseModel


class DataSchema(BaseModel):
    phone: str
    address: str

