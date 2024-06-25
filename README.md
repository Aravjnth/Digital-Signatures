Digital Signatures

## Overview

The Digital Signatures project is a Python-based tool designed to create and verify digital signatures. Digital signatures provide a way to ensure the authenticity and integrity of digital messages or documents. This tool uses cryptographic algorithms to generate and verify signatures, making it useful for secure communications and data integrity checks.

## Features

- Generate digital signatures using private keys.
- Verify digital signatures using public keys.
- Supports various cryptographic algorithms (e.g., RSA, DSA).
- Easy-to-use command-line interface.
- Secure key management.

## Requirements

- Python 3.x
- `cryptography` library

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Aravjnth/Digital-Signatures.git
    cd digital-signatures
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the tool to generate a digital signature:
    ```bash
    python digital_signatures.py -m sign -f <file> -k <private-key>
    ```

2. Run the tool to verify a digital signature:
    ```bash
    python digital_signatures.py -m verify -f <file> -s <signature> -k <public-key>
    ```

    Replace `<file>`, `<private-key>`, `<signature>`, and `<public-key>` with the actual values.

### Example

Generate a digital signature for a file using a private key:

```bash
python digital_signatures.py -m sign -f document.txt -k private_key.pem
```

Verify a digital signature for a file using a public key:

```bash
python digital_signatures.py -m verify -f document.txt -s signature.sig -k public_key.pem
```

## Options

- `-m, --mode`: Mode of operation (sign or verify).
- `-f, --file`: Path to the file to be signed or verified.
- `-k, --key`: Path to the private key (for signing) or public key (for verification).
- `-s, --signature`: Path to the signature file (required for verification).

## Legal Disclaimer

This tool is intended for educational purposes and ethical use only. Unauthorized use of this tool to sign or verify documents without proper authorization is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact me at www.linkedin.com/in/aravinth-aj
