from typing import Optional

from fastapi import FastAPI, Query
from fastapi._compat import PYDANTIC_V2
from fastapi.testclient import TestClient
from pydantic import BaseModel
from typing_extensions import Literal


class Dog(BaseModel):
    pet_type: Literal["dog"]
    name: str


class Matrjoschka(BaseModel):
    size: str = 0  # without type coecerion Query parameters are limited to str
    inner: Optional["Matrjoschka"] = None


app = FastAPI()


@app.post(
    "/pet",
    operation_id="createPet",
)
def createPet(pet: Dog = Query(style="deepObject")) -> Dog:
    return pet


@app.post(
    "/toy",
    operation_id="createToy",
)
def createToy(toy: Matrjoschka = Query(style="deepObject")) -> Matrjoschka:
    return toy


client = TestClient(app)


def test_pet():
    response = client.post("""/pet?pet[pet_type]=dog&pet[name]=doggy""")
    if PYDANTIC_V2:
        dog = Dog.model_validate(response.json())
    else:
        dog = Dog.parse_obj(response.json())
    assert response.status_code == 200
    assert dog.pet_type == "dog" and dog.name == "doggy"


def test_matrjoschka():
    response = client.post(
        """/toy?toy[size]=3&toy[inner][size]=2&toy[inner][inner][size]=1'"""
    )
    print(response)
    if PYDANTIC_V2:
        toy = Matrjoschka.model_validate(response.json())
    else:
        toy = Matrjoschka.parse_obj(response.json())
    assert response.status_code == 200
    assert toy
    assert toy.inner.size == "2"
