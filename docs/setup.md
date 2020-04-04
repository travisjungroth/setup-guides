# Setup

These instruction are an opinionated step-by-step guide aimed at beginners on MacOS. Unless you're installing this onto a new machine, you'll probably already have some of the requirements installed. To check if you can skip a section, use that section's Verification and skip if it already passes. Any step that's in code formatting `like this` means to enter the command in [Terminal](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac).

### Install Homebrew

#### Requirements

<details><summary>MacOS 10.13 or higher</summary>
<strong>Testing this requirement</strong></br>

1. `system_profiler SPSoftwareDataType`
2. System version should be >= 10.13

</details>

<details><summary>Bourne compatible shell</summary>
<strong>Testing this requirement</strong>
  
1. `echo $0`
2. The output should have "bash" or "zsh" in it

</details>

#### Steps

1. Go to https://brew.sh
2. Copy the install command on the home page.
3. Run the install command.

#### Verification

1. `brew --version`
2. It should return the Homebrew version.

### Install pyenv

#### Prerequisites

[Homebrew](/docs/setup.md#install-homebrew)

#### Steps

1. `brew install pyenv`

#### Verification

1. `pyenv --version`
2. It should return the pyenv version.

### Add pyenv to shell profile

#### Requirements

[pyenv](/docs/setup.md#install-pyenv)

### Steps

1. `echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bash_profile`
2. Close and reopen Terminal.

#### Verification

1. `pyenv shell`
2. It should return "pyenv: no shell-specific version configured" or a Python version number.

### Install Pipenv

#### Requirements

[Homebrew](/docs/setup.md#install-homebrew)

#### Steps

1. `brew install pipenv`

#### Verification

1. `pipenv --version`
2. It should return the Pipenv version.

### Install Postgres

#### Requirements

[Homebrew](/docs/setup.md#install-homebrew)

#### Steps

1. `brew install postgres`
2. `brew services start postgresql`
3. `createdb $whoami`

#### Verification

1. `psql -c 'SELECT 0'`
2. Check it matches the output below.

```
   ?column?
  ----------
          0
  (1 row)
```

### Clone the repo

#### Requirements

[git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

#### Steps

1. Use `cd` to change into an existing parent directory where you want the project located. For example, if you want it in ~/code/highly-composite, run `cd ~/code`.
2. `git clone https://github.com/highly-composite/highly-composite.git`
3. `cd highly-composite`

#### Verification

1. `pwd`
2. It should return the directory where you want this project, ending in highly-composite.
3. `git remote show origin`
4. The "Fetch URL" and "Push URL" should be https://github.com/highly-composite/highly-composite.git

### Install the Python dependencies

#### Requirements

[Pipenv](/docs/setup.md#install-pipenv)  
[pyenv](/docs/setup.md#install-pyenv)  
[Cloned repo](/docs/setup.md#clone-the-repo)

#### Steps

1. `pipenv sync --dev`
2. Enter "y" if prompted

#### Verification

1. `pipenv run python --version`
2. `cat runtime.txt`
3. These should return the same Python version.

### Run the setup script

#### Requirements

[Cloned repo](/docs/setup.md#clone-the-repo)

#### Steps

1. `scripts/setup.sh`

#### Verification

1. `pipenv run pytest`
2. The tests should run and all pass, with "\[100%\]" visible.

Now that it's set up, try [running the tests](/docs/testing.md) to verify the installation. Then, [run the server](/docs/running.md).
