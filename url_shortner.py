# -*- coding: utf-8 -*-
"""url_shortner.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TEDYTztDkC0PUuEFeQNv9VnxE0q8j5DJ

**TASK  -03  URL SHORTNER **

Before running the program, ensure you have installed the pyshorteners library:

Since we are given a task to shortern the url we need to get a long url first

lets google a sample long url
long url sample:www.yoursite.com/?/post/2021/12/08/$5982-! #_ref;di(@%

now since we got a long url lets start with a code install pip shorteners
"""

pip install pyshorteners

import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

def main():
    print("URL Shortener")
    print("-----------------")
    long_url = input("Enter the long URL you want to shorten: ")

    try:
        short_url = shorten_url(long_url)
        print("Shortened URL:", short_url)
    except pyshorteners.exceptions.UnknownShortener:
        print("Error: Unknown URL shortener. Please try again later.")
    except pyshorteners.exceptions.ShorteningErrorException:
        print("Error: Unable to shorten the URL. Please check the URL and try again.")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()

"""So this is the shortened url we required
Shortened URL: https://tinyurl.com/283bxsos
"""