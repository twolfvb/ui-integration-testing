import urlparse
import logging

class Router(object):
    SCHEMA   = 'http'
    NETLOC   = 'localhost:8000'
    PATH     = ''
    PARAMS   = ''
    QUERY    = ''
    FRAGMENT = ''

    @classmethod
    def browse_to(cls, driver, page):
        url = cls.url_to(page.route)
        driver.get(url)

    @classmethod
    def url_to(cls, endpoint):
        base_url = urlparse.urlunparse((
            cls.SCHEMA,
            cls.NETLOC,
            cls.PATH,
            cls.PARAMS,
            cls.QUERY,
            cls.FRAGMENT
        ))
        return base_url + endpoint
