from typing import List

import pytest
from fastapi import FastAPI, File, Form
from fastapi.testclient import TestClient
from typing_extensions import Annotated

app = FastAPI()


@app.post("/files/")
async def create_file(token: Annotated[str, Form()], file: Annotated[bytes, File()]):
    return {
        "file_size": len(file),
        "token": token,
    }


@app.post("/multiple-files/")
async def create_multiple_file(
    token: Annotated[str, Form()], files: Annotated[List[bytes], File()]
):
    return {
        "file_contents": files,
        "token": token,
    }


client = TestClient(app)


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    json_response = response.json()
    assert json_response["components"]["schemas"]["Body_create_file_files__post"] == {
        "title": "Body_create_file_files__post",
        "required": ["token", "file"],
        "type": "object",
        "properties": {
            "token": {"title": "Token", "type": "string"},
            "file": {"title": "File", "type": "string", "format": "binary"},
        },
    }
    assert json_response["components"]["schemas"][
        "Body_create_multiple_file_multiple_files__post"
    ] == {
        "title": "Body_create_multiple_file_multiple_files__post",
        "required": ["token", "files"],
        "type": "object",
        "properties": {
            "token": {"title": "Token", "type": "string"},
            "files": {
                "items": {"format": "binary", "type": "string"},
                "title": "Files",
                "type": "array",
            },
        },
    }


def test_post_form_no_body():
    response = client.post("/files/")
    assert response.status_code == 422, response.text


def test_post_form_no_file():
    response = client.post("/files/", data={"token": "foo"})
    assert response.status_code == 422, response.text


def test_post_body_json():
    response = client.post("/files/", json={"file": "Foo", "token": "Bar"})
    assert response.status_code == 422, response.text


def test_post_file_no_token(tmp_path):
    path = tmp_path / "test.txt"
    path.write_text("<file content>")
    with path.open("rb") as file:
        response = client.post(
            "/files/",
            files={"file": file},
        )
    assert response.status_code == 422, response.text


def test_post_files_and_token(tmp_path):
    path = tmp_path / "test.txt"
    path.write_text("<file content>")
    with path.open("rb") as file:
        response = client.post(
            "/files/",
            data={"token": "foo"},
            files={"file": file},
        )
    assert response.status_code == 200, response.text
    assert response.json() == {"file_size": 14, "token": "foo"}


@pytest.fixture
def f1(tmp_path):
    f_path = tmp_path / "example1.txt"
    f_path.write_text("foo")
    with f_path.open("rb") as f:
        yield f


@pytest.fixture
def f2(tmp_path):
    f_path = tmp_path / "example2.txt"
    f_path.write_text("bar")
    with f_path.open("rb") as f:
        yield f


def test_post_multiple_files_and_token(f1, f2):
    response = client.post(
        "/multiple-files/",
        data={"token": "foo"},
        files=[
            ("files", f1),
            ("files", f2),
        ],
    )

    assert response.status_code == 200, response.text
    assert response.json() == {"file_contents": ["foo", "bar"], "token": "foo"}
