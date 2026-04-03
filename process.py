import random

INPUT_FILE = "original.txt"
OUTPUT_FILE = "vless.txt"
FLAG_TO_REMOVE = "%F0%9F%87%B7%F0%9F%87%BA"

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    filtered = [line for line in lines if FLAG_TO_REMOVE not in line]

    random.shuffle(filtered)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(filtered)

if __name__ == "__main__":
    main()
