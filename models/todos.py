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
    N: str
    P: str
    K: str
    ph: str
    humidity: str
    ec: str
    temperature: str
    username: str
    id: str
 
