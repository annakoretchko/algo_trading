import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='automate_finance',
    version='0.01',
    author="Anna Koretchko",
    author_email='annakoretchko@gmail.com',
    description='Automating finance tasks and strategy',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)