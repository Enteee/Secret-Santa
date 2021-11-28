#!/usr/bin/env python
from flask import Flask, abort
import argparse
import random
import secrets
import string

parser = argparse.ArgumentParser(description='Secret Santa')

parser.add_argument(
        'santas',
        type=str,
        nargs='+',
        help='People participating in the secret santa scheme'
)

parser.add_argument(
        '--host',
        type=str,
        default="localhost",
        help='Host to run webserver on',
)

parser.add_argument(
        '--port',
        type=int,
        default=random.randint(1025, 65535),
        help='Port to run webserver on'
)
args = parser.parse_args()

app = Flask(__name__)

secret_to_santa = {}

@app.route("/")
def root():
    return f"Santas: {args.santas}"

@app.route('/<secret>')
def get_secret(secret):
    try:
        santa, dest = secret_to_santa[secret]
    except KeyError:
        abort(404, description="Secret was not found")
    return f"{santa} du bist secret santa von: {dest}"

def make_secret():
    alphabet = string.ascii_letters + string.digits
    secret = ''.join(secrets.choice(alphabet) for i in range(15))
    return secret

def main():
    santas = args.santas
    random.shuffle(santas)

    for i, santa in enumerate(santas):
        secret = make_secret()
        secret_to_santa[secret] = (
            santa ,
            santas[ (i+1) % len(santas) ]
        )
        print(f"{santa}: http://{args.host}:{args.port}/{secret}")

    # Start Server
    app.run(host=args.host, port=args.port)

if __name__ == "__main__":
    main()
