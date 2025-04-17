from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:

    requirements=[]

    with open(file_path) as req:
        requirements = req.readlines()
        requirements = [token.replace("/n","") for token in requirements]
        
        return requirements


setup(
    name="end-to-end-ml",
    version="0.0.1",
    author="faseeh",
    author_email="haidermuhammadfaseeeh@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('Requirements.txt')
)