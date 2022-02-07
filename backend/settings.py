from pydantic import BaseSettings, Field, PostgresDsn


class AsyncPostgresDsn(PostgresDsn):
    # from: https://github.com/tiangolo/full-stack-fastapi-postgresql/pull/359/files
    allowed_schemes = {"postgres+asyncpg", "postgresql+asyncpg"}


class Settings(BaseSettings):
    DATABASE_URL: AsyncPostgresDsn = Field(
        env="DATABASE_URL",
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
