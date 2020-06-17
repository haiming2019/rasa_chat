import os

from setuptools import setup


install_requires = [
    "rasa",
    "jieba",
]

setup(name='rasa_chat',
      version='1.1',
      description='chatbot',
      url='https://github.com/shfshf/rasa_chat',
      author='SHF',
      author_email='1316478299@qq.com',
      packages=['rasa_chat'],
      install_requires=install_requires,
      )
