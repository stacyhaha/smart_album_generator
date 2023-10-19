from setuptools import setup, find_packages
reqs = [

]

setup(
    name='album',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    package_data={'': ['*.json']},
    package_dir={'': '.'},
    url='https://git.aipp.io/zhanghaipeng/kuaishou_chatbot.git',
    license='MIT',
    author='renjianan, tanghaoran, yanfu, xiangyi',
    zip_safe=True,
    description='smart_ablum back_end',
    install_requires=reqs
)
