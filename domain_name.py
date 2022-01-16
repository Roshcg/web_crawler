from urllib.parse import urlparse


def get_domain_name(url):
    """
    get domain name (example.com)
    :param url:
    :return:
    """
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


def get_sub_domain_name(url):
    """
    get sub domain name (name.ex.com)
    :param url:
    :return:
    """
    try:
        return urlparse(url).netloc
    except:
        return ''
