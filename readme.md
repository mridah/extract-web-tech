# extract-web-tech

## Description

Extract website platform information from a list of urls


## Requirements

- python 2.7 and above
- virtualenv

## Set up

- Navigate to project root folder and initialize `virtualenv`

```
    virtualenv venv
```

- Start virtual environment

```
    source venv/bin/activate    <--- for linux
    venv\scripts\activate    <--- for windows
```

- Install required packages in virtual environment

```
    pip install requirements.txt
```

- Edit urls.txt and place your urls in the following format

```
    url1.com
    www.url2.com
    abc.url3.com
```

NOTE: No need to prepend url with `http://`

- Run the script

```
    python run.py
```

This will create a new file `data.csv` with all the output.


- Exit the virtual environment

```
    deactivate    <--- for linux
    venv\scripts\deactivate    <--- for windows
```
