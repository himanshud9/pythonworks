from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='browserhistory',
    version='0.1.2',
    author='Himanshu D',
    author_email='himanshud987@gmail.com',
    description="A simple module to extract browsers's history.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/himanshud9/pythonworks',
    py_modules=['browserhistory'],
    platforms=['Linux', 'MacOS', 'Windows'],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Database",
    ],
)
