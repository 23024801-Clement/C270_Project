import pytest
from test import app
def test_addition():
    """Test case for addition operation"""
    with app.test_client() as client: #creating client
        response = client.post("/", data={"num1": "5", "num2": "3", "operation": "+"})
        assert b"8.0" in response.data