from collections import Counter
from datetime import datetime

from app.repositories.candidate_repository import CandidateRepository
from app.schemas.candidate import CandidateResponse


class CandidateService:
    def __init__(self, repository: CandidateRepository):
        self.repository = repository

    def analyze_unemployed_candidates(self) -> CandidateResponse:
        candidates = self.repository.get_unemployed_candidates()

        if not candidates:
            return CandidateResponse(
                total_unemployed=0,
                location_with_most_unemployed="None",
                unemployed_count_in_location=0,
                timestamp=datetime.now().isoformat()
            )

        locations = Counter(candidate.location for candidate in candidates)
        most_common_location = locations.most_common(1)[0]

        return CandidateResponse(
            total_unemployed=len(candidates),
            location_with_most_unemployed=most_common_location[0],
            unemployed_count_in_location=most_common_location[1],
            timestamp=datetime.now().isoformat()
        )
