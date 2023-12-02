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
        '--print_host',
        type=str,
        default="localhost",
        help='Host to run webserver on',
)

parser.add_argument(
        '--port',
        type=int,
        default=80,
        help='Port to run webserver on'
)

parser.add_argument(
        '--tls-cert',
        type=str,
        default=None,
        help='TLS certificate path'
)

parser.add_argument(
        '--tls-key',
        type=str,
        default=None,
        help='TLS key path'
)

parser.add_argument(
        '--seed',
        type=int,
        default=secrets.randbits(128),
        help='Random seed'
)

args = parser.parse_args()

# TLS setup
if args.tls_cert is not None and args.tls_key is not None:
    tls_context = (args.tls_cert, args.tls_key)
else:
    tls_context = 'adhoc'

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
    return f"<html><body><h1>{santa} du bist secret santa von: {dest}</h1></body></html>"

def make_secret():
    alphabet = string.ascii_letters + string.digits
    secret = ''.join(random.choice(alphabet) for i in range(15))
    return secret

def main():
    random.seed(args.seed)
    print(f"Random Seed: {args.seed}")

    santas = args.santas
    random.shuffle(santas)

    to_print = []
    for i, santa in enumerate(santas):
        secret = make_secret()
        dst_santa = santas[ (i+1) % len(santas) ]
        secret_to_santa[secret] = ( santa , dst_santa)
        to_print.append(f"{santa}: https://{args.print_host}:{args.port}/{secret}")

    # print after shuffling
    random.shuffle(to_print)
    for l in to_print:
        print(l)

    # Start Server
    app.run(
        host="0.0.0.0",
        ssl_context=tls_context,
        port=args.port,
    )

if __name__ == "__main__":
    main()
