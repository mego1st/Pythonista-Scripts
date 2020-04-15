import appex

def main():
  #retrieve url when ran in safari
  url = appex.get_web_page_info()
  print(url['url'])
  #write url to file
  file = open('bookmarks.txt', 'a+')
  a = (url['url'])
  file.write(a + '\n')
  file.close()

if __name__ == '__main__':
  main()
