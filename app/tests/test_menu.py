import pytest
from app.main import mostrar_menu

def test_menu_opciones(capsys):
    mostrar_menu()
    captured = capsys.readouterr()
    assert "1. Ingresar API Key" in captured.out
    assert "2. Importar fotos y seleccionar" in captured.out
