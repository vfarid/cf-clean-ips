import time
import json
import dns
import dns.resolver


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

print("Last Update: " + time.strftime("%Y-%m-%d %H:%M"))

print("")
print("IPv4:")
for provider in providers:
    try:
        ipv4_result = dns.resolver.resolve(provider, "A")
        for ipv4 in ipv4_result:
            print(f"  - {ipv4.to_text():15s}    {providers[provider]:5s}    {provider}    {int(time.time())}")
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
            print(f"  - {ipv4.to_text():32s}    {providers[provider]:5s}    {provider}    {int(time.time())}")
    except:
        # Ignore
        ignored = True
