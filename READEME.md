# Send email with color capability AND attachments (multi-mime email)

## Sources used to build this example

[stack overflow](https://stackoverflow.com/questions/37204979/python-how-do-i-send-multiple-files-in-the-email-i-can-send-1-file-but-how-to-s)

as none of them worked i created working setup for me.

Other sources
[docs python](https://docs.python.org/3/library/email.examples.html)

[dotenv](https://pypi.org/project/python-dotenv/)

## notes

- if you don't have/want local email setup, you may need to connect to (authenticated) email server (gmail)
- your company zero trust might block the connection
- simple email will end up in SPAM folder


## python version/modules

used python venv and python 3.11.3 and 3.13.1

pip freeze create a huge list, mostly not relevant
python -m pipreqs.pipreqs . creates such additional crud.
requirement.txt created with:
```bash
% pip3 install pipreqs
% python -m  pipreqs.pipreqs .
```
as there is not that much to depend on, you can do probably without
```
pip install python-dotenv
```
if you like to continue loading environment from .env

## setup environment before run

set-up your environment vaiables :
- create yur own version of env.sh by using gmail-py-env-setup-example.sh
- source the file (bash)

## testfiles

[123].html are random test files to attach
you may want to use something more useful
