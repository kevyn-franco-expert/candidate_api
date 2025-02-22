import math
from typing import Union


class CalculatorService:
    @staticmethod
    def evaluate_expression(expression: str) -> Union[float, str]:
        try:
            safe_expression = expression.replace('^', '**')

            safe_dict = {
                'abs': abs,
                'float': float,
                'int': int,
                'max': max,
                'min': min,
                'pow': pow,
                'round': round,
                'sum': sum,
                'sqrt': math.sqrt,
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'pi': math.pi,
                'e': math.e
            }

            result = eval(safe_expression, {"__builtins__": {}}, safe_dict)
            return float(result)
        except Exception as e:
            return f"Error evaluating expression: {str(e)}"
