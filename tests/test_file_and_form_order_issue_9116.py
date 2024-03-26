"""
See https://github.com/tiangolo/fastapi/discussions/9116

Showcases regression introduced in commit ab2b86f

"""
import pathlib

import pytest
from fastapi import FastAPI, File, Form
from fastapi.testclient import TestClient

app = FastAPI()


@app.post("/file_before_form")
def file_before_form(
    file: bytes = File(...),
    city: str = Form(...),
):
    return {"file_content": file, "city": city}


@app.post("/file_after_form")
def file_after_form(
    city: str = Form(...),
    file: bytes = File(...),
):
    return {"file_content": file, "city": city}


client = TestClient(app)


@pytest.fixture
def tmp_file(tmp_path) -> pathlib.Path:
    f = tmp_path / "example.txt"
    f.write_text("foo")
    return f


@pytest.mark.parametrize("endpoint_path", ("/file_before_form", "/file_after_form"))
def test_file_form_order(endpoint_path: str, tmp_file):
    with tmp_file.open("rb") as f:
        response = client.post(
            url=endpoint_path,
            data={"city": "Thimphou"},
            files={"file": (tmp_file.name, f)},
        )
    assert response.status_code == 200, response.text
    assert response.json() == {"file_content": "foo", "city": "Thimphou"}
