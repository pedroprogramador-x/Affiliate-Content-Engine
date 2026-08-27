"""Testes do endpoint `GET /health` e da criação da aplicação.

Nenhum teste acessa rede ou serviços externos: o `TestClient` exercita
a aplicação ASGI em processo.
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.testclient import TestClient

from ace_api import __version__
from ace_api.main import app, create_app


def test_create_app_returns_fastapi_instance() -> None:
    assert isinstance(create_app(), FastAPI)


def test_fresh_app_instance_serves_health() -> None:
    """Uma instância recém-criada por `create_app()` já expõe `/health`."""
    with TestClient(create_app()) as client:
        assert client.get("/health").status_code == 200


def test_health_status_code() -> None:
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200


def test_health_response_contract() -> None:
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.json() == {
        "status": "ok",
        "service": "ace-api",
        "version": __version__,
    }
