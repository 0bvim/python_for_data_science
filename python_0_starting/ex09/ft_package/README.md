# How to Build and Install `ft_package`

1. **Build the package**

    Inside the `ft_package` folder, run:

    ```bash
    python -m build
    ```

    This command uses the `pyproject.toml` file to instruct Python how to build the package. The build artifacts will be created in the `dist/` directory.

2. **Install the package**

    To install the package using `pip`, run one of the following commands:

    ```bash
    pip install ./dist/ft_package-0.0.1.tar.gz
    ```

    or

    ```bash
    pip install ./dist/ft_package-0.0.1-py3-none-any.whl
    ```

3. **Test the package**

    After installation, you can test the package by running:

    ```bash
    python3 ../tester.py
    ```

4. **Uninstall the package**

    If you need to remove the package, use:

    ```bash
    pip uninstall ft_package
    ```

    This will uninstall `ft_package` from your Python environment.
