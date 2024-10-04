FROM python:3.11-slim-bookworm

WORKDIR /app
EXPOSE 8000

RUN pwd

COPY ./requirements.txt /evercrow/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /evercrow/requirements.txt

COPY ./evercrow ./evercrow

CMD ["python", "/app/evercrow/main.py"]