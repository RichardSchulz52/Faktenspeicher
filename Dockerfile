FROM python:3.12-slim

EXPOSE 8501

ENV database_path=/usr/data/fakten.db

WORKDIR /usr/app
ADD pages ./pages
ADD Search.py .
ADD startup.py .
ADD repo.py .
ADD requirements.txt .
RUN python -m pip install -r requirements.txt
RUN mkdir -p ../data

ENTRYPOINT ["python", "startup.py"]