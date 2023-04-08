import time
import json
import dns
import dns.resolver

result = {
  "last_update": time.strftime("%Y-%m-%d %H:%M"),
  "ipv4": {},
  "ipv6": {}
}

provider = "cloudflare.com"
ipv4_result = dns.resolver.resolve(provider, "A")

for ipv4 in ipv4_result:
    result.ipv4.append({"ip": ipv4.to_text(), "provider": provider})

print(json.dumps(result, indent=4))
