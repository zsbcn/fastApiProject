from ghcr.io/astral-sh/uv:python3.11-alpine
copy . .
cmd ["uvicorn","main:app" ]
