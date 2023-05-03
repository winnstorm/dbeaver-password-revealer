# DBeaver File Decryption

This Python script allows you to decrypt DBeaver file `credentials-config.json` and extract user and password information. It utilizes the OpenSSL library for decryption.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   
```
git clone https://github.com/your-username/dbeaver-file-decryption.git
```


2. Install the required Python packages:


```
pip install -r requirements.txt
```


3. Download the OpenSSL executable:

- **Windows:** Download the OpenSSL executable for Windows from the following link: [OpenSSL for Windows](https://www.openssl.org/community/binaries.html) and save it in the same directory as the Python script.

- **Other Operating Systems:** Install OpenSSL using your package manager or follow the official instructions.

## Usage

1. Run the script:


2. The GUI window will appear.

3. Click the "Select File" button and choose the `credentials-config.json` file you want to decrypt.

4. Click the "Execute Command" button to decrypt the file.

5. The decrypted user and password information will be displayed in the "Decrypted Result" box.

6. Copy the required information from the "Decrypted Result" box.

7. If you want to select a different file, click the "Reset Selection" button.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
