
# -*- coding: utf-8 -*-


from selenium import webdriver


if __name__ == '__main__':
    driver = webdriver.PhantomJS()
    url = 'http://cs.crosswarp.com/wf/hoge/test/DomPage'
    driver.get(url)
    data = driver.page_source.encode('utf-8')
    print(data)
    driver.save_screenshot('cw.png')
    driver.quit()

