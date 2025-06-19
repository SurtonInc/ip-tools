#!/usr/bin/env python3
import argparse

import dns.resolver


def main(cluster):
    srv_answers = dns.resolver.resolve(f"_mongodb._tcp.{cluster}", "SRV")
    hosts = {str(r.target).rstrip(".") for r in srv_answers}  # type: ignore

    ips = set()
    for host in hosts:
        for a in dns.resolver.resolve(host, "A"):
            ips.add(a.to_text())

    print("/32, ".join(sorted(ips)) + "/32")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get MongoDB cluster IPs from SRV records."
    )
    parser.add_argument(
        "cluster", help="MongoDB cluster name (e.g., 'cluster0.mongodb.net')"
    )
    args = parser.parse_args()

    main(args.cluster)
