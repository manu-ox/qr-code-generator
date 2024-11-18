from fastapi.responses import HTMLResponse
from pathlib import Path
from re import sub


qr_page_content = Path(f"templates/qr.html").read_text()


def get_home_page() -> HTMLResponse:
    """Return the home page."""

    return HTMLResponse(
        Path(f"templates/index.html").read_text(), 
        status_code=200
        )

def get_qr_page(url: str) -> HTMLResponse:
    """Return the QR download page."""

    return HTMLResponse(
        sub(r'{{\s*url\s*}}', url, qr_page_content), 
        status_code=200
        )