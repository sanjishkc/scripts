#!/usr/bin/env python3
"""Recursive Base64 Decoder.

A small, friendly tool that decodes text which has been Base64-encoded several
times over. It was built to solve CTF challenges where a flag is hidden under an
unknown number of Base64 layers, but it works for any multi-encoded text.

Just run the script and answer a couple of questions - no command-line flags to
remember.
"""

import base64
import binascii


def decode_once(data):
    """Decode a single Base64 layer. Returns the decoded string, or None on failure."""
    try:
        decoded_bytes = base64.b64decode(data, validate=True)
        return decoded_bytes.decode("utf-8")
    except (binascii.Error, ValueError, UnicodeDecodeError):
        return None


def decode_fixed(data, rounds):
    """Decode exactly `rounds` times, showing progress along the way."""
    for i in range(1, rounds + 1):
        result = decode_once(data)
        if result is None:
            print(f"  Stopped: layer {i} is not valid Base64.")
            return data
        data = result.strip()
        print(f"  Layer {i}: {data}")
    return data


def decode_auto(data):
    """Keep decoding until the text is no longer valid Base64."""
    rounds = 0
    while True:
        result = decode_once(data)
        if result is None:
            break
        data = result.strip()
        rounds += 1
        print(f"  Layer {rounds}: {data}")
    print(f"  Finished after {rounds} layer(s).")
    return data


def ask_choice(question, options):
    """Ask the user to pick one option from a numbered menu."""
    print(question)
    for number, label in options.items():
        print(f"  {number}. {label}")
    while True:
        choice = input("Choice: ").strip()
        if choice in options:
            return choice
        print("  Please enter one of the numbers above.")


def ask_positive_int(question):
    """Ask for a whole number greater than zero."""
    while True:
        answer = input(question).strip()
        if answer.isdigit() and int(answer) > 0:
            return int(answer)
        print("  Please enter a number greater than 0.")


def get_input_text():
    """Let the user paste text or point to a file."""
    source = ask_choice(
        "\nWhere is the encoded text?",
        {"1": "Type or paste it", "2": "Read it from a file"},
    )
    if source == "1":
        return input("Paste the Base64 text: ").strip()

    path = input("File path: ").strip()
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except OSError as error:
        print(f"  Could not open the file: {error}")
        return None


def main():
    print("=" * 45)
    print("        Recursive Base64 Decoder")
    print("=" * 45)

    text = get_input_text()
    if not text:
        print("No text to decode. Exiting.")
        return

    mode = ask_choice(
        "\nHow many times should it decode?",
        {"1": "Keep going until it can't (auto)", "2": "A set number of times"},
    )

    print("\nDecoding...")
    if mode == "1":
        result = decode_auto(text)
    else:
        rounds = ask_positive_int("How many rounds? ")
        result = decode_fixed(text, rounds)

    print("\n" + "-" * 45)
    print("Result:")
    print(result)
    print("-" * 45)

    if input("\nSave the result to a file? (y/n): ").strip().lower() == "y":
        path = input("Save as: ").strip()
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(result)
            print(f"Saved to {path}")
        except OSError as error:
            print(f"Could not save: {error}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled.")
