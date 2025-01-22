from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requires(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements

setup(
    name='MLPROJECT',
    version='0.0.1',
    author='SrinivasaReddy-Avuluri',
    author_email='srinivasareddyavuluri14@gmail.com',
    packages=find_packages(),
    install_requires=get_requires('requirements.txt')
)