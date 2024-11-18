from qrcode import QRCode
from io import BytesIO
import logging


def generate_qr_code(url, size, padding, color, bgcolor) -> bytes | bool:
    try:
        qr = QRCode(box_size=size, border=padding, mask_pattern=1)
        qr.add_data(url)
        image = qr.make_image(fill_color=color, back_color=bgcolor)

        qr_stream = BytesIO()
        
        try:
            image.save(qr_stream, "PNG")
            return qr_stream.getvalue()
        finally:
            qr_stream.close()
        
    except Exception as e:
        logging.error(f"Error in generating QR: {e}")
        return False
