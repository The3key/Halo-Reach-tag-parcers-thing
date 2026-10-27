
def reversi(file, out):
    with open(file, 'r') as hex_d, open(out, 'wb') as bin_o:
        offset = 0

        for line in hex_d:
            line = line.strip()

            hex_sec = line.split('|')[0].strip()

            tokens = hex_sec.split()
            if not tokens:
                continue

            line_offset = int(tokens[0], 16)

            if line_offset > offset:
                missing_bytes = line_offset - offset
                bin_o.write(b'\x00' * missing_bytes)
                offset = line_offset

            b_strings = tokens[1:]

            chunk_bytes = bytearray()
            for b_str in b_strings:
                chunk_bytes.append(int(b_str, 16))

            bin_o.write(chunk_bytes)

            offset += len(chunk_bytes)

reversi("hex_out", "danger/magnum.weapon")

