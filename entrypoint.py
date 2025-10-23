"""Entrypoint to run the API."""
import uvicorn

from src.app.config import app_config

uvicorn.run(
    app="src.app.main:app",
    host=app_config.APP_HOST,
    port=app_config.APP_PORT,
    reload=False,
    log_level="info"
)
