from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from argparse import ArgumentParser
from ConfigParser import SafeConfigParser
from time import sleep



def get_User(vendor, cFile='user.conf'):
	config = SafeConfigParser()
	config.read(cFile)
	user = config.get(vendor, 'user')
	password = config.get(vendor, 'password')
	return (user, password)


def get_Login(vendor, cFile='vendor.conf'):
	config = SafeConfigParser()
	config.read(cFile)
	loginUrl = config.get(vendor, 'login')
	uE = config.get(vendor, 'uE')
	pE = config.get(vendor, 'pE')
	bE = config.get(vendor, 'bE')
	return (loginUrl, uE, pE, bE)


def get_action(vendor, action, cFile='vendor.conf'):
	config = SafeConfigParser()
	config.read(cFile)
	return config.get(vendor, action)


def login(vendor):
	user, password = get_User(vendor)
	url, uE, pE, bE = get_Login(vendor)
	driver = webdriver.Firefox()
	wait = WebDriverWait(driver, 10)
	driver.maximize_window()
	driver.get(url)
	driver.find_element_by_xpath(uE).send_keys(user)
	driver.find_element_by_xpath(pE).send_keys(password)
	driver.find_element_by_xpath(bE).click()
	sleep(3)
	return driver


def vendor_action(driver, action):
	if action:
		return driver.get(action)
	return driver


def arg_parse():
	parser = ArgumentParser(description='CLI for automating Vendor actions')
	parser.add_argument("--vendor", "-v", type=str, dest='vendor', choices=['hpe','cisco','dell','ibm','apc','netapp','huawei','panduit','se'], required=True, help='vendor name')
	parser.add_argument("--action", "-a", type=str, dest='action', choices=['spec','cert','deal','rebate','user','status','learn'], default='', help='type of action')
	args = parser.parse_args()
	return args.vendor.upper(), args.action


def main():
	vendor, action = arg_parse()
	drv = login(vendor)
	if action:
		action = get_action(vendor, action)
	vendor_action(drv, action)



if __name__ == '__main__':
	main()




