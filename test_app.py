from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.get_data(as_text=True) == "¡Hola, CI/CD con DevOps!"