


# Creating source and build distribution for the package
echo "Creating source and build distribution for the package"
echo "$ python3 setup.py sdist bdist_wheel"
python3 setup.py sdist bdist_wheel

# Uploading new version to PyPI server
# tar.gz (source distribution), .whl (build distribution)
echo "Uploading new version to PyPI server"
echo "$ python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*0.0.6*"
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*0.0.6*

