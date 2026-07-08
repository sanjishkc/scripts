# Recursive Base64 Decoder

A simple, interactive tool that decodes text which has been Base64-encoded several times over.

It was built to solve CTF challenges where a flag is hidden under an unknown number of Base64 layers, but it works for any text that has been encoded more than once. Just run it and answer a couple of questions. There are no command-line flags to memorize.

## Why

The usual quick fix for these puzzles is a hard-coded loop:

```python
for i in range(50):
    data = base64.b64decode(data)
```

That only works if you already know the number of layers. This tool asks how you'd like to decode instead — either a set number of rounds, or **auto mode**, which keeps going until the text is no longer valid Base64.

## Features

- **Interactive prompts** — no flags to remember; the script walks you through it.
- **Auto mode** — decodes until it can't anymore, so you don't need to know the depth.
- **Fixed rounds** — decode an exact number of times when you do know.
- **Paste or file input** — type the text in, or point it at a file.
- **Step-by-step output** — shows each layer as it's peeled off.
- **Save the result** — optionally write the final output to a file.
- **Graceful errors** — invalid input and bad file paths are handled without a crash.

## Requirements

Python 3.6 or newer. No external packages — everything uses the standard library.

## Installation

```bash
git clone https://github.com/sanjishkc/tools-scripts/Recursive_Base64_Decoder.git
```

## Usage

Run the script and follow the prompts:

```bash
cd Recursive_Base64_Decoder
python3 recursive_base64_decoder.py
```

Example session:

```
=============================================
        Recursive Base64 Decoder
=============================================

Where is the encoded text?
  1. Type or paste it
  2. Read it from a file
Choice: 2
File path: sample_encoded.txt

How many times should it decode?
  1. Keep going until it can't (auto)
  2. A set number of times
Choice: 2
How many rounds? 5

Decoding...
  Layer 1: VlZSR1UxSXlWWHBUV0hCYVRURmFOVmt6Y0VkTmF6QjRUMWRzVDJGc1NtMVhiVFZUVFRKYVVsQlVNRDA9
  Layer 2: VVRGU1IyVXpTWHBaTTFaNVkzcEdNazB4T1dsT2FsSm1XbTVTTTJaUlBUMD0=
  Layer 3: UTFSR2UzSXpZM1Z5Y3pGMk0xOWlOalJmWm5SM2ZRPT0=
  Layer 4: Q1RGe3IzY3VyczF2M19iNjRfZnR3fQ==
  Layer 5: CTF{r3curs1v3_b64_ftw}

---------------------------------------------
Result:
CTF{r3curs1v3_b64_ftw}
---------------------------------------------

Save the result to a file? (y/n): n
```

A ready-made `sample_encoded.txt` (five Base64 layers) is included so you can try the example above right away.

## Directory Structure

```text
Recursive_Base64_Decoder/
├── recursive_base64_decoder.py   # The tool
├── README.md                     # This file
├── sample_encoded.txt            # Example: "CTF{...}" wrapped in 5 Base64 layers
└── sample_output.txt             # Captured example run
```

## Notes

- Auto mode stops as soon as a layer fails to decode — that's your innermost text.
- Fixed mode stops early and tells you if it hits something that isn't valid Base64.
- Press `Ctrl+C` at any time to cancel.

## Disclaimer

This tool is for educational use, CTF practice, and authorized security work only. Decode only data you own or have permission to analyze.

## Future Ideas

- Support for other encodings (Base32, Base85, hex).
- Automatic detection of the encoding used.
