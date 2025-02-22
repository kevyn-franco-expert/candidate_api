from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.repositories.candidate_repository import CandidateRepository
from app.schemas.candidate import CandidateResponse
from app.services.candidate_service import CandidateService

router = APIRouter()


@router.get("/analyze/", response_model=CandidateResponse)
async def analyze_candidates(db: Session = Depends(get_db)):
    try:
        repository = CandidateRepository(db)
        service = CandidateService(repository)
        return service.analyze_unemployed_candidates()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing candidates: {str(e)}"
        )
