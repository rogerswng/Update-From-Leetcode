# -*- coding: utf-8 -*-

import requests, re, time

urlLeetCode = "https://leetcode.com/problemset/algorithms/#"

flag = 0
r = requests.get(urlLeetCode)
rEncode = r.text.encode("utf-8")

with open("html.txt", "w") as f:
	f.write(rEncode)

with open("html.txt", "r") as f:
	for each_line in f:
		each_line = each_line.strip()
		#print(each_line)
		m = re.match(r"^<td>(\d+)</td>$", each_line)
		if m is not None:
			print(m.group(1))
			flag = 1
		if flag == 1:
			n = re.match(r"^<a href=.*>(.*)</a>$", each_line)
			if n is not None:
				print(n.group(1))
				break
