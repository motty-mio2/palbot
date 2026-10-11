FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# ホストから /workdir がマウントされても仮想環境が消えないよう /opt/venv に作成
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

WORKDIR /workdir
COPY . /workdir/

ENTRYPOINT [ "python", "/workdir/src/main.py" ]