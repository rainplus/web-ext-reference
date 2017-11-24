#!/bin/python
# encoding:utf-8

import requests as r
from bs4 import BeautifulSoup
# import re
import html2text
import os

import sys

reload(sys)
sys.setdefaultencoding('utf8')

# import json

# html2text.BODY_WIDTH = 0

start_url = "https://developer.mozilla.org/en-US/Add-ons"
headers = {
	"user-agent": "Mozilla/6.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0",
	"Accept-Encoding": "identity",
	"Accept-Language": "en,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.5,zh-TW;q=0.3,zh-HK;q=0.2",
	"Cache-Control": "no-cache",
	"Connection": "keep-alive",
	"Host": "cdn.mdn.mozilla.net",
	"Origin": "https://developer.mozilla.org",
	"Pragma": "no-cache",
	"Referer": "https://cdn.mdn.mozilla.net/static/build/styles/mdn-skinny.83e893a66215.css"
}


class MDN:
	def __init__(self, url):
		self.url = url
		self.base_url = "https://developer.mozilla.org"
		self.index = 1
		self.content = {}

	def get_content(self):
		content = r.get(self.url, headers=headers).content
		soup = BeautifulSoup(content, 'html.parser')
		quick_links = soup.select("#quick-links > ol > li")
		for i, item in enumerate(quick_links):
			title = str(item.a.string).replace(" ", "_")
			url = item.a['href']
			title = self.preIndex(self.index) + "_" + title
			self.index += 1
			if item.ol != None:
				dict2 = self.buildContent(links=item.select('> ol > li'))
				dict2[title] = url
				self.content[title] = dict2
			else:
				self.content[title] = url

	def buildContent(self, links):
		index = 1;
		dict1 = {}
		for i, item in enumerate(links):
			title = str(item.a.string).replace(" ", "_")
			url = item.a['href']
			title = self.preIndex(index) + "_" + title
			index += 1
			if item.ol != None:
				dict2 = self.buildContent(links=item.select('> ol > li'))
				dict2[title] = url
				dict1[title] = dict2
			else:
				dict1[title] = url
		return dict1

	def preIndex(self, index):
		s = str(index)
		if len(s) < 2:
			return "0" + s
		else:
			return s

	def turn_path(self, url):

		val = str(url).replace("/en-US/docs/Mozilla/Add-ons/", "").replace("WebExtensions#", "").replace(
			"WebExtensions/", "").replace("?", "").replace("#", "")
		val_ = val[val.rfind("/") - len(val):]
		# print val_.replace("/", "")
		return val_.replace("/", "")

	def print_content(self, content, index=1, dirs=""):
		place = ""
		count = index
		while count > 1:
			place += "  "
			count -= 1
		items = content.items()
		items.sort();
		for key, value in items:
			summary = "SUMMARY.md"
			if isinstance(value, dict):
				with open(summary, "aw+")  as file:
					file.write("{}* [{}]({})\n".format(place, key, key + ".md"))
				print key, value[key]
				self.create_file_with_dir_and_md(key + ".md", value[key])
				del value[key]
				dirs = key + "/"
				self.print_content(value, index + 1, dirs)
			else:
				with open(summary, "aw+")  as file:
					if index == 1:
						md_name = self.turn_path(key) + "/" + self.turn_path(key + ".md")

						file.write("{}* [{}]({})\n".format(place, key, md_name))
						self.create_file_with_dir_and_md(md_name, value)
					else:
						md_name = dirs + self.turn_path(key) + "/" + self.turn_path(value + ".md")
						file.write("{}* [{}]({})\n".format(place, key, md_name))
						self.create_file_with_dir_and_md(
							md_name, value)

	def create_file_with_dir_and_md(self, file_name, url):

		if str(file_name).__contains__("http"):
			return
		dirName = os.path.dirname(file_name)
		# print dirName
		if not os.path.exists(dirName) and dirName != "./" and dirName != '':
			os.system("mkdir -p " + dirName)
		with open(file_name, "aw+") as file:

			if not str(url).__contains__("http"):
				response = r.get(self.base_url + url)
				if response.status_code == 200:
					html2text.inline_links = False
					articles = BeautifulSoup(response.content, 'html.parser').select("#wikiArticle")
					if len(articles) >0:
						md = html2text.html2text(str(articles[0]))
						file.write(md)





if __name__ == "__main__":
	os.system("ls |grep -vE 'README.md|mdn_content.py'|xargs rm -rf")

	mdn = MDN(start_url)
	mdn.get_content()
	mdn.print_content(mdn.content)
	os.system("find . -type f -name *.md|xargs  sed -i '' 's/\\n//g' ")
