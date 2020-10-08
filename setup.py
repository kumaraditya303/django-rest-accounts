from setuptools import setup, find_packages
from accounts import __version__

setup(
    name="django-accounts",
    version=__version__,
    license = "MIT",
    author="Kumar Aditya",
    author_email="@kumaraditya303",
    description="A reusable Django Accounts apps built on Django Rest Framework for fast REST development.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kumaraditya303/Django-Accounts",
    packages=find_packages(),
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Django>=3.0",
        "djangorestframework>=3.0",
        "pillow>=7.2.0",
    ],
)