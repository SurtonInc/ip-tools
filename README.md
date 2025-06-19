# surton-ip-tools

A simple Python tool to extract all IP addresses for a MongoDB Atlas cluster by resolving its SRV DNS records. Useful for network whitelisting or diagnostics.

## Features

- Resolves a MongoDB Atlas cluster SRV record to get all associated hostnames
- Resolves each hostname to its IP address
- Outputs a comma-separated list of IPs in `/32` CIDR format

## Requirements

- Python 3.12+
- [Poetry](https://python-poetry.org/) for dependency management

## Installation

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd ip-tools
   ```
2. Install dependencies with Poetry:
   ```sh
   poetry install
   ```

## Usage

Run the script to get the IPs for your MongoDB cluster:

```sh
poetry run python get_mongo_cluster_ips.py <cluster-url>
```

Replace `<cluster-url>` with your MongoDB Atlas cluster URL, e.g.:

```sh
poetry run python get_mongo_cluster_ips.py cluster0.mongodb.net
```

**Output:**
A comma-separated list of IP addresses in `/32` format, suitable for whitelisting.

## Example

```
poetry run python get_mongo_cluster_ips.py cluster0.mongodb.net
```

Output:

```
34.201.32.85/32, 52.23.45.67/32, ...
```

## License

MIT
