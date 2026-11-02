import os
import struct 

def hexdump(file, output, sz):
    with open(file,'rb') as raw,  open(output,'w') as out:
        offset = 0
        hlf= sz//2
        while True:
            chunk = raw.read(sz)
            if not chunk:
                break
            #if chunk == b'\x00' * len(chunk):
            #    print("{SKIPPED}")
            #    offset += 16
            #if chunk == b'\xcd' * len(chunk):
            #    print("{CLEAN MEM}")
            #    offset += 16


        

            hex_bytes = [f"{b:02x}" for b in chunk]
            hex_bytes += [" "] * (sz - len(chunk))
            
            hex_part1 = " ".join(hex_bytes[:hlf])
            hex_part2 = " ".join(hex_bytes[hlf:])
            ascii_c = "".join(chr(b) if 32 <= b <= 126 else " " for b in chunk)

            o = f"{offset:08x} {hex_part1} {hex_part2} |{ascii_c}"
            print(o)
            out.write(o + "\n")
            
            offset += sz
            


            
hexdump('danger/ur mom magnum.weapon',"test_hex", 16)


