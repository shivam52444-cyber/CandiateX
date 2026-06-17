FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    TRANSFORMERS_NO_TORCHVISION=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ca-certificates \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

# IMPORTANT: keep 8501 exposed (internal reference)
EXPOSE 7860

# CRITICAL FIX: use only Railway PORT
CMD ["streamlit", "run", "frontend.py", "--server.address=0.0.0.0", "--server.port=7860"]
