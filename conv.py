import struct



def parse_weapon_tag(file):
    with open(file, "rb") as t_file:
        raw = t_file.read(4)
        #clean the file, get rid of the null characters and then spit out 
        clean = raw.replace(b"\x00",b"")
        print(clean)
while True:
    with open("hexout", "r"):
        print("prins")

parse_weapon_tag("tags/magnum/magnum.weapon")