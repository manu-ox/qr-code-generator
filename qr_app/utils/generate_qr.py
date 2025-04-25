from qrcode import QRCode, constants
from qrcode.image.styledpil import StyledPilImage
from io import BytesIO
from qrcode.image.styles.moduledrawers.pil import (
    CircleModuleDrawer,
    VerticalBarsDrawer,
    RoundedModuleDrawer,
    GappedSquareModuleDrawer,
    SquareModuleDrawer,
    HorizontalBarsDrawer
)

import logging


DEFAULT_DESIGN = 'square'
DEFAULT_QR_COLOR = 'black'
DEFAULT_BG_COLOR = 'white'
DEFAULT_SIZE = 10
DEFAULT_PADDING = 1


DESIGN = {
    DEFAULT_DESIGN: SquareModuleDrawer(),
    'gapped-square': GappedSquareModuleDrawer(),
    'circle': CircleModuleDrawer(),
    'rounded': RoundedModuleDrawer(),
    'horizontal-bars': HorizontalBarsDrawer(),
    'vertical-bars': VerticalBarsDrawer()
}


def generate_qr(content, size=DEFAULT_SIZE, padding=DEFAULT_PADDING, color=DEFAULT_QR_COLOR, bgcolor=DEFAULT_BG_COLOR, design=DEFAULT_DESIGN) -> bytes | bool:
    """QR code generator"""

    try:
        qr = QRCode(
            error_correction=constants.ERROR_CORRECT_H,
            box_size=size,
            border=padding
        )

        qr.add_data(content)

        if design == DEFAULT_DESIGN:
            image = qr.make_image(fill_color=color, back_color=bgcolor)
        else:
            image = qr.make_image(image_factory=StyledPilImage, module_drawer=DESIGN.get(design))


        with BytesIO() as stream:
            image.save(stream, format="PNG")
            return stream.getvalue()

        
    except Exception as e:
        logging.error(f"Error in generating QR: {e}")
        return False