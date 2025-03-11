from setuptools import setup, find_packages

setup(
   name='graph062',
   version='1.1',
   description='Class graph.',
   long_description='Use it in your project where you need a graph construction.\nGitHub: https://github.com/JartiX/graph',
   license='MIT',
   author='Artem Pilyavin',
   author_email='artempilavin@gmail.com',
   url='https://github.com/JartiX/graph',
   packages=find_packages(),
   install_requires=[],
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)