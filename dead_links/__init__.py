
# coding: utf-8

import requests
import re
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

url = 'http://xxx.x.xxx.xxx:XXXX'  
 
#Put your IP address or url for your confluence server here.
#Don't forget to specify port number if required!

def is_login_failed(soup):

#Checks for an error message box(class aui-message-error).
#If present, this means login failed

    target_class = 'aui-message-error'
    return soup.find(class_=target_class) is not None

def login(client, username, password):

#It logs into confluence!
    
#It creates a payload dictionary (containing username, password and other random crap)
#and then posts it into confluences login page. It then inspects the result and if it 
#was a failed attempt it will throw an Exception.
 
    login_url = url + '/dologin.action'
    payload = {
        'os_username': username,
        'os_password': password,
        'login': 'Log in',
        'os_destination': '/index.action',
    }

    response = client.post(login_url, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if is_login_failed(soup):
        raise Exception('login failed')

def should_follow_link(href):
    if href.startswith('#'):
        return False
    
    url = urlparse(href)
    if url.scheme == 'https':
        return False
    
    if url.hostname is not None and url.hostname != 'xxx.x.xx.xxx':
        return False
    
    if url.port is not None and url.port !=XXXX:
        return False
    
    if url.path.startswith('/download/attachments/'):
        return False
    
    return True

def get_links_on_page(soup):
    links_to_check = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if href is None:
            continue

        if should_follow_link(href):
            links_to_check.append(href)

    return links_to_check


client = requests.Session()
login(client, 'username','password')

r = client.get('http://xxx.x.xx.xxx:XXXX/display/random-page/2017+Event+Random+Page')
soup = BeautifulSoup(r.text, 'html.parser')

#We can now pick a page on our confluence server to index
 
inputs = [
    ('/display/~J.Doe', True),
    ('/download/attachments/4653456/2017-event-day-page-flyer.pub?version=1&modificationDate=174500292323&api=v2', False),
    ('#', False), 
    ('http://xxx.x.xx.xxx:XXXX/display/~D.White', True),
    ('http://xxx.x.xx.xxx:XXXX', False),
    ('http://xxx.x.xx.xxx:XXXX/display/~J.Doe', False),
    ('/display/yourpage/2017+Random+Fundraiser+Day+Review', True),
    ('http://www.atlassian.com/c/conf/17470', False),
    ('http://www.google.com', False)
]

#We now wish to give our seive a set of training data for refinement of
#our exclusion criteria. This will ensure we only obtain the dead links we're looking for.
 
for (src, should_be) in inputs:
    got = should_follow_link(src)
    if got != should_be:
        print('Link "{}", expected "{}" and got "{}" '.format(src, should_be, got))

  #another checker to make sure our training data matches up with what we want
