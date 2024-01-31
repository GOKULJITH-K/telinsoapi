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