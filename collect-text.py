import time
import json
import dns
import dns.resolver

providers = json.load(open('providers.json'))

print("Last Update: " + time.strftime("%Y-%m-%d %H:%M"))

print("")
print("IPv4:")
for provider in providers:
    try:
        ipv4_result = dns.resolver.resolve(provider, "A")
        for ipv4 in ipv4_result:
            print(f"  - {ipv4.to_text():15s}    {providers[provider]:5s}    {'.'.join(provider.split('.')[1:])}    {int(time.time())}")
    except:
        # Ignore
        ignored = True

print("")
print("IPv6:")
for provider in providers:
    # IPv6
    try:
        ipv6_result = dns.resolver.resolve(provider, "AAAA")
        for ipv6 in ipv6_result:
            print(f"  - {ipv4.to_text():32s}    {providers[provider]:5s}    {'.'.join(provider.split('.')[1:])}    {int(time.time())}")
    except:
        # Ignore
        ignored = True
