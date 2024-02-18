from fastapi import FastAPI, HTTPException

from domain.exceptions.line_index_beyond_eof_error import LineIndexBeyondEOFError
from application.services.text_file_service import TextFileService

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Tiago Peres' approach to Salsify Line Server Problem"}


@app.get("/lines/{line_index}")
async def read_line(line_index: int):
    """
    Endpoint to serve individual lines of the text file.
    """
    if line_index < 0:
        raise HTTPException(status_code=400, detail="Line index must be non-negative")
    try:
        line_text = TextFileService().get_line(line_index)
        if not line_text:
            raise LineIndexBeyondEOFError("Line index is beyond the end of the file")
        return {"line_text": line_text}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))  # File not found
    except IOError as e:
        raise HTTPException(status_code=500, detail=str(e))  # I/O error
    except LineIndexBeyondEOFError as e:
        raise HTTPException(status_code=413, detail=str(e))  # Line index is beyond the end of the file
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
