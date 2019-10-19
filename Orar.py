from selenium import webdriver

chromeDriver = 'C:\\Users\\CalinNUTU\\source\\chromedriver_win32\\chromedriver.exe'
browser = webdriver.Chrome(chromeDriver)
browser.maximize_window()
browser.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vThTUuLTXVjArLiEL5PxLYAmXCfV5HLbxIaPSxbfIiQ9j06AwUNID7Hi2QAgeuDJkoW1MfBLIxpI6-m/pubhtml?gid=294857279&single=true')
