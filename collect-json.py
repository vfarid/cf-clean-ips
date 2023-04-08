import time
import json
import dns
import dns.resolver


result = {
  "last_update": time.strftime("%Y-%m-%d %H:%M"),
  "ipv4": [],
  "ipv6": []
}

providers = {
    "mci.ircf.space": "MCI",
    "mcix.ircf.space": "MCI",
    "mtn.ircf.space": "MTN",
    "mtnx.ircf.space": "MTN",
    "mkh.ircf.space": "MKH",
    "rtl.ircf.space": "RTL",
    "hwb.ircf.space": "HWB",
    "ast.ircf.space": "AST",
    "sht.ircf.space": "SHT",
    "prs.ircf.space": "PRS",
    "mbt.ircf.space": "MBT",
    "ask.ircf.space": "ASK",
    "rsp.ircf.space": "RSP",
    "afn.ircf.space": "AFN",
    "ztl.ircf.space": "ZTL",
    "psm.ircf.space": "PSM",
    "arx.ircf.space": "ARX",
    "smt.ircf.space": "SMT",
    "fnv.ircf.space": "FNV",
    "dbn.ircf.space": "DBN",
    "apt.ircf.space": "APT",
    "mci.amiajoketoyou.lol": "MCI",
    "mtn.amiajoketoyou.lol": "MTN",
}

for provider in providers:
    # IPv4
    try:
        ipv4_result = dns.resolver.resolve(provider, "A")
        for ipv4 in ipv4_result:
            result["ipv4"].append({
                "ip": ipv4.to_text(),
                "operator": providers[provider],
                "provider": provider,
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
                "provider": provider,
                "created_at": int(time.time())
            })
    except:
        # Ignore
        ignored = True

print(json.dumps(result, indent=4))
