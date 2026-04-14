.. figure:: zinnia/static/zinnia/logo/dbz_logo_text.png
    :scale: 50
    :align: center


Django Blog Zinnia — Internal Fork
===================================

This is an **internally maintained fork** targeting **Django 5.2 LTS** and **Python 3.12**.

Fork lineage
------------

* `Original project`_ by `@Fantomas42`_ — abandoned ~March 2020
* `arrobalytics fork`_ — updated for Django 3/4 compatibility in 2022, subsequently abandoned
* **This repo** — fork of the above, maintained internally for Django 5.2 LTS

Requirements
------------

* Python 3.10+
* Django 5.2 LTS

Installation
============

Add to your ``Pipfile``:

.. code-block:: toml

    django-blog-zinnia = { git = "https://your-internal-git-host/django-blog-zinnia.git" }

Or with pip:

.. code-block:: bash

    pip install git+https://your-internal-git-host/django-blog-zinnia.git

Upgrading an existing database from Django < 5.1
-------------------------------------------------

Migration ``0006`` handles the transition from the deprecated ``index_together``
format to named ``indexes``. Run migrations as normal — it is a no-op for fresh
installations and automatically renames the old auto-generated indexes on
existing databases.

.. code-block:: bash

    python manage.py migrate zinnia


===================================
Django Blog Zinnia
===================================

Simple yet powerful and really extendable application for managing a blog
within your Django Web site.

Zinnia has been made for publishing Weblog entries and designed to do it well.
Basically any feature that can be provided by another reusable app has been
left out — why re-implement something that is already done, reviewed and tested?

Features
========

* Comments
* `Sitemaps`_
* Archives views
* Related entries
* Private entries
* RSS or Atom Feeds
* Tags and categories views
* `Advanced search engine`_
* Prepublication and expiration
* `Custom templates for various contents`_
* Editing in `Markdown`_, `Textile`_ or `reStructuredText`_
* Widgets (Popular entries, Similar entries, ...)
* Admin dashboard
* `MetaWeblog API`_
* Ping Directories
* Ping External links
* `Gravatar`_ support
* Collaborative work
* Tags autocompletion
* `Entry model extendable`_
* Pingback/Trackback support
* `Blogger conversion utility`_
* `WordPress conversion utility`_
* `WYMeditor`_, `TinyMCE`_, `CKEditor`_ and `MarkItUp`_ support
* Efficient database queries
* Ready to use and extendable templates


.. _`Sitemaps`: http://docs.djangoblogzinnia.com/en/latest/getting-started/configuration.html#module-zinnia.sitemaps
.. _`Advanced search engine`: http://docs.djangoblogzinnia.com/en/latest/topics/search_engines.html
.. _`Custom templates for various contents`: http://docs.djangoblogzinnia.com/en/latest/getting-started/configuration.html#templates-for-entries
.. _`Markdown`: http://daringfireball.net/projects/markdown/
.. _`Textile`: http://redcloth.org/hobix.com/textile/
.. _`reStructuredText`: http://docutils.sourceforge.net/rst.html
.. _`MetaWeblog API`: http://www.xmlrpc.com/metaWeblogApi
.. _`Gravatar`: http://gravatar.com/
.. _`Entry model extendable`: http://django-blog-zinnia.rtfd.org/extending-entry
.. _`WYMeditor`: https://github.com/django-blog-zinnia/zinnia-wysiwyg-wymeditor
.. _`TinyMCE`: https://github.com/django-blog-zinnia/zinnia-wysiwyg-tinymce
.. _`CKEditor`: https://github.com/django-blog-zinnia/zinnia-wysiwyg-ckeditor
.. _`MarkItUp`: https://github.com/django-blog-zinnia/zinnia-wysiwyg-markitup
.. _`Blogger conversion utility`: https://github.com/django-blog-zinnia/blogger2zinnia
.. _`WordPress conversion utility`: https://github.com/django-blog-zinnia/wordpress2zinnia
.. _`Original project`: https://github.com/Fantomas42/django-blog-zinnia/
.. _`@Fantomas42`: https://github.com/Fantomas42/
.. _`arrobalytics fork`: https://github.com/arrobalytics/django-blog-zinnia
