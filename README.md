# Project Name Here

## Instructions

This is a template repository for Python applications. Feel free to use this as your starting point, instead of creating a repository from scratch.

You'll probably want to update this README file by:
 1. specifying your project name for the top level heading (above),
 2. changing the virtual environment name in the "Setup" section below (in both the creation and activation commands),
 3. updating the contents of the "requirements.txt" file to reflect the packages you're using in your project, and also
 4. Creating your own Python files in the app directory, and updating the "Usage" section below accordingly.

When you're done, remove this Instructions section from the README file.

## Setup

```sh
conda create -n project-xyz-env python=3.10

conda activate project-xyz-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

Create a new file in the root directory called ".env", and populate its contents:

```sh
# this is the ".env" file...

USER_NAME="Your Name"
PASSWORD="super secret"
```

## Usage

Run the example script:

```sh
python app/my_script.py

# ... OR ...

python -m app.my_script
```
