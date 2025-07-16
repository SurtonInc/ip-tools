# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a collection of Python-based IP resolution tools for network diagnostics and whitelisting purposes. The project uses Poetry for dependency management and requires Python 3.12+.

## Key Commands

### Development Setup
```bash
# Install dependencies
poetry install

# Enter Poetry shell (optional)
poetry shell
```

### Running Tools
```bash
# MongoDB Atlas cluster IP resolver
poetry run python get_mongo_cluster_ips.py <cluster-url>
# Example: poetry run python get_mongo_cluster_ips.py cluster0.mongodb.net

# General IP resolver
poetry run python ip_resolver.py <hostname>
poetry run python ip_resolver.py -v <hostname>  # verbose mode with canonical names
# Example: poetry run python ip_resolver.py wvains.cluster-cavfm4tkbkmt.us-east-1.rds.amazonaws.com
```

### Dependency Management
```bash
# Add new dependency
poetry add <package-name>

# Update dependencies
poetry update
```

## Architecture

The codebase consists of two independent Python scripts:

1. **get_mongo_cluster_ips.py** - Resolves MongoDB Atlas SRV records to IP addresses
   - Uses dnspython for SRV lookups
   - Outputs IPs in CIDR /32 format for whitelisting
   - MongoDB-specific DNS resolution logic

2. **ip_resolver.py** - General-purpose hostname to IP resolver
   - Uses Python's socket library
   - Supports multiple hostnames
   - Verbose mode shows canonical names

Both scripts are standalone CLI tools with argparse interfaces. There is no shared code or package structure (package-mode is set to false in pyproject.toml).

## Important Notes

- Always use `poetry run` prefix for all Python commands to ensure the correct virtual environment
- The project has no test suite, linting configuration, or CI/CD setup
- Scripts are designed for direct execution, not as importable modules
- The dnspython dependency is only used by get_mongo_cluster_ips.py