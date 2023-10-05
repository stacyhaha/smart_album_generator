from setuptools import setup, find_packages
reqs = [
        "simplex_sdk",
        "simplex_base_model",
        "torch",
        "transformers==4.8.2",
        "eigen-tracing==0.0.3",
        "kg-schema==0.0.3",
        "requests",
        "onnx"
]

setup(
    name='smart_album',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    package_data={'': ['*.json']},
    package_dir={'': '.'},
    url='https://git.aipp.io/zhanghaipeng/kuaishou_chatbot.git',
    license='MIT',
    author='xiangyi',
    author_email='xiangyi@aidigger.com',
    zip_safe=True,
    description='smart_ablum back_end',
    install_requires=reqs
)
