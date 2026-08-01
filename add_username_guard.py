with open('bitswap_dashboard.html', 'r') as f:
    lines = f.readlines()

target_line = "        if (profile) {\n"
found = -1
count = 0
for i, line in enumerate(lines):
    if line == target_line:
        count += 1
        found = i

print(f"Matches found: {count}")

if count == 1:
    indent = "            "
    guard = (
        indent + "if (!profile.username) {\n" +
        indent + "    window.location.href = 'bitswap_choose_username.html';\n" +
        indent + "    return;\n" +
        indent + "}\n"
    )
    lines.insert(found + 1, guard)
    with open('bitswap_dashboard.html', 'w') as f:
        f.writelines(lines)
    print("✅ Username guard inserted.")
else:
    print("⚠️ Expected exactly 1 match — file left untouched.")
