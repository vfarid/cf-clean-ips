import time
import json
import dns
import dns.resolver

result = {
  "last_update": time.strftime("%Y-%m-%d %H:%M"),
  "ipv4": [],
  "ipv6": []
}

providers = json.load(open('providers.json'))

for provider in providers:
    # IPv4
    try:
        ipv4_result = dns.resolver.resolve(provider, "A")
        for ipv4 in ipv4_result:
            result["ipv4"].append({
                "ip": ipv4.to_text(),
                "operator": providers[provider],
                "provider": '.'.join(provider.split('.')[1:]),
                "created_at": int(time.time())
            })
    except:
        # Ignore
        ignored = True

    # IPv6
    try:
        ipv6_result = dns.resolver.resolve(provider, "AAAA")
        for ipv6 in ipv6_result:
            result["ipv6"].append({
                "ip": ipv6.to_text(),
                "operator": providers[provider],
                "provider": '.'.join(provider.split('.')[1:]),
                "created_at": int(time.time())
            })
    except:
        # Ignore
        ignored = True

print(json.dumps(result, indent=4))
