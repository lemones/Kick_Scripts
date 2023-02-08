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
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0', 'Host': 'kick.com'}

try:
    request = httpx.Client()
    response = request.get(url, headers=headers).json()
    print(f"{response['playback_url']}") if response['livestream'] != None else exit()

except Exception as e:
    # If not working with httpx, use cloudscraper.
    # This is bad practice! But works...
    try:
        import cloudscraper
        scraper = cloudscraper.create_scraper()
        r = scraper.get(url).text 
        y = json.loads(r)
        print(f"{y['playback_url']}") if y['livestream'] != None else exit()
    except Exception as e:
        print(e)
    #exit()