#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import requests
import csv

app = Flask(__name__)

SECRET = str(file.open("../SecretCode.txt").read())

@app.route('/proxies/<code>', methods=['POST'])
def getProxies(code):
	try:
		if str(code) == SECRET:
			with open('ProxyList.csv', 'rb') as f:
			    reader = csv.reader(f)
			    your_list = list(set(list(reader)))
			return {"Proxies": your_list}
	except:
		return "ERROR"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888)