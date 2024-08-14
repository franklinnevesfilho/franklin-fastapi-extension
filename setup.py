from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="franklin_fastapi_extension",
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "mysql-connector-python"
    ],
    include_package_data=True,
    description="This is a FastAPI Extension to simplify the creation process of APIS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Franklin Neves Filho",
    url="https://github.com/franklinnevesfilho/SimpleAPI",
    license="Do What The Fuck You Want To Public License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: WTFPL License",
    ],
    python_requires=">=3.8"
)
