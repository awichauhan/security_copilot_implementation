from pathlib import Path
from pypdf import PdfReader

def parse_pdf(file_path: str) -> list[dict]:
    """Extract text and source metadata from each non-empty PDF page."""
    path = Path(file_path)
    reader = PdfReader(path)

    documents = []

    # Start numbering from 1 so it matches physical PDF page numbers.
    for page_number, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()

        # Skip pages where no text could be extracted.
        if not text:
            continue

        documents.append({
            "text": text,
            "metadata": {
                "source": path.name,
                "page": page_number,
            },
        })

    return documents

