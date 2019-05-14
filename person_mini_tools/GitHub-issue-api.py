import requests
import sys


def main():
	# Github API 使用方式 URI
	# 用户 					https://api.github.com/users；
	# 某个用户某个仓库的issue 	https://api.github.com/repos/username/repo_name/issues?parameter=val; 
	# 某个用户的仓库 			https://api.github.com/user/repos；
	url = 'https://api.github.com/repos/jinyuyoulong/ideas/issues'
	headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
	json = requests.get(url)
	print(json.url)
	responseJson =  json.json()

	path = './autowrite/issues-json.txt'
	with open (path, 'w') as f:
		

	print(type(responseJson))


if __name__ == '__main__':
	main()