import os, json
from urllib.request import urlopen

loop = "Yes"

while loop == "Yes":
    ip = input("Please enter the IP Address here: ")
    url = "http://ip-api.com/json/"
    openurl = urlopen(url + ip)
    data = openurl.read()
    response = json.loads(data)

    print("ISP: " + response["isp"])
    print("Region: " + response["region"])
    print("Region Name: " + response["regionName"])
    print("City: " + response["city"])
    print("Country: " + response["country"])
    print("Zip: " + response["zip"])

    loop = input("Would you like to enter another IP (Enter Yes or No)\n>")
    if loop == "No":
        break

