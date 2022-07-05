#!/usr/bin/python
import sys, selenium.common.exceptions, argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

parser = argparse.ArgumentParser(description='This script is going to monitor web page load time.')
parser.add_argument('-a', help='Define URL of monitored web page, for example https://itsfoss.com/')
parser.add_argument('-t', help='Default timeout is 15 second', default='15')
args = parser.parse_args()

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disk-cache-dir=/dev/null')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(args.t)
addr = args.a

try:
    driver.get(addr)
    connect_start = driver.execute_script('return window.performance.timing.connectStart')
    load_event_end = driver.execute_script('return window.performance.timing.loadEventEnd')
    total_time = load_event_end - connect_start
    print((total_time) / 1000)
    driver.quit()
except selenium.common.exceptions.TimeoutException:
    print('0')
    driver.quit()