import json
import pytest

from restful_cc import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_customer_registered(client):
    r = client.put(
        '/api/customer',
        data='{"first_name": "larry", "email": "larry@gmail.com", "trailing_digits": 1234}',
        headers={
            'Content-Type': 'application/json'
        })

    assert r.status_code == 201
    data = json.loads(r.data.decode('utf-8'))
    assert data['data'] == {
	"card_type": None,
        "email": "larry@gmail.com",
	"end_date": None,
        "first_name": "larry",
	"leading_digits": None,
        "start_date": None,
        "trailing_digits": 1234 }



    
def test_customer_found(client):
    r = client.get(
        '/api/customer',
        data='{"trailing_digits": 1234, "leading_digits": 5363}',
        headers={
            'Content-Type': 'application/json'
        })

    assert r.status_code == 200
    data = json.loads(r.data.decode('utf-8'))
    assert data['matches'] == {'larry@gmail.com': 'larry'}
    
def test_customer_not_found(client):
    r = client.get(
        '/api/customer',
        data='{"trailing_digits": 6789}',
        headers={
            'Content-Type': 'application/json'
        })

    assert r.status_code == 404
    data = json.loads(r.data.decode('utf-8'))
    assert data['matches'] == {}

