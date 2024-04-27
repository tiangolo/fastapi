from unittest.mock import MagicMock, patch

import pytest
from fastapi import FastAPI
from fastapi.middleware.debugger import (
    DebuggerMiddleware,
    webpdb_catch_exceptions_middleware,
)
from fastapi.testclient import TestClient

MAGIC_VALUE_THAT_NEVER_RETURNS = 42


def get_client_for_new_app(middlware_params=None):
    app = FastAPI()
    app.add_middleware(DebuggerMiddleware, **(middlware_params or {}))

    @app.get("/call-debugger-on-raise")
    async def raise_exception():
        raise ValueError("Test")
        return MAGIC_VALUE_THAT_NEVER_RETURNS

    return TestClient(app)


@pytest.fixture
def pdb_test_client():
    return get_client_for_new_app()


@pytest.fixture
def webpdb_test_client():
    return get_client_for_new_app(
        {"start_debugger_func": webpdb_catch_exceptions_middleware}
    )


def test_pdb(pdb_test_client):
    pdb_mock = MagicMock()
    with patch.dict("sys.modules", {"pdb": pdb_mock}):
        with pytest.raises(ValueError):
            result = pdb_test_client.get("/call-debugger-on-raise")
            assert result != MAGIC_VALUE_THAT_NEVER_RETURNS

    assert pdb_mock.pm.called


def test_webpdb(webpdb_test_client):
    webpdb_mock = MagicMock()
    with patch.dict("sys.modules", {"web_pdb": webpdb_mock}):
        with pytest.raises(ValueError):
            result = webpdb_test_client.get("/call-debugger-on-raise")
            assert result != MAGIC_VALUE_THAT_NEVER_RETURNS

    assert webpdb_mock.catch_post_mortem.called
