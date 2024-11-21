# Secret Santa

This Secret Santa tool assigns each participant a gift recipient and provides them with a unique link to view their assignment. You can run it locally, through Docker using the provided `run.sh` script, or set up a reproducible development environment with `nix` and `direnv`.

## Features

- Randomly assigns each participant a recipient, ensuring everyone gives and receives a gift.
- Generates unique, secret links for participants to view their assignment.
- Supports HTTPS for secure link sharing.

## Requirements

- **Python 3.6+**
- **Flask**
- **Docker** (if using `run.sh`)
- **Nix** and **Direnv** (optional, for reproducible development environment)

To install Flask, run:
```bash
pip install flask
```

### Optional Tools for Development

This project offers a reproducible development environment using [`nix`](https://nixos.org/download/) and [`direnv`](https://direnv.net/docs/installation.html). With these, dependencies are managed automatically, making setup simple and consistent.

1. **Install** `nix` and `direnv` by following their respective installation instructions.
2. Run `direnv allow` in the project directory. This will automatically set up the necessary environment.

With `nix` and `direnv`, all dependencies will be configured, and you'll have a consistent development environment ready to go.

## Usage

### Running Directly

Run the Secret Santa tool from the command line, specifying participants and optional server settings.

```bash
python secretsanta.py [options] santas...
```

#### Required Argument

- `santas` - Names of people participating in the Secret Santa event.

#### Optional Arguments

- `--print_host` - Hostname for generated links. Default: `localhost`.
- `--port` - Port for the web server. Default: `80`.
- `--tls-cert` - Path to a TLS certificate for HTTPS.
- `--tls-key` - Path to a TLS key.
- `--seed` - Random seed for reproducible results. Defaults to a random 128-bit seed.

#### Example

To assign Secret Santa participants and run the server on `localhost`, port `5000`:

```bash
python secretsanta.py --print_host "localhost" --port 5000 Alice Bob Charlie
```

This will generate and print unique links for each participant, displaying their Secret Santa assignment when visited.

### Using the `run.sh` Script

The `run.sh` script simplifies deployment by using Docker to create and run a containerized instance of the Secret Santa tool. This script is designed for secure HTTPS deployments with TLS.

#### Usage

Ensure you have a TLS certificate and key, then run the script as follows:

```bash
./run.sh [participants...]
```

#### Environment Variables

The script uses the following environment variables, with default values if not specified:

- `TLS_CERT` - Path to the TLS certificate file. Default: `./cert.pem`.
- `TLS_KEY` - Path to the TLS key file. Default: `./key.pem`.
- `PORT` - The port the web server will use. Default: `42418`.

The script will check that `TLS_CERT` and `TLS_KEY` exist. If not, it will exit with an error.

#### Example

To run the tool with three participants (`Alice`, `Bob`, and `Charlie`), using `cert.pem` and `key.pem` in the current directory, run:

```bash
./run.sh Alice Bob Charlie
```

This command builds a Docker image and starts a containerized web server that listens on the specified port (`42418` by default). Each participant receives a unique link to their assignment page on the secure HTTPS server.

### Output

The tool prints a list of links, one for each participant, displaying their Secret Santa assignment:

```
Alice: https://localhost:42418/<unique_secret>
Bob: https://localhost:42418/<unique_secret>
Charlie: https://localhost:42418/<unique_secret>
```

Each participant can view only their own assignment using their unique link.

## License

This project is open-source and available under the MIT License.
