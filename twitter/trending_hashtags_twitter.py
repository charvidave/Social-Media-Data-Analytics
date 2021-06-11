import requests
import json

bearer_token = "AAAAAAAAAAAAAAAAAAAAAM47QgEAAAAAlkHbCZivC9DBkX4GTs6rhZRl1bM%3D0wKW1YYhoVCmKf4VLyvuDYIZDsnxEJYH7kLnKxDXf1cgn68jy6"
#url = "https://api.twitter.com/1.1/tweets/search/recent?query="
#twitter_params = "WednesdayMotivation"
#url = url + twitter_params
url = "https://api.twitter.com/1.1/trends/place.json?id=2295411"
#above is trending hashtags in mumbai

#url="https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent"
headers = {"Authorization": "Bearer {}".format(bearer_token)}
response = requests.request("GET", url, headers=headers)
res_json = response.json()

print(res_json)
