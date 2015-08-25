import pafy
import re

from django.core.cache import cache


def get_pafy(url):
    """Generate a pafy object to pull thumbnail images.

    :param str url: The URL to the youtube video.

    """
    is_playlist = "/videoseries" in url

    if is_playlist:
        videos = pafy.get_playlist(url)
        if len(videos['items']):
            return videos['items'][0]['pafy']

    return pafy.new(url)


def get_thumbnail_url(video_url):
    """Use the gdata API to get the thumbnail image.

    If the django cache is enabled, the values are cached using a key of
    `youtube_thumbnail:{video_url}`. If the request could not be made, a
    blank image is used.

    :param str video_url: The URL to the video on youtube.
    :returns: The URL to the best thumbnail available. The returned URL
              will be protocol relative (e.g. //youtube.com/...)


    """
    cache_key = "youtube_thumbnail:{0}".format(video_url)

    url = cache.get(cache_key)
    if not url:
        try:
            video = get_pafy(video_url)

            if video:
                url = video.bigthumbhd or video.bigthumb or video.thumb
                cache.set(cache_key, url)
            else:
                url = ""
        except:
            url = ""

    return re.sub(r'(^https?://)', '//', url)
