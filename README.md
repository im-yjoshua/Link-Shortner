# URL Shortener

A simple Python script to shorten URLs using the TinyURL API.

## Requirements

Make sure you have the necessary dependencies installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```
The `requirements.txt` should contain:
```
requests
validators
```
## Usage
1. Clone the repository to your local machine:
```
git clone https://github.com/im-yjoshua/Link-Shortner.git
cd link-shortener
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Run the script:
```
python link_shortner.py
```
4. Enter the URL you want to shorten when prompted.
```
Enter the URL you want to shorten:
Enter here: https://example.com
```
5. If the URL is valid, you will receive a shortened URL:
```
Your short url is: http://tinyurl.com/abc123
```
# Code Explanation
```python
import requests
import validators

def UrlShortner(url):
    postRequest = requests.post(f'http://tinyurl.com/api-create.php?url={url}')
    response = postRequest.text
    print(f'Your short url is: {response}')

if __name__ == "__main__":
    print("Enter the URL you want to shorten: ")
    urlInput = input("Enter here: ")
    if not validators.url(urlInput):
        print("Invalid URL. Please enter a valid URL.")
    else:
        UrlShortner(urlInput)

```
- `import requests` Imports the requests module to handle HTTP requests.
- `import validators` Imports the validators module to validate URLs.
- `def UrlShortner(url)` Defines a function that takes a URL as an argument, sends a POST request to the TinyURL API, and prints the shortened URL.
- `if __name__ == "__main__":` Ensures the script runs only if it is executed as the main program.
- `urlInput = input("Enter here: ")` Prompts the user to enter a URL.
- `if not validators.url(urlInput):` Checks if the entered URL is valid.
- `UrlShortner(urlInput)` Calls the UrlShortner function with the user-provided URL if it is valid.

## License
This project is licensed under the MIT License.