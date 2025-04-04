def main():
    with open("text/alice_in_wonderland.txt", "r", encoding="utf8") as f:
        text = f.read()
    print(f"number words: {len(text.split()):,}")


if __name__ == "__main__":
    main()
