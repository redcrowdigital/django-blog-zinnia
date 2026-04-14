"""Setup script of django-blog-zinnia"""
from setuptools import find_packages
from setuptools import setup

import zinnia

setup(
    dependency_links=[
        "git+https://github.com/arrobalytics/django-tagging.git@027eb90c88ad2d4aead4f50bbbd8d6f0b1678954#egg=django-tagging",
        "git+https://github.com/arrobalytics/django-xmlrpc.git@6cf59c555b207de7ecec75ac962751e8245cf8c9#egg=django-xmlrpc",
        "git+https://github.com/arrobalytics/mots-vides.git@eaeccf73bdb415d0c5559ccd74de360b37a2bbac#egg=mots-vides",
    ],
    name="django-blog-zinnia",
    version=zinnia.__version__,
    description="A clear and powerful weblog application powered with Django",
    long_description="\n".join([open("README.rst").read(), open("CHANGELOG").read()]),
    keywords="django, blog, weblog, zinnia, post, news",
    author=zinnia.__author__,
    author_email=zinnia.__email__,
    url=zinnia.__url__,
    packages=find_packages(exclude=["demo"]),
    classifiers=[
        "Framework :: Django",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license=zinnia.__license__,
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "beautifulsoup4>=4.10.0",
        "django>=5.2,<6.0",
        "django-contrib-comments>=2.2",
        "django-mptt>=0.16",
        "html5lib>=1.1",
        "markdown>=3.3.6",
        "pillow>=10.0",
        "pyparsing>=3.0.6",
        "regex>=2021.11.10",
        "soupsieve>=2.3.1",
        "textile>=4.0.2",
        "webencodings>=0.5.1",
    ],
)
