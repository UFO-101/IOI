from setuptools import setup, find_packages

setup(
    name="easy_transformer",
    version="0.1.0",
    packages=find_packages(),
    license="LICENSE",
    description="An implementation of transformers tailored for mechanistic interpretability.",
    long_description=open("README.md").read(),
    install_requires=[
        "einops",
        "numpy",
        "torch",
        "datasets",
        "transformers",
        "tqdm",
        "pandas",
        "datasets",
        "wandb",
        "fancy_einsum",
        "matplotlib",
        "IPython",
    ],
)
