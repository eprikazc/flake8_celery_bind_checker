from setuptools import setup


setup(
    name="flake8_celery_bind_checker",
    version="0.1.0",
    description="A Flake8 plugin to check that Celery tasks with bind=True include self",
    author="Eugene Prikazchikov",
    author_email="eprikazc@gmail.com",
    license="MIT",
    packages=["flake8_celery_bind_checker"],
    entry_points={
        "flake8.extension": [
            "CBL = flake8_celery_bind_checker.checker:CeleryBindPlugin",
        ],
    },
    install_requires=[
        "flake8",
        "flake8-plugin-utils>=1.3.1",
    ],
)
