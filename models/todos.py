from pydantic import BaseModel

class Todo(BaseModel):
    """
    docstring
    """
    nitrogen: str
    phosphorous: str
    potassium: str
    temperature: str
    ph: str


class CropData(BaseModel):
    N: float
    P: float
    K: float
    ph: float
    humidity: float
    ec: float
    temperature: float
    username: str
    id: str
 
