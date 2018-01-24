import os
import sys
import json
import argparse
from getpass import getpass
from tabulate import tabulate
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5 import QtWidgets

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


try:
	with open(os.path.join(os.path.dirname(__file__), 'contacts.json'), "r") as f:
		contacts = json.loads(f.read())
except FileNotFoundError:
	contacts = {}


def create_msg(receiver, subject=None, text=None, files=None):
	msg = MIMEMultipart()
	msg['To'] = receiver
	msg['Subject'] = subject
	msg.attach(MIMEText(text))

	if files:
		for filename in files:
			with open(filename, "rb") as f:
				part = MIMEApplication(f.read())
				part.add_header('Content-Disposition', 'attachment', 
								filename=filename.split('/')[-1])
				msg.attach(part)
	return msg


def select_files():
	qtapp = QApplication(sys.argv)
	qtwgt = QtWidgets.QWidget()
	filenames, _ = QFileDialog.getOpenFileNames(qtwgt)
	return filenames


def send_mail(msg):
	global contacts

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()

	flag = False
	while not flag:
		username = input("Enter username (press Enter to use default \'me\'): ")
		if username == "": 
			try:
				username = contacts['me']
			except:
				print("Set default contact by setting email with name \'me\'.")
				sys.exit(0)
		password = getpass("Enter password: ")

		try:
			server.login(username, password)
			flag = True
		except Exception as e:
			print("Login failed. Please try again.")
			flag = False

	msg['From'] = username
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	print("Your mail was sent successfully!")


def mailer():
	global contacts

	receiver = input("To: ")
	if "@" not in receiver:
		try:
			receiver = contacts[receiver]
		except:
			print("Contact not found. Please enter complete email or save new contact.")
			sys.exit(0)
	subject = input("Subject: ")
	text = input("Text: ")
	opt = input("Want to attach any files? (y/n): ")
	if opt == 'y':
		files = select_files()
	else:
		files = None

	msg = create_msg(receiver, subject, text, files)
	send_mail(msg)


def main():
	global contacts

	parser = argparse.ArgumentParser(description = "A simple command-line email client!")
 
	parser.add_argument("-m", "--mail", action='store_true',
						help = "Send mail.")

	parser.add_argument("-c", "--contacts", action='store_true',
						help = "Shows the saved email contacts.")

	parser.add_argument("-r", "--reset", action='store_true',
						help = "Reset contacts list to default.")

	parser.add_argument("-a", "--add", type = str, nargs = 2,
						metavar = ("name", "email"), default = None,
						help = "Add new contact.")
	  
	args = parser.parse_args()

	if args.mail:
		mailer()

	elif args.contacts:
		print(tabulate(contacts.items(), tablefmt="grid", headers=["name", "email"]))

	elif args.reset:
		contacts = {}
		with open(os.path.join(os.path.dirname(__file__), 'contacts.json'), "w") as f:
			f.write(json.dumps(contacts))
		print("Contacts list reset to default.")

	elif args.add != None:
		name, email = args.add
		contacts[name] = email
		with open(os.path.join(os.path.dirname(__file__), 'contacts.json'), "w") as f:
			f.write(json.dumps(contacts))
		print("New contact saved!")
		
	elif len(sys.argv) == 1:
		parser.print_help()


if __name__=="__main__":
	main()
