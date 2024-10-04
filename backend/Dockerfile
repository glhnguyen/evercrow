FROM python:3.11-slim-bookworm

# Install poppler-utils and other required libraries
RUN apt-get update && apt-get install -y \
    poppler-utils \
    libpoppler-cpp-dev \
    tesseract-ocr \
    build-essential

WORKDIR /app
EXPOSE 8000

RUN pwd

COPY ./requirements.txt /evercrow/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /evercrow/requirements.txt

COPY ./evercrow ./evercrow

CMD ["python", "/app/evercrow/main.py"]