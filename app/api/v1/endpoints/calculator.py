from fastapi import APIRouter, HTTPException

from app.schemas.calculator import CalculatorInput, CalculatorResponse
from app.services.calculator_service import CalculatorService

router = APIRouter()


@router.post("/calculate/", response_model=CalculatorResponse)
async def calculate_expression(input_data: CalculatorInput):
    calculator = CalculatorService()
    result = calculator.evaluate_expression(input_data.expression)

    if isinstance(result, str):
        raise HTTPException(status_code=400, detail=result)

    return CalculatorResponse(
        result=result,
        expression=input_data.expression
    )
