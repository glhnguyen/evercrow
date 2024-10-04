from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from extract import extract_text_and_count_birds, get_bird_names
import os
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {'Hello': 'World'}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)) -> dict:
    """
    Endpoint to handle PDF file uploads, extract text using OCR if necessary, and count bird names.

    Args:
        file (UploadFile): Uploaded PDF file.

    Returns:
        Dict[str, int]: A dictionary with the count of bird names.
    """

    bird_names = get_bird_names()

     # Ensure the uploaded file is a PDF
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a PDF.")

    # Save uploaded file temporarily
    file_path = f"temp_{file.filename}"
    try:
        with open(file_path, "wb") as temp_file:
            temp_file.write(await file.read())
        
        # Extract text and count birds
        bird_counts = extract_text_and_count_birds(file_path, bird_names)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the file: {e}")
    
    finally:
        # Clean up and remove the temporary file after processing
        if os.path.exists(file_path):
            os.remove(file_path)
    
    return JSONResponse(content=bird_counts, media_type="application/json")

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000,
                reload=True,)
