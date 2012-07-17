from setuptools import setup
import findfiles

requirements = [
]

setup(
    name="findfiles",
    version=findfiles.__version__,
    author="Robby Ranshous",
    author_email="rranshous@gmail.com",
    description="simple iterator for finding files on disk",
    keywords="find",
    url="https://github.com/rranshous/findfiles",
    py_modules=["findfiles"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    install_requires=requirements,
)
