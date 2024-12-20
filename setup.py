from setuptools import find_packages,setup
from typing import List

# function to get requirements automatically in SETUP

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
    
setup(

    name='mlproject',
    version='0.0.1',
    author='Azhar',
    author_email='azharuddin.10121995@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)    
