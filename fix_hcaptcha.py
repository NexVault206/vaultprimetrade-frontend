import re

with open('bitswap_createaccount.html', 'r') as f:
    content = f.read()

changes = 0

old_script = '<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>'
new_script = '<script src="https://js.hcaptcha.com/1/api.js" async defer></script>'
n1 = content.count(old_script)
if n1 == 1:
    content = content.replace(old_script, new_script, 1)
    changes += 1
    print("✅ Script tag swapped")
else:
    print(f"⚠️ Script tag matched {n1} times")

old_div = '<div class="cf-turnstile" data-sitekey="YOUR_TURNSTILE_SITE_KEY" data-callback="onTurnstileSuccess" data-theme="dark"></div>'
new_div = '<div class="h-captcha" data-sitekey="83c63a18-007e-4398-b94c-9c7214f4b810" data-callback="onTurnstileSuccess" data-theme="dark"></div>'
n2 = content.count(old_div)
if n2 == 1:
    content = content.replace(old_div, new_div, 1)
    changes += 1
    print("✅ Widget div swapped")
else:
    print(f"⚠️ Widget div matched {n2} times")

if changes == 2:
    with open('bitswap_createaccount.html', 'w') as f:
        f.write(content)
    print("✅ File updated successfully.")
else:
    print("⚠️ Not all changes applied — file left untouched.")
