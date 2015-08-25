import six

if six.PY3:
    from unittest import mock
else:
    import mock


def get_template(url):
    from django.template import Template
    return Template("""
        {{% load youtube_thumbnail %}}

        {{% youtube_thumbnail_url '{}' %}}
    """.format(url))


def test_youtube_thumbnail_url(rf):
    from django.template import Context

    mock_pafy = mock.MagicMock(
        bigthumbhd='//youtube.com/test.png',
        bigthumb='',
        thumb='',
    )

    with mock.patch('youtube_thumbnail.api.get_pafy', return_value=mock_pafy):
        t = get_template("https://youtube.com/video...")
        context = Context({'request': rf.get('/')})
        output = t.render(context)

        assert output.strip() == "//youtube.com/test.png"
