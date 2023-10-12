# Family Recipes Back End
This is an app that would allow families or a group of friends to share recipes with each other. There would be different options to write in your own recipe or to take a picture of a physical recipe and upload it. This would allow families and groups of friends to share their cooking experiences with each without having to be in the same place. It would also be a great way to store recipes that you like so that you wouldn't have to search through old cookbooks to find a recipe that was used before. A user could also be a part of more than one family or group to share more recipes with different people.

A shopping list feature could be added that would add the ingredients of a recipe to a shopping list so that it would be easy to find all the ingredients you would need. In addition to the shopping list feature, a meal planning feature could be added that would allow users to plan out their meals and coordinate their shopping trips effectively.


# Python Setup
Install `pyenv` to manage python installations; [Linux, macOS, and WSL](https://github.com/pyenv/pyenv/tree/master?tab=readme-ov-file#unixmacos), [windows](https://github.com/pyenv-win/pyenv-win?tab=readme-ov-file#installation).  
With `pyenv` installed you can now easily install specific python versions.  
Use `pyenv install -l` to list all versions available for your system.  
I think we should use version `3.11.5` since windows `pyenv` doesn't appear to have `3.11.6`. Install `3.11.5` with:
```sh
pyenv install 3.11.5
```
To use this installation, run `pyenv shell 3.11.5` to activate that version for your current shell session or you can run `python local 3.11.5` from the *root directory of this repo* to set `3.11.5` as the version for this project.  

Now that you have Python installed you can setup your virtual environment with `venv`. Inside the repo root, with your python install activated, run the following:
```sh
python3 -m venv .venv
```
This will create a new virtual enviroment inside the `.venv` directory. This is where libraries and packages will be installed so they don't interferre with any system python packages.  
Environments also need to be activated/deactivated:  
On macOS / Linux run / WSL:
```sh
source ./.venv/bin/activate
```
On windows [Powershell](https://github.com/microsoft/PowerShell):
```sh
./.venv/Scripts/Activate.ps1
```
On windows CMD (you probably want to use PowerShell on windows, it's just better in every way):
```sh
.\.venv\Scripts\activate.bat
```

Once you've actiavated the environment you should see a `(.venv)` somewhere in your shell prompt.  
<pic>  
You can also verify that you are using the venv python by running `which python` (`get-command python` on Powershell), it should point to the python interpreter in `.venv/bin/`  

To install the project dependencies listed in `./requirements.txt`, run:
```sh
pip install -r requirements.txt
```

This will install the basic dependcies for our project (`Flask`, `libsql_client`, `python-dotenv`), but only inside of you virtual environment; they will not be accessible without the environment actiavated.  

To deactiavte your virtual environment run:
```sh
deactivate
```

`.venv` is not checked into git, if you ever need to recreate it just remove it (`rm -rdf .venv`) and re-create using the steps above.  

For more info on `venv`, check the [docs](https://docs.python.org/3/library/venv.html)

