# Estágio 1: O "Treino" (Builder)
FROM python:3.14-slim AS builder

# Variáveis de ambiente pro Python não dar "chilique" no Linux
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=2.3.2 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app

# Instala dependências de sistema (essencial no Linux para compilar libs)
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Adiciona o Poetry ao PATH
ENV PATH="/root/.local/bin:$PATH"

# Copia os arquivos de dependência
COPY pyproject.toml poetry.lock ./

# Instala as dependências (sem as de desenvolvimento)
RUN poetry install --only main --no-root

# Estágio 2: O "Jogo" (Runtime - Imagem Final)
FROM python:3.14-slim AS runtime

WORKDIR /app

# Copia apenas as bibliotecas instaladas no estágio anterior
COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia o código do seu Django
COPY . .

# Expondo a porta padrão do Django
EXPOSE 8000

# Comando para rodar (No Linux, usamos o gunicorn em produção, mas aqui vai o runserver)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]