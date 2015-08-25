from classytags.core import Tag, Options
from classytags.arguments import Argument
from django import template

from ..api import get_thumbnail_url

register = template.Library()


class YoutubeThumbnailURL(Tag):
    name = 'youtube_thumbnail_url'
    options = Options(
        Argument('url'),
    )

    def render_tag(self, context, url):
        return get_thumbnail_url(url)


register.tag(YoutubeThumbnailURL)
