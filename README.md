# tutorial_util
Repository to demonstrate creation of building python packages

## sumlib package

This library does a summation operation on two integers.


### Download
```bash
$ pip install --upgrade git+git://github.com/Lyra-Amorphous/tutorial_util@sumlib
```


To uninstall
```bash
sudo pip uninstall sumlib
```

### Version
```
0.0.6
```

### Usage
```python
import sumlib
num_sum = sumlib.dosum(10, 20)
mat_sum = sumlib.domatrixsum([10,20], [3,4])

print (num_sum)
print (mat_sum)
```
or 
```python
from sumlib import *
num_sum = dosum(10, 20)
mat_sum = domatrixsum([10,20], [3,4])

print (num_sum)
print (mat_sum)
```


### Output
```
>>> print (output)
30
>>> print (mat_sum)
[13 24]
```


### Running Tests
```
$ python -m tests.test_sumlib
```



#
# Steps to upgrade version of this package


This tutorial is for uploading python packages to test PyPI server.

#### Make required changes

You can make changes in files in `sumlib` folder, and configuration files like `setup.py`

#### Install required libraries & update version {default : patch}
```bash
$ ./bumpversion.sh
```

#### Create a build & upload distribution files - `NOT REQUIRED if you do not want to make this public`
Here, `projectname` = `sumlib`

In order to make this distribution public, you can upload this on test PyPI server.
When finalized you can upload this the PyPI server.

Pre-requisites:
1. Account on  [Test PyPi server](https://test.pypi.org/)
2. Account on [PyPi server](https://pypi.org/)

Note : These are two separate servers, and you will need to create individuals accounts. 
It is not necessary to have the same credentials.

Next steps enable you to build you package in local, and publish it on the test PyPI server.

```bash
$ ./PyPIrunsetup.sh
```

You will be prompted for your PyPI account username and password

```bash
Enter your username: [YOUR_USERNAME]
Enter your password: 
Uploading distributions to https://test.pypi.org/legacy/
Uploading sumlib-0.0.4-py2.py3-none-any.whl
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8.06k/8.06k [00:02<00:00, 3.01kB/s]
Uploading sumlib-0.0.4.tar.gz
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10.8k/10.8k [00:01<00:00, 7.73kB/s]
```

After this completes, you will see a new project version here: 
https://test.pypi.org/project/<projectname>

You will have `<projectname>` available through `pip` publicly.
You can download this public library on test PyPI server with this command:
```bash
$ python -m pip install --upgrade --index-url https://test.pypi.org/simple/ --no-deps <projectname>
```

In order to make this available on PyPI server, replace `test.pypi.org` with `pypi.org` in `runsetup.sh`.

Libraries on PyPI server can be downloaded with this command:
```bash
$ python -m pip install --upgrade <projectname>
```
 
