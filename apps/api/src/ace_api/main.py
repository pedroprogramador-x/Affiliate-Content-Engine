"""Ponto de entrada da aplicação FastAPI do ACE."""

from __future__ import annotations

from fastapi import FastAPI

from ace_api import __version__
from ace_api.api.health import router as health_router


def create_app() -> FastAPI:
    """Cria e configura a instância FastAPI da API do ACE.

    Mantida como factory para que os testes possam construir instâncias
    isoladas e para que configuração futura (middlewares, routers
    adicionais) não dependa de estado global implícito.
    """
    app = FastAPI(
        title="ACE API",
        version=__version__,
        summary="Backend do Affiliate Content Engine.",
    )
    app.include_router(health_router)
    return app


app = create_app()
