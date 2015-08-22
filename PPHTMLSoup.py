from BeautifulSoup import BeautifulSoup as bs


input_code = raw_input()
soup = bs(input_code)
prettyHTML = soup.prettify()

print prettyHTML
