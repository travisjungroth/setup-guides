# Setup

Install brew
prereqs:
MacOS 10.13 or higher
Test
Run system_profiler SPSoftwareDataType
System version is > 10.13

Bourne compatible shell
Test
Run echo $0
The output should have bash or zsh in it

Actions
Go to brew.sh
Copy the install command
Paste it into terminal

Verification
Run brew --version

Install pyenv
Prereqs:
Brew

Actions
run brew install pyenv

Verification
pyenv --version


Add pyenv to shell complete
Prereqs
pyenv

Actions
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

Verification
pyenv shell
pyenv: no shell-specific version configured is good
pyenv: shell integration not enabled. Run `pyenv init' for instructions. is bad


Install pipenv
Prereqs:
Brew

Actions
run brew install pipenv

Verification
pipenv --version

Install postgres
Prereqs:
brew

Actions:
brew install postgres
brew services start postgresql
createdb $whoami


Verification
psql -c 'SELECT 0'


Clone the project
Prereqs:
git

Test:
git --version

Actions
cd into parent directory
run git clone https://github.com/highlycomposite/highlycomposite.git
cd highlycomposite

Verification
pwd to check path
git remote show origin to see tracking
ls to see files


Run pipenv install --dev
Prereqs:
pipenv
pyenv
project cloned

Action
pipenv sync --dev
Hit yes if needed

Verification
pipenv run python --version


Run the setup script
prereqs:
project

Verification
pipenv run pytest

