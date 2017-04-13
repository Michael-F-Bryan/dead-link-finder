import requests
import re
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

def is_login_failed(soup):
    """
    Checks for an error message box(class aui-message-error).
    If present, this means login failed
    """
    target_class = 'aui-message-error'
    return soup.find(class_=target_class) is not None


def login(client, url, username, password):
    """
    It logs into confluence!
        
    It creates a payload dictionary (containing username, password and other random crap)
    and then posts it into confluences login page. It then inspects the result and if it 
    was a failed attempt it will throw an Exception.
    """
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
    
    if url.hostname is not None and url.hostname != '134.7.57.175':
        return False
    
    if url.port is not None and url.port != 8090:
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



