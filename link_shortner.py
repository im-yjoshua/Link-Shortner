import requests
import validators

def UrlShortner(url):
    postRequest= requests.post(f'http://tinyurl.com/api-create.php?url={url}')
    response= postRequest.text
    print(f'Your short url is: {response}')

if __name__ == "__main__":
    print("Enter the URL you want to shorten: ")
    urlInput = input("Enter here: ")
    if not validators.url(urlInput):
        print("Invalid URL. Please enter a valid URL.")
    else:
        UrlShortner(urlInput)

