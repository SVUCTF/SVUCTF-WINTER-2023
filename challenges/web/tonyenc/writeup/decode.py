tonyenc_key = bytearray(
    b"\xe0\x87\xf9\x93\x12\x97\x16\xda\x0a\x58\xf8\xc8\xfb\x5e\xf1\x41\xd6\x85\x11\x54\x0e\xd7\xec\x14\x74\x62\xb5\x49"
)

with open("index.php", "rb") as f:
    f.seek(20)
    data = bytearray(f.read())

v2 = 0
for i in range(len(data)):
    if i & 1:
        v2 = (i + v2 + tonyenc_key[v2]) % 0x1C
        data[i] = tonyenc_key[v2] ^ data[i]
        data[i] ^= 0xFF

print(data.decode())
