FROM python:3.12-slim

RUN useradd --create-home --uid 10001 helpdesk && mkdir /dados && chown helpdesk /dados

WORKDIR /app
COPY requirements ./requirements
RUN pip install --no-cache-dir -r requirements
COPY app ./app

USER helpdesk
ENV DATABASE_URL=sqlite:////dados/inventario.db \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]
