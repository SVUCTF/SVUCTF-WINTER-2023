gift = "#70#77#67#68#127#86#50#105#124#104#45#120#83#74#66#73#100#78#116#35#70#74#113#120#119#125#69#80#45#121#109#98"
flag = ""

for index, char in enumerate(gift.split("#")[1:]):
    char_code = int(char)
    char_code ^= index
    flag += chr(char_code).swapcase()

print(flag)
