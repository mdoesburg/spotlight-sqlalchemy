# Spotlight SQLAlchemy
SQLAlchemy plugin for [Spotlight](https://github.com/mdoesburg/spotlight).

## Table of Contents
* [Installation](#installation)
* [Dependencies](#dependencies)
* [Usage](#usage)
  * [Examples](#examples)
* [Available Rules](#available-rules)

## Installation
Spotlight SQLAlchemy can be installed via pip:

```
pip install spotlight-sqlalchemy
```

## Dependencies
* [python >= 3.6.0](https://www.python.org/)
* [SQLAlchemy >= 1.3.1](https://pypi.org/project/SQLAlchemy/)

## Usage
```python
from spotlight_sqlalchemy.plugin import SQLAlchemyPlugin
```

### Examples
```python
from spotlight.validator import Validator
from spotlight_sqlalchemy.plugin import SQLAlchemyPlugin

rules = {
    "id": "exists:user,id",
    "email": "unique:user,email"
}

input_ = {
    "id": 1,
    "email": "john.doe@example.com"
}

validator = Validator([SQLAlchemyPlugin(session)])
errors = validator.validate(input_, rules)
```

## Available Rules
* [unique (database)](#unique-database)
* [exists (database)](#exists-database)

_**Warning:**_
_You should never pass any user controlled input into the database rules. Otherwise, your application will be vulnerable to an SQL injection attack._


### unique (database)
The field under validation must be unique in a given database table. The last 4 fields (ignore column, ignore value, where column, where value) are optional.
```
unique:table,column
```
```
unique:table,column,ignoreColumn,ignoreValue
```
```
unique:table,column,ignoreColumn,ignoreValue,whereColumn,whereValue
```
```
unique:table,column,null,null,whereColumn,whereValue
```

### exists (database)
The field under validation must exist on a given database table. The last 2 fields (where column, where value) are optional.
```
exists:table,column
```
```
exists:table,column,whereColumn,whereValue
```