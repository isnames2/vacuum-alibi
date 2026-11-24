import os

# The judged text: one line, spoken by the vacuum itself. Keep it verbatim.
LINE = "I left that corner alone because my bump sensor classified the dust bunny as load-bearing, and I don't demolish structures."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
