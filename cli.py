# cli.py
import argparse
from key_manager import load_key
from crypto_utils import encrypt_data, decrypt_data
from file_operations import read_file, write_file

def run():
    parser = argparse.ArgumentParser(description="Simple Encryption Tool")
    parser.add_argument("action", choices=["encrypt", "decrypt"])
    parser.add_argument("input_file")
    parser.add_argument("output_file")

    args = parser.parse_args()
    key = load_key()
    data = read_file(args.input_file)

    if args.action == "encrypt":
        result = encrypt_data(data, key)
    else:
        result = decrypt_data(data, key)

    write_file(args.output_file, result)
    print("Done!")
