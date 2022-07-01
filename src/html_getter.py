import requests

# Expecting for a name to be passed to this module, which is then searched
# for, and the HTML of the resulting webpage is returned.
# We may have to do some funky stuff to get around Cloudflare.

url = "https://nhentai.net/g/85562/"
r = requests.get(url)
print(r.text)
