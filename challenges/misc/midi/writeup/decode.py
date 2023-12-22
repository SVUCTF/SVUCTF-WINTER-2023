from mido import MidiFile

g_major_scale = [67, 69, 71, 72, 74, 76, 78]
mid = MidiFile("../attachments/G_Major_Jingle_Bells.mid")

flag = ""
temp_charcode = ""

for msg in mid.tracks[2]:
    if msg.type == "note_on":
        index = g_major_scale.index(msg.note)
        temp_charcode += str(index)

    # 当遇到 note_off 并且有缓存的 Charcode
    elif len(temp_charcode) != 0:
        charcode = int(temp_charcode, 7)
        temp_charcode = ""
        flag += chr(charcode)

print(flag)
