# Extract Elements from Webpage
Code snippet to count elements in a web page > this should use BeautifulSoup for statis webpages or geckodriver for dynamic ones

- opens a hardcoded webpage
- uses BeautifulSoup to search for elements
  - if it finds elements, returns the number of found elements
  - if number of found elements is 0, use geckodriver and return the number of found elements

