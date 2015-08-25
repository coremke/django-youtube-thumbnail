# django-youtube-thumbnail

> Quickly pull the highest resolution thumbnail image available for a YouTube video.

[![Build Status](https://img.shields.io/travis/gsmke/django-youtube-thumbnail/master.svg?style=flat)](https://travis-ci.org/gsmke/django-youtube-thumbnail)
[![Latest Version](https://img.shields.io/pypi/v/django-youtube-thumbnail.svg?style=flat)](https://pypi.python.org/pypi/django-youtube-thumbnail/)

## Quick start

1. Install the package from pypi:

    ```bash
    pip install django-youtube-thumbnail
    ```

2. Add "youtube_thumbnail" your INSTALLED_APPS:

    ```python
    INSTALLED_APPS = (
        ...
        'youtube_thumbnail',
    )
    ```

3. Use the provided template tag to get the thumbnail
```html
{% load youtube_thumbnail %}
<img src="{% youtube_thumbnail_url 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' %}">
```

### Cache

If you have the django cache enabled, thumbnail results will be cached to avoid unnecessary lookups.
