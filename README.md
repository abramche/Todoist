Todoist Android/Appium automation project skeleton
====================

A test project for [Todoist](https://en.todoist.com/) application, sporting both back-end and front-end actions.

# Prerequisites

Several dependencies will need to be installed prior to running the test cases.

1. [Python 3](https://www.python.org/), this particular project was written on the latest version (3.7.2 as of committing this README).

2. [Appium-Python-Client](https://pypi.org/project/Appium-Python-Client/), easiest to be installed from [PyPi](https://pypi.org). This will also install node.js and other Appium client dependencies.

    ```shell
    pip install Appium-Python-Client
    ```

3. [pytest](https://docs.pytest.org/en/latest/) and [unittest2](https://pypi.org/project/unittest2/) are used for setting up the fixtures and assertions.

    ```shell
    pip install unittest2
    pip install pytest
    ```

4. Install from source via [GitHub](https://github.com/appium/python-client).

    ```shell
    git clone git@github.com:appium/python-client.git
    cd python-client
    python setup.py install
    ```
    
5. [Todoist Python library](https://github.com/doist/todoist-python) for their implementation of the API calls.

    ```shell
    pip install todoist-python
    ```
    
6. Either a physical connected Android device (enable USB debugging) or an [Android emulator](https://developer.android.com/studio/run/emulator). The tests were written using the latter running the version 7.0.

## Run tests

You can run 3 tests using `pytest`. Note that both Appium web server and the Android device should be running for the tests.

```
$ pytest
```
