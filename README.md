```
 __  __                       __ _                       _____                        _             
|  \/  |    ___       _ _    / _` |    ___       o O O  |_   _|     _ _    __ _      (_)     _ _    
| |\/| |   / -_)     | '_|   \__, |   / -_)     o         | |      | '_|  / _` |     | |    | ' \   
|_|__|_|   \___|    _|_|_    |___/    \___|    TS__[O]   _|_|_    _|_|_   \__,_|    _|_|_   |_||_|  
_|"""""| _|"""""| _|"""""| _|"""""| _|"""""|  {======| _|"""""| _|"""""| _|"""""| _|"""""| _|"""""| 
"`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' ./o--000' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' 
```

# Merge-Train

A tool for teams that need to scale

## Quickstart

1. Install the required dependences
```sh
pip install -r requirements.txt
```

2. Ensure that the `GITHUB_PERSONAL_ACCESS_TOKEN_MERGE_TRAIN` environment variable is set with your [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) (it is like a scoped, expiring password for a single app)

3. Run the merge train command
```sh
./merge_train.py
```

## Contributing

Start a new virtual environment with
```sh
python3 -m venv ./venv
./venv/bin/activate
```

To update the list of dependencies
```sh
pip freeze > requirements.txt
```

To check for outdated dependencies
```sh
pip list --outdated
```