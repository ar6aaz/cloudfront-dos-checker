import sys
import requests

# Read the list of URLs from the file specified in the command line argument
urls_file = sys.argv[1]
with open(urls_file, "r") as f:
  urls = f.readlines()
  count = len(f.readlines())

# The keyword to search for in the HTTP response to find if the website is on Cloudfront
keyword = "X-Amz-Cf-Pop"
keyword2 = "X-Amz-Cf-Id"
keyword3 = "X-Cache"
additional_header = {'X-Amz-Server-Side-Encryption': 'AES256xss'}
count = 0

# Send an HTTP request to each URL and search for the keyword in the response
for url in urls:
  response = requests.get(url)
  if ((keyword in response.headers) and (keyword2 in response.headers)
      and (keyword3 in response.headers)):
    additional_response = requests.get(url + '/?test',
                                       headers=additional_header)
    if ((additional_response.status_code == 400)):
      print(
        f"Possible Misconfiguration found. Worth checking the URL manually: {url}"
      )

print(f"Completed checking all {count} URLs in the file")