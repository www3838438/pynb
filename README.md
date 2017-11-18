# [N]ote[B]ook[PY]thon[M]ark[D]own

## Installation

To install nbpymd on your system:

```
pip install nbpymd
```

## License

The nbpymd project is released under the MIT license. Please see `LICENSE.txt`.


## Development

The project has been developed and tested on `Python 3.6`.
Tests, builds and releases are managed with `Fabric`.
The build, test and releasing environment is managed with `Docker`.

Please install Docker and Fabric in your system. To install Fabric:

```
pip install Fabric3
```


### Releasing

Please build and start the Docker image: see *Docker container*.

Create a file `secrets.py` in the project directory with the Pypi credentials in this format:

```
pypi_auth = {
    'user': 'youruser',
    'pass': 'yourpass'
}
```

To release a new version:

```
fab release
```


### Tests

Please build and start the Docker image: see *Docker container*.

To run the module tests:

```
fab test
```

To run tests printing output and stopping at first error:

```
fab test_sx
```

To run the pep8 test:

```
fab test_pep8
```

To fix some common pep8 errors in the code:

```
fab fix_pep8
```

To test the pip package:
```
fab test_pip
```


### Docker container

To build the Docker image:

```
fab docker_build
```

To force a complete rebuild of the Docker image without using the cache:

```
fab docker_build:--no-cache
```

To start the daemonized Docker container:

```
fab docker_start
```

Top stop the Docker container:

```
fab docker_stop
```

To open a shell in the Docker container:

```
fab docker_sh
```

