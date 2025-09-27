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
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home
RUN curl -O https://cdn.npmmirror.com/binaries/chrome-for-testing/142.0.7436.0/linux64/chrome-linux64.zip && \
    unzip chrome-linux64.zip && \
    mv chrome-linux64 chrome && \
    rm chrome-linux64.zip

ENV PATH=$PATH:/home/chrome \
    PYTHONDONTWRITEBYTECODE=1
