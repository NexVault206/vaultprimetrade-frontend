import re

with open('bitswap_deposit.html', 'r') as f:
    content = f.read()

# Step 1: Remove XRP, LTC, USDT_SOL objects entirely (id through closing "},")
remove_ids = ['xrp', 'ltc', 'usdt_sol']
removed = 0
for rid in remove_ids:
    pattern = re.compile(
        r"[ \t]*\{\s*id: '" + rid + r"',.*?\n[ \t]*\},\n",
        re.DOTALL
    )
    new_content, n = pattern.subn('', content, count=1)
    if n == 1:
        content = new_content
        removed += 1
        print(f"✅ Removed '{rid}' block")
    else:
        print(f"⚠️ '{rid}' block not matched — skipped")

# Step 2: Set wallet addresses for the 8 confirmed assets
addresses = {
    'eth': '0x6280C0c8964c6aD383F42c832EEf4284dB3064D2',
    'bnb': '0x6280C0c8964c6aD383F42c832EEf4284dB3064D2',
    'btc': 'bc1qvsgf8m84up6mlg9gxx853ez35064d5tl6xpszs',
    'sol': '2vT5nH6LdPqnfZHyVhzvvr3GjeSF6ukBm1E7XEReTCF6',
    'usdc_erc': '0x6280C0c8964c6aD383F42c832EEf4284dB3064D2',
    'usdt_erc': '0x6280C0c8964c6aD383F42c832EEf4284dB3064D2',
    'usdt_trc': 'TNptL5kEyfiKTK8u6ybChS81UcBXyKUzFM',
    'usdt_bep': '0x6280C0c8964c6aD383F42c832EEf4284dB3064D2',
}

set_count = 0
for cid, addr in addresses.items():
    pattern = re.compile(
        r"(id: '" + cid + r"',.*?address: ')[^']*(',)",
        re.DOTALL
    )
    new_content, n = pattern.subn(r"\g<1>" + addr + r"\g<2>", content, count=1)
    if n == 1:
        content = new_content
        set_count += 1
        print(f"✅ Set address for '{cid}'")
    else:
        print(f"⚠️ '{cid}' address not matched — skipped")

print(f"\nRemoved {removed}/3, addresses set {set_count}/8")

if removed == 3 and set_count == 8:
    with open('bitswap_deposit.html', 'w') as f:
        f.write(content)
    print("✅ File updated successfully.")
else:
    print("⚠️ Not all changes applied — file left untouched. Review above.")
