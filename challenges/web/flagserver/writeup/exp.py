import string
import random
import requests
from PIL import Image

url = "http://127.0.0.1:5000"
session = requests.session()

key = "zzz"
random.seed(key)

resp = session.get(f"{url}/auth/captcha/image/{key}", stream=True)
image = Image.open(resp.raw)

# gettext
random.sample(string.digits + string.ascii_uppercase, 5)

# noise_dots
width, height = image.size
for _ in range(int(width * height * 0.1)):
    random.randint(0, width)
    random.randint(0, height)

# random_code
code_list = random.sample(string.digits + string.ascii_letters, 8)
code = "".join(code_list)

print(code)
