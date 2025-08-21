import os

def r():
    addr = (
        hex(
            int(input("Enter address: "), 16)
            + 2
            + (int(input("Enter relative address: "), 16) * 2)
        )
        .replace("0x", "00")
        .upper()
    )
    print(addr)
    os.system("wl-copy " + addr)

while 1:
    r()