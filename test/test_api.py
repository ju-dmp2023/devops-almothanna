import pytest
from calculator_client import Client
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.api.actions import calculate

def test_api_calculate_add():
    client = Client(base_url="http://localhost:5000")
    
    body = Calculation(
        operation=Opertions.ADD, 
        operand1=5.0, 
        operand2=3.0
    )

    result = calculate.sync(client=client, body=body)

    assert result.result == 8.0