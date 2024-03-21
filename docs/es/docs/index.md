---
hide:
  - navigation
---

<style>
.md-content .md-typeset h1 { display: none; }
</style>

<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, alto desempeño, fácil de aprender, rápido de programar, listo para producción</em>
</p>
<p align="center">
<a href="https://github.com/tiangolo/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/tiangolo/fastapi/workflows/Test/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/tiangolo/fastapi" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/tiangolo/fastapi.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

---

**Documentación**: <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a>

**Código Fuente**: <a href="https://github.com/tiangolo/fastapi" target="_blank">https://github.com/tiangolo/fastapi</a>

---

FastAPI es un web framework moderno y rápido (de alto rendimiento) para construir APIs con Python 3.8+ basado en las anotaciones de tipos estándar de Python.

Sus características principales son:

* **Rapidez**: Alto rendimiento, a la par con **NodeJS** y **Go** (gracias a Starlette y Pydantic). [Uno de los frameworks de Python más rápidos](#rendimiento).
* **Rápido de programar**: Incrementa la velocidad de desarrollo entre 200% y 300%. *
* **Menos errores**: Reduce los errores humanos (de programador) aproximadamente un 40%. *
* **Intuitivo**: Gran soporte en los editores con <abbr title="conocido en inglés como auto-complete, autocompletion, IntelliSense, completion">auto completado</abbr> en todas partes. Gasta menos tiempo <abbr title="buscando y corrigiendo errores">debugging</abbr>.
* **Fácil**: Está diseñado para ser fácil de usar y aprender. Gastando menos tiempo leyendo documentación.
* **Corto**: Minimiza la duplicación de código. Múltiples funcionalidades con cada declaración de parámetros. Menos errores.
* **Robusto**: Crea código listo para producción con documentación automática interactiva.
* **Basado en estándares**: Basado y totalmente compatible con los estándares abiertos para APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (conocido previamente como Swagger) y <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

<small>* Esta estimación está basada en pruebas con un equipo de desarrollo interno construyendo aplicaciones listas para producción.</small>

## Sponsors

<!-- sponsors -->

{% if sponsors %}
{% for sponsor in sponsors.gold -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor -%}
{%- for sponsor in sponsors.silver -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor %}
{% endif %}

<!-- /sponsors -->

<a href="https://fastapi.tiangolo.com/fastapi-people/#sponsors" class="external-link" target="_blank">Otros sponsors</a>

## Opiniones

"_[...] I'm using **FastAPI** a ton these days. [...] I'm actually planning to use it for all of my team's **ML services at Microsoft**. Some of them are getting integrated into the core **Windows** product and some **Office** products._"

<div style="text-align: right; margin-right: 10%;">Kabir Khan - <strong>Microsoft</strong> <a href="https://github.com/tiangolo/fastapi/pull/26" target="_blank"><small>(ref)</small></a></div>

---

"_We adopted the **FastAPI** library to spawn a **REST** server that can be queried to obtain **predictions**. [for Ludwig]_"

<div style="text-align: right; margin-right: 10%;">Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - <strong>Uber</strong> <a href="https://eng.uber.com/ludwig-v0-2/" target="_blank"><small>(ref)</small></a></div>

---

"_**Netflix** is pleased to announce the open-source release of our **crisis management** orchestration framework: **Dispatch**! [built with **FastAPI**]_"

<div style="text-align: right; margin-right: 10%;">Kevin Glisson, Marc Vilanova, Forest Monsen - <strong>Netflix</strong> <a href="https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072" target="_blank"><small>(ref)</small></a></div>

---

"_I’m over the moon excited about **FastAPI**. It’s so fun!_"

<div style="text-align: right; margin-right: 10%;">Brian Okken - <strong><a href="https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855" target="_blank">Python Bytes</a> podcast host</strong> <a href="https://twitter.com/brianokken/status/1112220079972728832" target="_blank"><small>(ref)</small></a></div>

---

"_Honestly, what you've built looks super solid and polished. In many ways, it's what I wanted **Hug** to be - it's really inspiring to see someone build that._"

<div style="text-align: right; margin-right: 10%;">Timothy Crosley - <strong><a href="https://www.hug.rest/" target="_blank">Hug</a> creator</strong> <a href="https://news.ycombinator.com/item?id=19455465" target="_blank"><small>(ref)</small></a></div>

---

"_If you're looking to learn one **modern framework** for building REST APIs, check out **FastAPI** [...] It's fast, easy to use and easy to learn [...]_"

"_We've switched over to **FastAPI** for our **APIs** [...] I think you'll like it [...]_"

<div style="text-align: right; margin-right: 10%;">Ines Montani - Matthew Honnibal - <strong><a href="https://explosion.ai" target="_blank">Explosion AI</a> founders - <a href="https://spacy.io" target="_blank">spaCy</a> creators</strong> <a href="https://twitter.com/_inesmontani/status/1144173225322143744" target="_blank"><small>(ref)</small></a> - <a href="https://twitter.com/honnibal/status/1144031421859655680" target="_blank"><small>(ref)</small></a></div>

---

"_If anyone is looking to build a production Python API, I would highly recommend **FastAPI**. It is **beautifully designed**, **simple to use** and **highly scalable**, it has become a **key component** in our API first development strategy and is driving many automations and services such as our Virtual TAC Engineer._"

<div style="text-align: right; margin-right: 10%;">Deon Pillsbury - <strong>Cisco</strong> <a href="https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/" target="_blank"><small>(ref)</small></a></div>

---

## **Typer**, el FastAPI de las CLIs

<a href="https://typer.tiangolo.com" target="_blank"><img src="https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

Si estás construyendo un app de <abbr title="Interfaz de línea de comandos en español">CLI</abbr> para ser usada en la terminal en vez de una API web, fíjate en <a href="https://typer.tiangolo.com/" class="external-link" target="_blank">**Typer**</a>.

**Typer** es el hermano menor de FastAPI.  La intención es que sea el **FastAPI de las CLIs**. ⌨️ 🚀

## Requisitos

Python 3.8+

FastAPI está sobre los hombros de gigantes:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> para las partes web.
* <a href="https://pydantic-docs.helpmanual.io/" class="external-link" target="_blank">Pydantic</a> para las partes de datos.

## Instalación

<div class="termy">

```console
$ pip install fastapi

---> 100%
```

</div>

También vas a necesitar un servidor ASGI para producción cómo <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> o <a href="https://gitlab.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.

<div class="termy">

```console
$ pip install "uvicorn[standard]"

---> 100%
```

</div>

## Ejemplo

### Créalo

* Crea un archivo `main.py` con:

```Python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

<details markdown="1">
<summary>O usa <code>async def</code>...</summary>

Si tu código usa `async` / `await`, usa `async def`:

```Python hl_lines="9  14"
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

**Nota**:

Si no lo sabes, revisa la sección _"¿Con prisa?"_ sobre <a href="https://fastapi.tiangolo.com/es/async/#con-prisa" target="_blank">`async` y `await` en la documentación</a>.

</details>

### Córrelo

Corre el servidor con:

<div class="termy">

```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

<details markdown="1">
<summary>Sobre el comando <code>uvicorn main:app --reload</code>...</summary>

El comando `uvicorn main:app` se refiere a:

* `main`: el archivo `main.py` (el"modulo" de Python).
* `app`: el objeto creado dentro de `main.py` con la línea `app = FastAPI()`.
* `--reload`: hace que el servidor se reinicie después de cambios en el código. Esta opción solo debe ser usada en desarrollo.

</details>

### Revísalo

Abre tu navegador en <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a>.

Verás la respuesta de JSON cómo:

```JSON
{"item_id": 5, "q": "somequery"}
```

Ya creaste una API que:

* Recibe HTTP requests en los _paths_ `/` y `/items/{item_id}`.
* Ambos _paths_ toman <em>operaciones</em> `GET` (también conocido como HTTP _methods_).
* El _path_ `/items/{item_id}` tiene un _path parameter_ `item_id` que debería ser un `int`.
* El _path_ `/items/{item_id}` tiene un `str` _query parameter_ `q` opcional.

### Documentación interactiva de APIs

Ahora ve a <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

Verás la documentación automática e interactiva de la API (proveída por <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Documentación alternativa de la API

Ahora, ve a <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

Ahora verás la documentación automática alternativa (proveída por <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## Mejora al ejemplo

Ahora modifica el archivo `main.py` para recibir un <abbr title="cuerpo del mensaje HTTP">body</abbr> del `PUT` request.

Declara el body usando las declaraciones de tipo estándares de Python gracias a Pydantic.

```Python hl_lines="4  9-12  25-27"
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

El servidor debería recargar automáticamente (porque añadiste `--reload` al comando `uvicorn` que está más arriba).

### Mejora a la documentación interactiva de APIs

Ahora ve a <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

* La documentación interactiva de la API se actualizará automáticamente, incluyendo el nuevo body:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

* Haz click en el botón de "Try it out" que te permite llenar los parámetros e interactuar directamente con la API:

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

* Luego haz click en el botón de "Execute". La interfaz de usuario se comunicará con tu API, enviará los parámetros y recibirá los resultados para mostrarlos en pantalla:

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Mejora a la documentación alternativa de la API

Ahora, ve a <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

* La documentación alternativa también reflejará el nuevo parámetro de query y el body:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### Resumen

En resumen, declaras los tipos de parámetros, body, etc. **una vez** como parámetros de la función.

Lo haces con tipos modernos estándar de Python.

No tienes que aprender una sintaxis nueva, los métodos o clases de una library específica, etc.

Solo **Python 3.8+** estándar.

Por ejemplo, para un `int`:

```Python
item_id: int
```

o para un modelo más complejo de `Item`:

```Python
item: Item
```

...y con esa única declaración obtienes:

* Soporte del editor incluyendo:
    * Auto completado.
    * Anotaciones de tipos.
* Validación de datos:
    * Errores automáticos y claros cuándo los datos son inválidos.
    * Validación, incluso para objetos JSON profundamente anidados.
* <abbr title="en inglés: serialization, parsing, marshalling">Conversión</abbr> de datos de input: viniendo de la red a datos y tipos de Python. Leyendo desde:
    * JSON.
    * Path parameters.
    * Query parameters.
    * Cookies.
    * Headers.
    * Formularios.
    * Archivos.
* <abbr title="en inglés: serialization, parsing, marshalling">Conversión</abbr> de datos de output: convirtiendo de datos y tipos de Python a datos para la red (como JSON):
    * Convertir tipos de Python (`str`, `int`, `float`, `bool`, `list`, etc).
    * Objetos `datetime`.
    * Objetos `UUID`.
    * Modelos de bases de datos.
    * ...y muchos más.
* Documentación automática e interactiva incluyendo 2 interfaces de usuario alternativas:
    * Swagger UI.
    * ReDoc.

---

Volviendo al ejemplo de código anterior, **FastAPI** va a:

* Validar que existe un `item_id` en el path para requests usando `GET` y `PUT`.
* Validar que el `item_id` es del tipo `int` para requests de tipo `GET` y `PUT`.
    * Si no lo es, el cliente verá un mensaje de error útil y claro.
* Revisar si existe un query parameter opcional llamado `q` (cómo en `http://127.0.0.1:8000/items/foo?q=somequery`) para requests de tipo `GET`.
    * Como el parámetro `q` fue declarado con `= None` es opcional.
    * Sin el `None` sería obligatorio (cómo lo es el body en el caso con `PUT`).
* Para requests de tipo `PUT` a `/items/{item_id}` leer el body como JSON:
    * Revisar si tiene un atributo requerido `name` que debe ser un `str`.
    * Revisar si tiene un atributo requerido `price` que debe ser un `float`.
    * Revisar si tiene un atributo opcional `is_offer`, que debe ser un `bool`si está presente.
    * Todo esto funcionaría para objetos JSON profundamente anidados.
* Convertir de y a JSON automáticamente.
* Documentar todo con OpenAPI que puede ser usado por:
    * Sistemas de documentación interactiva.
    * Sistemas de generación automática de código de cliente para muchos lenguajes.
* Proveer directamente 2 interfaces de documentación web interactivas.

---

Hasta ahora, escasamente vimos lo básico pero ya tienes una idea de cómo funciona.

Intenta cambiando la línea a:

```Python
    return {"item_name": item.name, "item_id": item_id}
```

...de:

```Python
        ... "item_name": item.name ...
```

...a:

```Python
        ... "item_price": item.price ...
```

... y mira como el editor va a auto-completar los atributos y sabrá sus tipos:

![soporte de editor](https://fastapi.tiangolo.com/img/vscode-completion.png)

Para un ejemplo más completo que incluye más características ve el <a href="https://fastapi.tiangolo.com/tutorial/">Tutorial - Guía de Usuario</a>.

**Spoiler alert**: el Tutorial - Guía de Usuario incluye:

* Declaración de **parámetros** en otros lugares diferentes cómo los: **headers**, **cookies**, **formularios** y **archivos**.
* Cómo agregar **requisitos de validación** cómo `maximum_length` o `regex`.
* Un sistema de **<abbr title="también conocido en inglés cómo: components, resources, providers, services, injectables">Dependency Injection</abbr>** poderoso y fácil de usar.
* Seguridad y autenticación incluyendo soporte para **OAuth2** con **JWT tokens** y **HTTP Basic** auth.
* Técnicas más avanzadas, pero igual de fáciles, para declarar **modelos de JSON profundamente anidados** (gracias a Pydantic).
* **GraphQL** integrado con <a href="https://strawberry.rocks" class="external-link" target="_blank">Strawberry</a> y otras libraries.
* Muchas características extra (gracias a Starlette) como:
    * **WebSockets**
    * pruebas extremadamente fáciles con HTTPX y `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...y mucho más.

## Rendimiento

Benchmarks independientes de TechEmpower muestran que aplicaciones de **FastAPI** corriendo con Uvicorn cómo <a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">uno de los frameworks de Python más rápidos</a>, únicamente debajo de Starlette y Uvicorn (usados internamente por FastAPI). (*)

Para entender más al respecto revisa la sección <a href="https://fastapi.tiangolo.com/benchmarks/" class="internal-link" target="_blank">Benchmarks</a>.

## Dependencias Opcionales

Usadas por Pydantic:

* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email_validator</code></a> - para validación de emails.
* <a href="https://docs.pydantic.dev/latest/usage/pydantic_settings/" target="_blank"><code>pydantic-settings</code></a> - para la gestión de configuración.
* <a href="https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/" target="_blank"><code>pydantic-extra-types</code></a> - para tipos extras utilizados con Pydantic.

Usados por Starlette:

* <a href="https://www.python-httpx.org" target="_blank"><code>httpx</code></a> - Requerido si quieres usar el `TestClient`.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - Requerido si quieres usar la configuración por defecto de templates.
* <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> - Requerido si quieres dar soporte a  <abbr title="convertir el string que viene de un HTTP request a datos de Python">"parsing"</abbr> de formularios, con `request.form()`.
* <a href="https://pythonhosted.org/itsdangerous/" target="_blank"><code>itsdangerous</code></a> - Requerido para dar soporte a `SessionMiddleware`.
* <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" target="_blank"><code>pyyaml</code></a> - Requerido para dar soporte al `SchemaGenerator` de Starlette (probablemente no lo necesites con FastAPI).
* <a href="https://graphene-python.org/" target="_blank"><code>graphene</code></a> - Requerido para dar soporte a `GraphQLApp`.
* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - Requerido si quieres usar `UJSONResponse`.

Usado por FastAPI / Starlette:

* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - para el servidor que carga y sirve tu aplicación.
* <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - Requerido si quieres usar `ORJSONResponse`.

Puedes instalarlos con `pip install fastapi[all]`.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia del MIT.
