from setuptools import setup

setup(
   name='graph',
   version='1.0',
   description='Class graph.',
   license='MIT',
   author='Artem Pilyavin',
   author_email='artempilavin@gmail.com',
   url='https://github.com/JartiX/graph',
   packages=['graph'],
   install_requires=[],
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)