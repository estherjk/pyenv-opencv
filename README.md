# pyenv-opencv

Getting started with OpenCV in a Python virtual environment.

This guide is intended for macOS users who use [Homebrew](https://brew.sh/), as well as [pyenv](https://github.com/yyuu/pyenv) and [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv) to manage their Python environments.

## Installing pyenv and pyenv-virtualenv

Install pyenv and pyenv-virtualenv using Homebrew if you haven't already:

```bash
brew install pyenv pyenv-virtualenv
```

Install a Python version using pyenv:

```
pyenv install 2.7.13
```

## Installing OpenCV via Homebrew

Ensure that the system version of Python is active before installing OpenCV (for details on why, click [here](https://github.com/yyuu/pyenv/issues/106)):

```bash
pyenv shell system
brew install opencv
```

## Creating a Python virtual environment

Let's create a Python virtual environment using the version of Python that was installed in the previous section. This virtual environment will be our Python / OpenCV sandbox:

```bash
pyenv virtualenv 2.7.13 pyenv-opencv
```

Clone this repository to your computer and navigate to the directory where `pyenv-opencv` is located. The command prompt should change to look something like this:

```
# Update this to the path where pyenv-opencv is located on your computer
cd <path to pyenv-opencv>

(pyenv-opencv) ...$
```

pyenv-virtualenv automatically detects which Python virtual environment to activate based on what is specified in `.python-version`.

Install the Python dependencies using pip:

```bash
(pyenv-opencv) ...$ pip install -r requirements.txt
```

Create symlinks so that OpencV is accessible to the Python virtual environment:

```bash
# This is the site packages directory for our Python virtual environment
cd ~/.pyenv/versions/pyenv-opencv/lib/python2.7/site-packages

# Symlink files needed from the OpenCV Homebrew installation
ln -s /usr/local/Cellar/opencv/2.4.13.2/lib/python2.7/site-packages/cv.py cv.py
ln -s /usr/local/Cellar/opencv/2.4.13.2/lib/python2.7/site-packages/cv2.so cv2.so
```

*Note: Your version of OpenCV may be different. The directory structure is similar though, where it will look something like `/usr/local/Cellar/opencv/<version>/lib/python2.7/site-packages`.The procedure will be the same as above, where you will want to symlink `cv.py` and `cv2.so` to your virtual environment's site-packages folder.*

To check that OpenCV is configured correctly, navigate back to the `pyenv-opencv` directory and open Python:

```bash
# Update this to the path where pyenv-opencv is located on your computer
cd <path to pyenv-opencv>

(pyenv-opencv) ...$ python
Python 2.7.13 (default, Feb 25 2017, 10:24:16)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
```

If there are no errors, then you're good!

### Running a face detection example

Now, you should be able to use OpenCV in your Python virtual environment. Run `detection.py` to see a simple face detection example in action:

```bash
(pyenv-opencv) ...$ python detection.py
```
