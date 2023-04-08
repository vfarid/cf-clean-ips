import time
import json

result = {
  "last_update": time.strftime("%Y-%m-%d %H:%M"),
  "ipv4": {},
  "ipv6": {}
}

print(json.dumps(result, indent=4))
