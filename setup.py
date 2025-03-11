from setuptools import setup, find_packages

setup(
   name='graph',
   version='1.0',
   description='Class graph.',
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