"""Endpoint de health check da API do ACE."""

from __future__ import annotations

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

from ace_api import __version__

router = APIRouter(tags=["health"])

SERVICE_NAME = "ace-api"


class HealthResponse(BaseModel):
    """Contrato estável da resposta de `GET /health`."""

    status: Literal["ok"]
    service: str
    version: str


@router.get("/health")
def health() -> HealthResponse:
    """Retorna o estado de saúde do serviço.

    Responde apenas com informação estática do processo. Não consulta
    banco, Supabase ou qualquer provider externo — por design, para que
    o health check nunca dependa de integrações que podem estar fora do
    ar ou não configuradas.
    """
    return HealthResponse(status="ok", service=SERVICE_NAME, version=__version__)
