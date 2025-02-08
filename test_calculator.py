import pytest
from app import app  # Import the Flask app from your app.py
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
def test_calculator_addition(client):
    """Test the addition functionality"""
    response = client.post('/', data={'num1': '3', 'num2': '5', 'operation': '+'})
    assert b'Result' in response.data  # Check if the result is displayed in the response
    assert b'8.0' in response.data  # Check if the result is correct (3 + 5)
def test_calculator_subtraction(client):
    """Test the subtraction functionality"""
    response = client.post('/', data={'num1': '10', 'num2': '5', 'operation': '-'})
    assert b'Result' in response.data
    assert b'5.0' in response.data  # Check if the result is correct (10 - 5)
def test_calculator_invalid_operation(client):
        """Test invalid operation"""
        response = client.post('/', data={'num1': '5', 'num2': '3', 'operation': '%'})
        assert b'Invalid Operation' in response.data  # Check if the "Invalid Operation" message appears
