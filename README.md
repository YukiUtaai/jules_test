# QR Code Generator

This is a simple command-line tool to generate QR codes from a given string or URL.

## Installation

1. Clone this repository.
2. Install the required libraries:
   ```bash
   pip install qrcode[pil]
   ```

## Usage

You can generate a QR code by running the `main.py` script.

### Basic Usage

Provide the data you want to encode as an argument:

```bash
python main.py "Your data here"
```

This will generate a `qrcode.png` file in the same directory.

### Specify Output File

You can specify the output file name using the `-o` or `--output` option:

```bash
python main.py "https://www.example.com" -o example_qr.png
```

This will create a QR code for "https://www.example.com" and save it as `example_qr.png`.
