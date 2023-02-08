import requests
def valrank(username, tagline):

    response = requests.get(f"https://api.henrikdev.xyz/valorant/v1/mmr/na/{username}/{tagline}")
    try:
        data = response.json()['data']
        return(data)
    except:
        return('Unranked')
