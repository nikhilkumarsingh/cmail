[![PyPI](https://img.shields.io/badge/PyPi-v1.0.0-f39f37.svg)](https://pypi.python.org/pypi/cmail)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/nikhilkumarsingh/cmail/blob/master/LICENSE.txt)

# cmail

A simple command-line email client!

![](https://media.giphy.com/media/d3YH60LyEcJylGuY/giphy.gif)

- works on **Linux**, **Windows** and **MacOS**
- send email **with attachments**
- save **contacts**

## Installation

To install cmail, simply,

```
$ pip install cmail
```

**Note:** You may need to allow less secure apps on your Gmail account to send email using **cmail**. You can toggle the settings here: [Less secure apps](https://myaccount.google.com/lesssecureapps)

## Usage

- Help command:

```
$ cmail -h

usage: cmail.py [-h] [-m] [-c] [-r] [-v] [-a name email]

A simple command-line email client!

optional arguments:
  -h, --help            show this help message and exit
  -m, --mail            Send mail.
  -c, --contacts        Shows the saved email contacts.
  -r, --reset           Reset contacts list to default.
  -v, --version         Get the current version of cmail
  -a name email, --add name email
                        Add new contact.

```

- To send mail:

	```
	$ cmail -m

	To: example@gmail.com
	Subject: test
	Text: hi there!
	Want to attach any files? (y/n): n
	Enter username (press Enter to use default 'me'): indianpythonista@gmail.com
	Enter password:  
	Your mail was sent successfully!

	```

- To save a contact:
	
	```
	$ cmail -a me nikhilksingh97@gmail.com
	New contact saved!
	```

- To show contacts:

	```
	$ cmail -c

	+---------+--------------------------+
	| name    | email                    |
	+=========+==========================+
	| me      | nikhilksingh97@gmail.com |
	+---------+--------------------------+
	| example | example@example.com      |
	+---------+--------------------------+

	```

- Clear contacts list:

	```
	$ cmail -r

	Contacts list reset to default.
	```
