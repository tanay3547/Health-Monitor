# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainKBAMll.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sqlite3
from cryptography.fernet import Fernet

key = bytes("0dzuqY18ULkPRa5z8bVTwx0aB2tHVAMkOb4noayA_-I=", 'utf-8')
cipher_suite = Fernet(key)

db = sqlite3.connect('mydb.db')
c = db.cursor()

def login(username, password):
	c.execute('SELECT * FROM users WHERE username = ?', (username,))
	ciphered_password = c.fetchall()[0][1]
	unciphered = cipher_suite.decrypt(ciphered_password).decode('utf-8')

	if password==unciphered:
		return True
	else:
		return False


def checkUsername(username):
	c.execute('SELECT * FROM users WHERE username = ?', (username,))
	if c.fetchall():
		return True
	else:
		return False

def signup(username, password):
	c.execute('SELECT * FROM users WHERE username = ?', (username,))
	if c.fetchall():
		print("Username exists")
		return

	ciphered_password = cipher_suite.encrypt(bytes(password, 'utf-8'))   #required to be bytes
	c.execute('INSERT INTO users (username, password) VALUES (?,?)', (username, ciphered_password))

	c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, ciphered_password))

	if c.fetchall():
		db.commit()
		return True
	else: 
		return False

  
# Execute sql statement and grab all records where the "usuario" and
# "senha" are the same as "user" and "password"
