def main():
    # import libraries
    import urllib.request
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import time
    import pandas as pd

    # specify the url
    urlpage = 'https://groceries.asda.com/search/yogurt'
    print(urlpage)

    # query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(urlpage)

    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    # find product items
    results = soup.find_all('div', attrs={'class': 'co-product'})
    print('Number of results', len(results))

    # if you didn't define executable path in system variables:
    # driver = webdriver.Firefox(executable_path = 'your/directory/of/choice')
    # if you defined folder where geckodriver is in system variables as executable path
    driver = webdriver.Firefox()

    # get web page
    driver.get(urlpage)

    # makes sure all elements have loaded and scrolling scorlls to bottom
    time.sleep(5)

    # execute script to scroll down the page
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage = document.body.scrollHeight;return lenOfPage;")

    # if page calls cookie-acceptance-confirmation overlay, code still works in background

    # sleep for 30s
    time.sleep(5)

    driver.quit()


# main entry
if __name__ == '__main__':
    main()