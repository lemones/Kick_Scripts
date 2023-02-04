import argparse
import json
import httpx

#: Fetch livestream URL if streamer exist and is live
#    Requires:
#         httpx (emerge -va dev-python/httpx)
#    Usage example:
#         Play trough mpv player
#         $ mpv $(python ./get_playlist.py -s roshtein)

get_args = argparse.ArgumentParser()
get_args.add_argument("-s", "--streamer", required=True)
args = get_args.parse_args()

url = f"https://Kick.com/api/v1/channels/{args.streamer}"
user_agent= "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
headers = {
	'Host': 'kick.com',
	'User-Agent': user_agent
}

try:
    request = httpx.Client()
    response = request.get(url, headers=headers).json()
    print(f"{response['playback_url']}") if response['livestream'] != None else exit()

except Exception as e:
    print(e)
#    exit()

request = httpx.Client()
response = request.get(url, headers=headers)
print(response)
