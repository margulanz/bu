from fastapi.testclient import TestClient
from src.main import app
from src.classify import classify


client = TestClient(app)



IMAGEDIR = "tests/"

def test_upload_image():
	filename = "strawberries.jpg"
	response = client.post(
    	"/images/", files={"file": ("filename", open(f"{IMAGEDIR}{filename}", "rb"), "image/jpeg")}
	)
	assert response.status_code == 200
	assert response.json() == {'status':'success'}


def test_prediction():
	filename = "strawberries.jpg"
	response = classify(f"{IMAGEDIR}{filename}")
	assert response['Label'] == 'strawberry'
	assert int(response['percentage']) == 99






