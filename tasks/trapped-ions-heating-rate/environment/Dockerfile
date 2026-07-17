FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive \
    OMP_NUM_THREADS=1 \
    OPENBLAS_NUM_THREADS=1 \
    MKL_NUM_THREADS=1 \
    MPLBACKEND=Agg

RUN pip install --no-cache-dir \
    numpy==1.26.4 \
    scipy==1.13.1 \
    h5py==3.14.0 \
    matplotlib==3.9.4 \
    pytest==8.4.1 \
    pytest-json-ctrf==0.3.5

WORKDIR /app

RUN mkdir -p \
    /app \
    /root/data \
    /home/agent/.claude \
    /home/agent/.codex \
    /home/agent/.opencode \
    /home/agent/.agents && \
    chmod -R 777 /home/agent && \
    chmod 777 /root

COPY data/ /root/data/
