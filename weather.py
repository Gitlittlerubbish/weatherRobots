#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__auther__ = 'Tony Chen'

'''
This is an automatic weather report robot
'''
import requests
import json
import os
from bs4 import BeautifulSoup
import bs4


def getWeather(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		txt = r.text
		loadedJson = json.loads(txt)
		return loadedJson
	except:
		return {}


def fillWeather(wlist, loadedJson):
	w = loadedJson['data']['forecast'][1]
	wlist.append([w['date'], w['high'], w['low'], w['type'], w['notice']])



def printWeather(wlist):
	print(wlist)


def main():
	wlist = []
	url = 'https://www.sojson.com/open/api/weather/json.shtml?city=宜兴'
	loadedJson = getWeather(url)
	fillWeather(wlist, loadedJson)
	printWeather(wlist)


main()