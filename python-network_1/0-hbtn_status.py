#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    request = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(request) as response:
            html = response.read()
            print('Body response:')
            print('\t- type: {}'.format(type(html)))
            print('\t- content: {}'.format(html))
            print('\t- utf8 content: {}'.format(html.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
