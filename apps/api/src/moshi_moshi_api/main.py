"""The FastAPI application.

At Milestone 0 the API answers one question — whether it is running. Twilio webhooks
and the Gemini Live media bridge arrive with Milestone 1.
"""

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

from moshi_moshi_api import __version__


class Health(BaseModel):
    """The answer to a liveness probe."""

    status: Literal["ok"]
    version: str


def create_app() -> FastAPI:
    """Build the application. Tests call this directly; uvicorn uses `app` below."""
    app = FastAPI(
        title="moshi-moshi API",
        version=__version__,
        summary="Hello? AI speaking.",
    )

    @app.get("/health")
    async def health() -> Health:
        return Health(status="ok", version=__version__)

    return app


app = create_app()
