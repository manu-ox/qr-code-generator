from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from urllib import parse
import uvicorn
from utils.generator import generate_qr_code
from utils.responses import get_home_page, get_qr_page



app = FastAPI(
    title="QR Code Generator",
    description="A simple QR code generator",
    version="0.1",
    openapi_url=None,
    docs_url=None,
    redoc_url=None
)

app.mount("/static", StaticFiles(directory="static/"), name="static")

home_page = get_home_page()



@app.get("/qr/")
async def handler_qr(size: int=10, padding: int=2, url: str=None, qrcolor: str="black", bgcolor: str="white"):
    if not url:
        home_page
    
    qr_code = generate_qr_code(url, size, padding, qrcolor, bgcolor)

    if qr_code:
        return Response(
            qr_code,
            media_type="image/png",
            headers={"Content-Disposition": f"attachment; filename=qr.png"},
            status_code=200
        )
    else:
        return Response("QR code generation failed", status_code=500)


@app.get("/")
async def qr(size: int=10, padding: int=2, url: str=None, qrcolor: str="black", bgcolor: str="white"):
    if not url:
        return home_page
    
    return get_qr_page(
        f"/qr/?size={size}&padding={padding}&url={url}&qrcolor={parse.quote(qrcolor)}&bgcolor={parse.quote(bgcolor)}"
    )


@app.get("/{other_routes}/")
async def handler_other_routes(other_routes: str):
    return Response(f"You are in the wrong route!, {other_routes}")


if __name__ == "__main__":
    uvicorn.run(app)