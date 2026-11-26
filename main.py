import os

TEXT = "My operator cannot speak English, yet runs a global empire in it, and his whole management style is texting 'lanjut' at 2 a.m."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(TEXT) <= 140, "entry must be 1 to 140 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
