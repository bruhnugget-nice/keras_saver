from setuptools import setup, find_packages

setup(
    name="keras_saver",
    version="0.0.1",
    description='Do you want a GUI for your Keras Image models? Enter in keras_saver, where you can easily build a GUI, along with other cool features!',
    long_description="""
    Welcome to keras_saver!
    """
    author='bruhnugget-nice',
    url='https://github.com/bruhnugget-nice/keras_saver',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["cloudquicklabs1 = src.main:main"]},
)
