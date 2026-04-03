from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Monkey Mesh"
    debug: bool = False
    low_complexity_model: str = "ollama/mistral"
    medium_complexity_model: str = "mistral/mixtral-8x7b-instruct"
    high_complexity_model: str = "anthropic/claude-3-5-sonnet-20241022"
    langfuse_enabled: bool = True


settings = Settings()
