# surton-ip-tools

A collection of Python tools for IP address resolution and network diagnostics. Includes tools for MongoDB Atlas clusters and general hostname resolution.

## Features

### MongoDB Atlas IP Resolver (`get_mongo_cluster_ips.py`)
- Resolves a MongoDB Atlas cluster SRV record to get all associated hostnames
- Resolves each hostname to its IP address
- Outputs a comma-separated list of IPs in `/32` CIDR format

### General IP Resolver (`ip_resolver.py`)
- Resolves any hostname to its IP address(es)
- Supports multiple hostnames in a single command
- Verbose mode shows canonical names
- Outputs IPs in `/32` CIDR format for easy whitelisting

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

### MongoDB Atlas IP Resolver

Get IPs for your MongoDB cluster:

```sh
poetry run python get_mongo_cluster_ips.py <cluster-url>
```

Example:
```sh
poetry run python get_mongo_cluster_ips.py cluster0.mongodb.net
```

Output:
```
34.201.32.85/32, 52.23.45.67/32, ...
```

### General IP Resolver

Resolve any hostname to IP addresses:

```sh
poetry run python ip_resolver.py <hostname>
```

Examples:
```sh
# Single hostname
poetry run python ip_resolver.py google.com

# Multiple hostnames
poetry run python ip_resolver.py google.com amazon.com cloudflare.com

# AWS RDS endpoint
poetry run python ip_resolver.py wvains.cluster-cavfm4tkbkmt.us-east-1.rds.amazonaws.com

# Verbose mode (shows canonical names)
poetry run python ip_resolver.py -v example.com
```

Output formats:
```sh
# Single hostname
23.22.191.219/32

# Multiple hostnames
google.com:
  142.250.80.46/32
amazon.com:
  52.94.236.248/32
  54.239.28.85/32
  205.251.242.103/32

# Verbose mode
Hostname: example.com
Canonical name: example.com
IP addresses:
  - 93.184.215.14/32
```

## License

MIT
