from setuptools import setup
import find_files

requirements = [
]

setup(
    name="findfiles",
    version=find_files.__version__,
    author="Robby Ranshous",
    author_email="rranshous@gmail.com",
    description="simple iterator for finding files on disk",
    keywords="find",
    url="https://github.com/rranshous/findfiles",
    py_modules=["find_files"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    install_requires=requirements,
)
