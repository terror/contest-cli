import requests

# Gets list of supported sites
def get_sites():
    res = requests.get("https://kontests.net/api/v1/sites")
    print("{}\n{}".format("Supported Sites:", "-"*30))
    for item in res.json():
        print(item[0])
    print("-"*30)