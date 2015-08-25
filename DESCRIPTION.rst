django-youtube-thumbnail
========================

Quickly pull the highest resolution thumbnail image available for a YouTube video.

Quick Start
-----------

1. Install the package from pypi:

    .. code-block:: bash

        pip install django-youtube-thumbnail

2. Add "youtube_thumbnail" your INSTALLED_APPS:

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            'youtube_thumbnail',
        )

3. Use the provided template tag to get the thumbnail

    .. code-block:: html

        {% load youtube_thumbnail %}
        <img src="{% youtube_thumbnail_url 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' %}">
