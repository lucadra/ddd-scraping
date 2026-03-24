"""
Encoding Demo: What happens when you decode text with the wrong encoding?

Takes a text file as input, reads its raw bytes, and decodes them using
UTF-8, CP1252 (ANSI), and ISO-8859-1 — writing each result to a separate file.

Usage:
    python encoding_demo.py <path_to_file.txt>
"""

import sys
import os

ENCODINGS = ["utf-8", "cp1252", "iso-8859-1"]


def main():
    if len(sys.argv) != 2:
        print("Usage: python encoding_demo.py <path_to_file.txt>")
        sys.exit(1)

    input_path = sys.argv[1]
    raw_bytes = open(input_path, "rb").read()

    # Strip extension to build output names
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_dir = os.path.dirname(os.path.abspath(__file__))

    for encoding in ENCODINGS:
        # Use a filesystem-friendly name (e.g. cp1252 instead of keeping as-is)
        safe_name = encoding.replace("-", "")
        output_path = os.path.join(output_dir, f"{base_name}_{safe_name}.txt")

        try:
            decoded = raw_bytes.decode(encoding, errors="replace")
        except Exception as e:
            print(f"Error decoding as {encoding}: {e}")
            continue

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(decoded)

        print(f"Written: {output_path}")


if __name__ == "__main__":
    main()
