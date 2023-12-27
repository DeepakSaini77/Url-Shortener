# URL Shortener - Setup Guide

## Prerequisites

Ensure you have the following installed on your machine:

- [Python](https://www.python.org/) (>=3.6 Recommended)
- [Redis Server](https://redis.io/download)

> [!NOTE]
> if your python version <3.0, then instead of python3 use python


##### Install these dependencies

```
pip3 install Flask Flask-CORS redis

```

#### Start Redis server

```
redis-server
```
#### Now

``` 
python3 main.py
```

now go to open the index.html, or run the frontend by http-server,

go to 
``` 
/path/to/directory/public/index.html
```

## for test run
```
python3 -m unittest test_main.py
```
