"""
Dead Link Checker

A small program to crawl a website and check that there aren't any dead links.

Usage: 
    dead_links <URL>
"""
import docopt
import requests
from bs4 import BeautifulSoup

from . import login


def main(root_url):
    client = requests.Session()
    login(client, root_url, 'username','password')

    r = client.get('http://xxx.x.xx.xxx:XXXX/display/random-page/2017+Event+Random+Page')
    soup = BeautifulSoup(r.text, 'html.parser')

if __name__ == "__main__":
    args = docopt.docopt(__doc__)
    main(args['<URL>'])
