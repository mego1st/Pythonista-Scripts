import appex

url = appex.get_web_page_info()
print(url['url'])

def write_to_file:
  file = open('bookmarks.txt', 'a+')
  a = (url['url'])
  file.write(a + '\n')
  file.close()

write_to_file()
