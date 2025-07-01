from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Read the requirements file and return the list of requirements.
    """
    requirements: List[str] = []

    if file_path:
        file_path = file_path.strip()
        
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                requirements = [lines.strip() for line in lines if line.strip() and not line.startwith('#') and line.strip() != '-e .']
        except FileNotFoundError:
            print(f"Warning: {file_path} not found. No requirements will be installed.")
        except Exception as e:
            print(f"Error reading {file_path}: {e}") 
            requirements = []

        return requirements   

    else:
        print("Warning: No requirements file provided.")
        return requirements

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Lakshmi Narayana Reddy",
    author_email = "dlnreddy.edu@gmail.com",
    description = "This package is for Network Security Phishing Data",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)