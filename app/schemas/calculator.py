from pydantic import BaseModel


class CalculatorInput(BaseModel):
    expression: str


class CalculatorResponse(BaseModel):
    result: float
    expression: str
