[![PyPI version](https://badge.fury.io/py/ippy.svg)](https://pypi.python.org/pypi/ippy)
[![Build Status](https://travis-ci.org/shivammathur/IPpy.svg?branch=master)](https://travis-ci.org/shivammathur/IPpy)
[![codecov](https://codecov.io/gh/shivammathur/IPpy/branch/master/graph/badge.svg)](https://codecov.io/gh/shivammathur/IPpy)
[![License](https://img.shields.io/badge/license-MIT-428f7e.svg)](https://pypi.python.org/pypi/ippy)
[![Support me on Patreon](https://shivammathur.com/badges/patreon.svg)](https://www.patreon.com/shivammathur)
[![Support me on Paypal](https://shivammathur.com/badges/paypal.svg)](https://www.paypal.me/shivammathur)
[![Contact me on Codementor](https://cdn.codementor.io/badges/contact_me_github.svg)](https://www.codementor.io/shivammathur?utm_source=github&utm_medium=button&utm_term=shivammathur&utm_campaign=github)

<img src="https://shivammathur.com/IPpy.png" align="right" width="250">

# :rocket: IPpy
Parallel testing of IP addresses and domains in python.
Reads IP addresses and domains from a CSV file and gives two lists of accessible and inaccessible ones. Refer to [Usage](#memo-usage) to see how to use this.

## :tada: About
- Compatible with both Python 2 and 3.
- Testing of IPs and domains is done in parallel.
- By default there are 4 Workers.
- All Workers work on an input Queue and a output Queue.

## :ab: Modes
- verbose - if true, ping output will be displayed.
- output - `json` or `csv`

## :sparkles: Support
- Windows, Linux and macOS are supported.
- Supports both IPv4 and IPv6 IPs, and domain names.

```csv
# Examples
127.0.0.1
::1
localhost
```

## :zap: Install

```bash
$ pip install ippy
```

## :memo: Usage

```python
# Create IPpy instance
ippy_obj = ippy.Ippy()

# Set config - verbose, output, num_workers
# verbose - True or False
# output - csv or json
ippy_obj.set_config(True, 'csv', 4)

# Set Input File
ippy_obj.set_file(file='ip_list.csv')

# Run IPpy
ippy_obj.run()

# Get Results
output = ippy_obj.result()
print(output)
```
## :rotating_light: Tests
To run the tests, first install tox.

```bash
$ pip install tox
```

then run tox from the project root directory.

```bash
$ tox
```

## :scroll: License

The scripts and documentation in this project are released under the [MIT License](LICENSE). This project has multiple [dependencies](https://github.com/shivammathur/ippy/network/dependencies) and their licenses can be found in their respective repositories.

## :+1: Contributions

Contributions are welcome! See [Contributor's Guide](.github/CONTRIBUTING.md).

## :sparkling_heart: Support this project

- Please star the project and share it.
- Consider supporting the project using [GitHub sponsors](https://github.com/sponsors/shivammathur).
