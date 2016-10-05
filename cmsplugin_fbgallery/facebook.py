import logging

import requests

from django.conf import settings
from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured
from django.template import defaultfilters


logger = logging.getLogger(__name__)

try:
    app_id = settings.FB_APP_ID 
    app_secret =  settings.FB_APP_SECRET
except AttributeError:
    raise ImproperlyConfigured('FB_APP_ID and/or FB_APP_SECRET settings are not configured')

facebook_url = 'https://graph.facebook.com/v2.7/%s/photos?access_token=%s&fields=picture,name,source&format=json&method=get'
cache_expires = getattr(settings, 'CACHE_EXPIRES', 30)


def get_photos(album_id):
    cachename = 'fbgallery_cache_' + defaultfilters.slugify(album_id)
    data = None
    if cache_expires > 0:
        data = cache.get(cachename)
    if data is None:
        access_token = app_id + '|' + app_secret
        url = facebook_url % (album_id, access_token)
        
        logger.debug('querying facebook to %s', url)
        
        response = requests.get(url)

        if (response.status_code == 200):
            data = response.json()
            logger.debug(data)

            if cache_expires > 0:
                cache.set(cachename, data, cache_expires*60)
        else:
            logger.warning('error connecting to facebook: %s', response.status_code)
            logger.debug(response.text)

    return data


def display_album(album_id):
    """Display a facebook album

    First check that the album id belongs to the page id specified
    """
    album = get_photos(album_id)
    if album and 'data' in album:
        return album['data']
