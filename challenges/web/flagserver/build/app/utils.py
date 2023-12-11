import os
import random
import secrets
import string
from io import BytesIO
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont


def random_code(length: int) -> str:
    code_list = random.sample(string.digits + string.ascii_letters, length)
    code = "".join(code_list)
    return code


def random_password() -> str:
    return secrets.token_hex(16)


def captcha_image(key: str) -> Tuple[str, BytesIO]:
    font_size, font_num = 48, 5

    random.seed(key)

    font_path = os.path.join(os.path.dirname(__file__), "assets/Vera.ttf")
    font = ImageFont.truetype(font_path, font_size)

    text = gettext(font_num)
    size = getsize(font, text)
    size = (int(size[0] * 1.1), int(size[1] * 1.2))

    image = Image.new(mode="RGB", size=size, color="#ffffff")

    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font, fill="#609b8a")

    noise_dots(draw, image)

    io = BytesIO()
    image.save(io, "JPEG")
    io.seek(0)

    return text, io


def getsize(font: FreeTypeFont, text: str) -> Tuple[int, int]:
    _top, _left, _right, _bottom = font.getbbox(text)
    return _right - _left, _bottom - _top


def gettext(length: int) -> str:
    source = string.digits + string.ascii_uppercase
    text = "".join(random.sample(source, length))
    return text


def noise_dots(draw: ImageDraw, image: Image) -> ImageDraw:
    size = image.size
    for p in range(int(size[0] * size[1] * 0.1)):
        draw.point(
            (random.randint(0, size[0]), random.randint(0, size[1])),
            fill="#609b8a",
        )
    return draw
