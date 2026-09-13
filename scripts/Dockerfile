FROM python:3.12-slim AS rustbuild
RUN apt-get update && apt-get install -y --no-install-recommends curl build-essential \
    && rm -rf /var/lib/apt/lists/*
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal --default-toolchain 1.98.0
ENV PATH=/root/.cargo/bin:$PATH
RUN pip install --no-cache-dir maturin==1.15.0
WORKDIR /src
COPY rust_engine rust_engine
RUN maturin build -m rust_engine/pyengine/Cargo.toml --release -i python3.12 --out /wheels

FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=rustbuild /wheels/*.whl /tmp/
RUN pip install --no-cache-dir /tmp/*.whl && rm -f /tmp/*.whl
COPY . .
ENV PYTHONUNBUFFERED=1 OMP_NUM_THREADS=1
CMD ["python", "-u", "product3_server.py"]
