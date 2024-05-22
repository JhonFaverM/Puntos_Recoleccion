from pydantic import BaseModel, Field
from typing import Tuple


class PuntosRecoleccionModel(BaseModel):
    id: str
    point_status: str
    neighborhood: str
    coordinates: Tuple[float, float] = Field(..., description="Latitude and longitude")
