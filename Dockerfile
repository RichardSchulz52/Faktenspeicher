FROM python:3.12-slim

EXPOSE 8501

WORKDIR /usr/app
ADD pages ./pages
ADD Search.py .
ADD startup.py .
ADD repo.py .
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python", "startup.py"]