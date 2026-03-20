from pydantic import BaseModel

class ListItem(BaseModel):
        id: int
        name: str
        description: str