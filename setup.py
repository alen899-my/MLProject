from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirments(filepath:str)->List[str]:
    """
    this function will return list of requirnments
    """
    requirments=[]
    with open(filepath) as file_object:
        requirments=file_object.readlines()
        requirments=[req.replace("\n","")for req in requirments]
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
    return requirments


setup(
    name='mlproject',
    version='0.0.1',
    author="alen james",
    author_email='alenjames899@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')
)