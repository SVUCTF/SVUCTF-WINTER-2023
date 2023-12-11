import os
import secrets


class Config(object):
    SECRET_KEY = secrets.token_hex(16)
    FLAG = os.getenv("GZCTF_FLAG", "flag{fake_flag}")
