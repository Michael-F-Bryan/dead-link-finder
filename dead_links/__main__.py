"""
Dead Link Checker

A small program to crawl a website and check that there aren't any dead links.

Usage: 
    dead_links <URL>
"""
import docopt
import requests
from urllib.urlparse
from bs4 import BeautifulSoup


def main(root_url):
    client = requests.Session()
    login(client, root_url, 'username','password')

    r = client.get('http://xxx.x.xx.xxx:XXXX/display/random-page/2017+Event+Random+Page')
    soup = BeautifulSoup(r.text, 'html.parser')

if __name__ == "__main__":
    args = docopt.docopt(__doc__)
    print(args)
    main(args['<URL>'])
