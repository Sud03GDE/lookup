import requests
import subprocess

subprocess.run (["clear"])

lookup=input ("+Lookup ip info: ")

r=requests.get ("https://ipinfo.io/" + lookup)

print (r.text)