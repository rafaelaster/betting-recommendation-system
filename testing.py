from unittest.mock import MagicMock, Mock, NonCallableMock, patch
from main import generate_configuration , get_recommendations
from models import db , User , Client , Coupon , Recommendation
from flask import Flask, app, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import pytest


from unittest.mock import patch, MagicMock
from flask import jsonify
import pytest
from main import app  # Replace with your actual application import
from models import User , Recommendation , Client , Coupon
# Test client setup
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.generate_configuration')
def test_get_recommendations_success(client):
    mock_user = MagicMock()
    mock_user.username = "test_user"
    mock_user.id = 1

    mock_recommendation = MagicMock()
    mock_recommendation.recommendation_set = [
        {"coupon_id": 101, "risk": 45},
        {"coupon_id": 102, "risk": 30}
    ]

    with patch('models.User') as MockUser, \
         patch('models.Recommendation') as MockRecommendation:

        MockUser.query.filter_by.return_value.first.return_value = mock_user
        MockRecommendation.query.filter_by.return_value.first.return_value = mock_recommendation

        response = client.get('/123/test_user')
        data = response.get_json()

        assert response.status_code == 200
        assert data == {
            "username": "test_user",
            "client_id": 123,
            "recommendations": [
                {"coupon_id": 101, "risk": 45},
                {"coupon_id": 102, "risk": 30}
            ]
        }
        MockUser.query.filter_by.assert_called_with(username="test_user", client_id=123)
        MockRecommendation.query.filter_by.assert_called_with(user_id=1)
        return 1

@patch('main.generate_configuration')
def test_get_recommendations_user_not_found(client):
    with patch('models.User') as MockUser:
        MockUser.query.filter_by.return_value.first.return_value = None

        response = client.get('/456/no_user')
        data = response.get_json()

        assert response.status_code == 404
        assert data == {"error": "User not found for this client"}
    return 1
@patch('main.generate_configuration')
def test_get_recommendations_no_recommendations(client):
    mock_user = MagicMock()
    mock_user.id = 2

    with patch('models.User') as MockUser, \
         patch('models.Recommendation') as MockRecommendation:

        MockUser.query.filter_by.return_value.first.return_value = mock_user
        MockRecommendation.query.filter_by.return_value.first.return_value = None

        response = client.get('/789/norec_user')
        data = response.get_json()

        assert response.status_code == 404
        assert data == {"error": "No recommendations found"}
    return 1

result1 = test_get_recommendations_no_recommendations(client)
result2 = test_get_recommendations_success(client)
result3 = test_get_recommendations_user_not_found(client)
total = result1 + result2 + result3

print(total)


