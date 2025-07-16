#!/usr/bin/env python3

import argparse
import socket
import sys
from typing import List, Tuple


def resolve_hostname(hostname: str) -> List[str]:
    """
    Resolve a hostname to its IP addresses.

    Args:
        hostname: The hostname to resolve

    Returns:
        List of IP addresses
    """
    try:
        # Get address info for the hostname
        addr_info = socket.getaddrinfo(hostname, None)

        # Extract unique IP addresses
        ip_addresses = []
        seen = set()

        for info in addr_info:
            ip = info[4][0]
            if ip not in seen:
                seen.add(ip)
                ip_addresses.append(ip)

        return ip_addresses

    except socket.gaierror as e:
        raise Exception(f"Failed to resolve hostname '{hostname}': {e}")


def get_hostname_info(hostname: str) -> Tuple[str, List[str]]:
    """
    Get the canonical name and IP addresses for a hostname.

    Args:
        hostname: The hostname to query

    Returns:
        Tuple of (canonical_name, list_of_ips)
    """
    try:
        # Try to get the canonical name
        try:
            canonical_name = socket.getfqdn(hostname)
        except Exception:
            canonical_name = hostname

        # Get IP addresses
        ip_addresses = resolve_hostname(hostname)

        return canonical_name, ip_addresses

    except Exception as e:
        raise Exception(f"Error getting info for {hostname}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Resolve hostnames to IP addresses",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s google.com
  %(prog)s wvains.cluster-cavfm4tkbkmt.us-east-1.rds.amazonaws.com
  %(prog)s google.com amazon.com cloudflare.com
  %(prog)s -v example.com
        """,
    )

    parser.add_argument("hostnames", nargs="+", help="One or more hostnames to resolve")

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show additional information (canonical names)",
    )

    args = parser.parse_args()

    # Process each hostname
    for hostname in args.hostnames:
        try:
            if args.verbose:
                canonical_name, ip_addresses = get_hostname_info(hostname)
                print(f"\nHostname: {hostname}")
                if canonical_name != hostname:
                    print(f"Canonical name: {canonical_name}")
                print("IP addresses:")
                for ip in ip_addresses:
                    print(f"  - {ip}/32")
            else:
                ip_addresses = resolve_hostname(hostname)
                if len(args.hostnames) > 1:
                    print(f"{hostname}:")
                for ip in ip_addresses:
                    if len(args.hostnames) > 1:
                        print(f"  {ip}/32")
                    else:
                        print(f"{ip}/32")

        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            if len(args.hostnames) == 1:
                sys.exit(1)


if __name__ == "__main__":
    main()
