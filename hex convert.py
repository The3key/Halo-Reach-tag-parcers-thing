import os

def hexdump(file, output):
    with open(file,'rb') as raw,  open(output,'w') as out:
        offset = 0
        while True:
            chunk = raw.read(16)
            if not chunk:
                break
            if chunk == b'\x00' * len(chunk):
                print("{SKIPPED}")
                offset += 16
            if chunk == b'\xcd' * len(chunk):
                print("{CLEAN MEM}")
                offset += 16

            #your
            h_offset = f"{offset:02x}"

            hex_bytes = [f"{b:02x}" for b in chunk]
            #final padding
            hex_bytes += ["   "] * (16 - len(chunk))
            #reverts it back due to the fact that this is in big edian
            #turns it into a readable x86 hex dump for that line
            hex_part1 = " ".join(hex_bytes[:8])
            hex_part2 = " ".join(hex_bytes[8:])
            ascii_c = "".join(chr(b) if 32 <= b <= 126 else " " for b in chunk)

            o = f"{h_offset} {hex_part1} {hex_part2} |{ascii_c}"
            print(o)
            out.write(o + "\n")
            
            offset += 16
            


            
hexdump('danger/ur mom magnum.weapon',"althejxx_out")


