from typing import List
from mido import Message, MidiFile, MidiTrack


# 与 CyberChef To_Charcode('Space',7) 相同
def to_charcodes_in_base7(input: str) -> List[str]:
    output = []
    for char in input:
        code = ord(char)
        base7_digits = []
        while code > 0:
            remainder = code % 7
            base7_digits.insert(0, str(remainder))
            code //= 7
        output.append("".join(base7_digits))
    return output


# G 大调音阶
# G4 A4 B4 C4 D4 E4 F#4
g_major_scale = [67, 69, 71, 72, 74, 76, 78]

# 源 MIDI 文件，添加新轨道
mid = MidiFile("./jingle-bells-keyboard.mid")
track = MidiTrack()
mid.tracks.append(track)

ticks_per_charcode = mid.ticks_per_beat

# 延迟八个小节
ticks_delay = mid.ticks_per_beat * 2 * 8
track.append(Message("note_off", note=0, velocity=0, time=ticks_delay))


# 获得 Flag 的七进制 Charcode
flag = "flag{3NJoy_thE_D1ScoRdANt_note5}"
flag_charcodes = to_charcodes_in_base7(flag)
print(flag_charcodes)

# 将七进制 Charcode 写入轨道
for charcode in flag_charcodes:
    for digit in charcode:
        note = g_major_scale[int(digit)]
        velocity = 64
        track.append(
            Message("note_on", note=note, velocity=velocity, time=ticks_per_charcode)
        )
    track.append(Message("note_off", note=0, velocity=0, time=0))

mid.save("G_Major_Jingle_Bells.mid")
