# Evercrow

This project is designed to read PDF files and count the number of birds that appear.

## How It's Made

**Tech used:**

- Frontend: TypeScript, React, NodeJS
- Backend: Python
- Deployment: Dockerfile

### Server

Made in Python with a FastAPI framework. The `main.py` file houses the endpoints and calls the functions in `extract.py` which extracts text from the PDF and returns a JSON formatted list of birds. Unit tests are built with `unittest`. These test the endpoints and text extraction logic.

### Client

UI made in React with TypeScript and a NodeJS server.

## How to Run

There are different ways to run locally:

1. Using the Docker Compose file

   - Run the following command:

   ```
   docker compose up
   ```

   This will create and run the docker containers for the frontend and backend. You can attach to the containers through VS Code or through the Docker Dashboard and run locally with the same steps as Step 2.

2. Through a virtual env in two separate terminals

   1. For the backend:

      - Go into the `backend` directory
      - Install a virtual environment

      ```
      python3 -m venv env
      ```

      - Activate the env

      ```
      source venv/bin/activate
      ```

      - Install the dependencies in `requirements.txt`

      ```
      pip install -r requirements.txt
      ```

      This will install all the dependencies in the virtual env to keep your machine clean of these.

      - Run the backend

      ```
      python3 evercrow/main.py
      ```

   2. For the frontend:
      - In a new terminal, go into the frontend directory
      - Install the dependencies
      ```
      npm install
      ```
      - Start the application
      ```
      npm start
      ```

## Things to do

- [] Create CI/CD Pipeline
- [] Create extensive list of common bird names
- [] Design and format the frontend
