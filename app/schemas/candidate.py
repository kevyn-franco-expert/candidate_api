from typing import Optional

from pydantic import BaseModel


class CandidateBase(BaseModel):
    name: str
    location: str
    current_status: Optional[str] = None


class CandidateResponse(BaseModel):
    total_unemployed: int
    location_with_most_unemployed: str
    unemployed_count_in_location: int
    timestamp: str
