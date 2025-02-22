from typing import List

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.models.candidate import Candidate


class CandidateRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_unemployed_candidates(self) -> List[Candidate]:
        query = text("""
            SELECT 
                id,
                name,
                location,
                current_status
            FROM candidates 
            WHERE current_status = 'unemployed' 
                OR current_status IS NULL
        """)
        return self.db.execute(query).fetchall()
