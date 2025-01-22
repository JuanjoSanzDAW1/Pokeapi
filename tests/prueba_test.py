from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200


    normalized_response = "".join(response.text.split())


    assert "<title>Bienvenida</title>" in normalized_response
    assert "<h1>Hola,Victor!</h1>" in normalized_response
    assert "<p>SomoselgrupodeJuanJosé,Luis,Erwin,LucianySergio.</p>" in normalized_response
