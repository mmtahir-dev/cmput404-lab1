import requests
print(requests.__version__)
print(requests.get("https://www.google.com/"))
link="https://raw.githubusercontent.com/mmtahir-dev/cmput404-lab1/master/lab1.py"
r=requests.get(link)
print(r.text)
