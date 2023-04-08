import time
import json
import dns
import dns.resolver

class IPInfo:
    def __init__(self, ip, operator, provider, created_at):
        self.ip = ip
        self.operator = operator
        self.provider = provider
        self.created_at = created_at

result = {
  "last_update": time.strftime("%Y-%m-%d %H:%M"),
  "ipv4": [],
  "ipv6": []
}

provider = "cloudflare.com"
operator = "TEST"

ipv4_result = dns.resolver.resolve(provider, "A")

for ipv4 in ipv4_result:
    result.ipv4.append(IPInfo(ipv4.to_text(), operator, provider, int(time.time())))

print(json.dumps(result, indent=4))
