from qr_app import QrApp
from aiohttp.web import Request, Response
from pathlib import Path
from qr_app import utils


@QrApp.routes.get('/')
async def home(request: Request):
    """Render the home page."""

    homepage = Path(f"qr_app/templates/index.html").read_text()
    return Response(text=homepage, content_type='text/html')


@QrApp.routes.post('/generate/')
async def generator(request: Request):
    """Generate a QR code based on the provided text and design and return image as Response."""

    request_data = await request.post()
    qr_code = utils.generate_qr(
        content=request_data.get('content'),
        size=int(request_data.get('size', default=10)),
        padding=int(request_data.get('padding', default=1)),
        color=request_data.get('qrcolor', default='black'),
        bgcolor=request_data.get('bgcolor', default='white'),
        design=request_data.get('design', default='square')
    )

    if qr_code:
        return Response(
            body=qr_code,
            content_type="image/png",
            headers={"Content-Type: image/png;Content-Disposition": f"inline; filename=qr.png"},
            status=200
        )
    else:
        return Response("QR code generation failed", status_code=500)