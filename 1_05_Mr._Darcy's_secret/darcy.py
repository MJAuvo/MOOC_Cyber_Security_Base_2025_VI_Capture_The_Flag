#!/usr/bin/env python3

# Cipher = (Msg)^e mod N

def encrypted(msg, e=83, n=1829):
    "This function multiplies its parameter by three."
    return (msg**e) % n

def main():
    for msg in range(1, 1000):
        e_msg = encrypted(msg)
        if e_msg == 1151:
            print(f"Msg: {msg} ==> {e_msg}")

if __name__ == "__main__":
    main()