# blackjack_game

# Description
+ This app allows the user to play Blackjack against a computer

# Prerequisites
+ Anaconda 3.8+
+ Python 3.8+
+ Pip

# Needed 3rd Party Packages
+ python-dotenv
+ pandas

# Needed Modules
+ import os
+ from pandas import read_csv

# Installation

1. Fork, download, or clone this [remote repository](https://github.com/krosen5514/blackjack_game) under your own control.

2. Use your preferred shell and navigate to the repository.

3. Setup a new virtual environment
```sh
conda create -n blackjack-env python=3.8 
conda activate blackjack-env
```

4. Install package dependencies
```sh
pip install -r requirements.txt
```

5. Edit the virtual environment
* Create a ".env" file and assign values to the following environment variables:
```
PLAYER_NAME=

```

6. Usage
* Run the game script
```py
python blackjack_game.py
```