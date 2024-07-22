from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    ld = fh.read()


setup(
    name="keras_saver",
    version="0.0.1",
    description='Do you want a GUI for your Keras Image models? Enter in keras_saver, where you can easily build a GUI, along with other cool features!',
    long_description=ld,
    long_description_content_type="text/markdown",
    author='bruhnugget-nice',
    url='https://github.com/bruhnugget-nice/keras_saver',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    install_requires=['tensorflow', 'numpy', 'customtkinter', 'tkinter', 'imageio'],
    entry_points={"console_scripts": ["keras_saver = src.main:main"]},
)
