<h1 align="center">User Acceptance Test Convention</h1>

Trip Teknologi's User Acceptance Test Codebase Convention.

Getting Started
---

Initialization :

`curl -sL https://raw.githubusercontent.com/tripteki/uat/main/bin/project | sh -s -- <project>`

Configuration :

    .
    ├── <project>/
    ├──── tests/
    ├────── _perform_/config/__init__.py
    ├────── __cli__/config/__init__.py
    ├────── ___api___/config/__init__.py
    ├────── ____web____/config/__init__.py
    └────── ____mobile____/config/__init__.py

Installation :

Move your current working directory to the outer of project. <br />
Copy `<project>/pyproject.toml` to current working directory. <br />
Then install it with this command :

```
$ python3 -m pip install .
```

Usage
---

`python3 -m <project>`

Option
---

- `--help` : Usage.
- `test:performance` : Run performance test.
- `test:cli` : Run cli test cases.
- `test:api` : Run api test cases.
- `test:web` : Run web test cases.
- `test:mobile` : Run mobile test cases.

Author
---

- Trip Teknologi ([@tripteki](https://linkedin.com/company/tripteki))
- Hasby Maulana ([@hsbmaulana](https://linkedin.com/in/hsbmaulana))
