# routers/upload.py

from fastapi import APIRouter, UploadFile
from etl.process_csv import process_csv

router = APIRouter()   # IMPORTANT FIX

@router.post("/upload-csv")
async def upload_csv(file: UploadFile):
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    process_csv(file_path)

    return {"message": "CSV processed successfully"}
