#!/usr/bin/env python3
"""
Caesar Cipher CLI
- Encrypt/Decrypt text using a shift (key)
- Works with stdin, files, or direct text
- Preserves case; non-letters are left unchanged
- Supports brute-force (-B) to try all shifts
"""

import argparse
import sys
from typing import Iterable

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def shift_char(ch: str, k: int) -> str:
    if ch.isalpha():
        base = 'A' if ch.isupper() else 'a'
        # Normalize to 0-25, add shift, wrap with modulo 26, back to char
        return chr((ord(ch) - ord(base) + k) % 26 + ord(base))
    return ch

def transform(text: str, k: int) -> str:
    # k can be negative; modulo handles wrapping
    return "".join(shift_char(c, k) for c in text)

def read_stream(sources: Iterable[str]) -> str:
    if not sources:
        return sys.stdin.read()
    data = []
    for src in sources:
        with open(src, "r", encoding="utf-8", errors="replace") as f:
            data.append(f.read())
    return "\n".join(data)

def main():
    p = argparse.ArgumentParser(
        description="Caesar Cipher: encrypt/decrypt/bruteforce text."
    )
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("-e", "--encrypt", action="store_true", help="Encrypt mode")
    mode.add_argument("-d", "--decrypt", action="store_true", help="Decrypt mode")
    mode.add_argument("-B", "--bruteforce", action="store_true",
                      help="Try all 26 shifts (for unknown key)")

    p.add_argument("-k", "--key", type=int, help="Shift value (0–25). Negative ok.")
    p.add_argument("-t", "--text", help="Text to process (overrides stdin/files)")
    p.add_argument("-i", "--input", nargs="*", metavar="FILE",
                   help="Input file(s). If omitted, reads stdin.")
    p.add_argument("-o", "--output", metavar="FILE",
                   help="Write result to file instead of stdout")

    args = p.parse_args()

    if args.bruteforce:
        source = args.text if args.text is not None else read_stream(args.input)
        out_lines = []
        for k in range(26):
            # In brute force, treat as decrypt guesses (shift = -k)
            guess = transform(source, -k)
            out_lines.append(f"[key={k:02}] {guess}")
        result = "\n".join(out_lines)
    else:
        if args.key is None:
            sys.exit("Error: --key/-k is required for encrypt/decrypt.")
        k = args.key % 26
        # encryption uses +k, decryption uses -k
        eff = k if args.encrypt else -k
        source = args.text if args.text is not None else read_stream(args.input)
        result = transform(source, eff)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(result)

if __name__ == "__main__":
    main()
