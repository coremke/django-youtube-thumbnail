import pytest
import six

from django.core.cache import cache

if six.PY3:
    from unittest import mock
else:
    import mock


def test_get_pafy():
    from youtube_thumbnail.api import get_pafy

    with mock.patch('pafy.new') as pafy:
        get_pafy('https://youtube.com/video')
        assert pafy.called_once_with('https://youtube.com/video')


def test_get_pafy_playlist():
    from youtube_thumbnail.api import get_pafy

    with mock.patch('pafy.get_playlist', return_value={'items': [{'pafy': ''}]}) as pafy:
        get_pafy('https://youtube.com/videoseries')
        assert pafy.called_once_with('https://youtube.com/videoseries')


@pytest.mark.parametrize('url,mock_bigthumbhd,mock_bigthumb,mock_thumb,expected', (
    ('//www.youtube.com/embed/mIB9AZdmi0Y?modestbranding=1&showinfo=0&rel=0?wmode=opaque', 'http://test.com/test_big_hd.png', 'http://test.com/test_big.png', 'http://test.com/test_thumb.png', '//test.com/test_big_hd.png'),
    ('//www.youtube.com/embed/videoseries?list=PLZaU9l_NpP84Kg-ZFRT9wuWvfRQxFtTGc', '', '', '//test.com/test3.png', '//test.com/test3.png'),
    ('//www.youtube.com/watch?v=dQw4w9WgXcQ', '', 'https://test.com/test2_big.png', 'https://test.com/test2_thumb.png', '//test.com/test2_big.png'),
))
def test_get_thumbnail_url(url, mock_bigthumbhd, mock_bigthumb, mock_thumb, expected):
    from youtube_thumbnail.api import get_thumbnail_url

    mock_pafy = mock.MagicMock(
        bigthumbhd=mock_bigthumbhd,
        bigthumb=mock_bigthumb,
        thumb=mock_thumb,
    )

    with mock.patch('youtube_thumbnail.api.get_pafy', return_value=mock_pafy):
        assert get_thumbnail_url(url) == expected


def test_get_thumbnail_url_cache():
    from youtube_thumbnail.api import get_thumbnail_url

    mock_pafy = mock.MagicMock(
        bigthumbhd='http://test.com/test.png',
        bigthumb='',
        thumb='',
    )

    url = '//www.youtube.com/watch?v=dQw4w9WgXcQ'
    cache.set('youtube_thumbnail:{}'.format(url), 'http://test-cache.com/test2.png')

    with mock.patch('youtube_thumbnail.api.get_pafy', return_value=mock_pafy):
        assert get_thumbnail_url(url) == '//test-cache.com/test2.png'

    cache.clear()


def test_get_thumbnail_url_unknown():
    from youtube_thumbnail.api import get_thumbnail_url

    with mock.patch('youtube_thumbnail.api.get_pafy', return_value=None):
        assert get_thumbnail_url("//www.youtube.com/watch?v=dQw4w9WgXcQ") == ''


def test_get_thumbnail_url_error():
    from youtube_thumbnail.api import get_thumbnail_url

    with mock.patch('pafy.new', side_effect=Exception("test exception")):
        assert get_thumbnail_url("//www.youtube.com/watch?v=dQw4w9WgXcQ") == ''
