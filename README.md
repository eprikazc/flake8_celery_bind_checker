# flake8_celery_bind_checker

The `flake8_celery_bind_checker` is a Flake8 plugin designed to ensure that Celery task functions are correctly defined with respect to the `bind=True` parameter. Specifically, it checks that:

1. Functions decorated with `@shared_task(bind=True)` must have `self` as their first argument.
2. Functions decorated with `@shared_task(bind=False)` or without the `bind` parameter should not have `self` as their first argument.

These checks help maintain consistency and prevent common errors in defining Celery tasks.

## Installation

To install `flake8_celery_bind_checker`, you can use pip:

```
pip install flake8_celery_bind_checker
```

Alternatively, if you have access to the source code, navigate to the plugin directory and run:

```
pip install .
```

## Usage

Once installed, `flake8_celery_bind_checker` will automatically be included when you run Flake8. To check your Python files, simply use:

```
flake8 your_project_directory/
```

If you are using a virtual environment, make sure `flake8` and `flake8_celery_bind_checker` are installed within the same environment.

## Error Codes

This plugin defines the following error codes:

- **CBL001**: Celery task with `bind=True` must have `self` as its first argument. This error is raised when `bind=True` is specified, but the first parameter is not `self`.
- **CBL002**: Celery task without `bind=True` or with `bind=False` should not have `self` as its first argument. This error is raised when `bind=True` is not specified, or `bind=False` is explicitly stated, and yet the first parameter is `self`.

## Contributing

Contributions to `flake8_celery_bind_checker` are welcome! Please feel free to fork the repository, make changes, and submit pull requests. If you find any issues or have suggestions for improvements, please open an issue in the repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
