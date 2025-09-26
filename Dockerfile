FROM ghcr.io/astral-sh/uv:python3.11-trixie-slim
RUN apt-get update && apt-get install -y \
    libnss3 \
    libnspr4 \
    libglib2.0-0 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libxss1 \
    libgtk-3-0 \
    libdrm2 \
    fonts-liberation \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* \

RUN useradd --create-home --shell /bin/bash app
USER app
WORKDIR /home/app

COPY chrome-linux64 chrome
COPY app.py pyproject.toml ./

ENV PATH=$PATH:/home/app/chrome \
    PYTHONDONTWRITEBYTECODE=1
RUN uv sync

EXPOSE 8000

ENTRYPOINT [ "uv", "run", "litestar", "run", "--host", "0.0.0.0"]
