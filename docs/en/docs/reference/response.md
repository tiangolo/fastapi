# `Response` class

You can declare a parameter in a *path operation function* or dependency to be of type
`Response` and then you can set data for the response like headers or cookies.

You can also use it directly to create an instance of it and return it from your *path
operations*.

You can import it directly from `fastapi`:

```python
from fastapi import Response
```

::: starlette.responses.Response
    options:
        members:
            - charset
            - status_code
            - media_type
            - body
            - background
            - raw_headers
            - render
            - init_headers
            - headers
            - set_cookie
            - delete_cookie