# cloudfront-dos-checker
A python script to check if given list of URLs are vulnerable to DOS via cache poisoning

The tool automates the attack mentioned by [bxmbn](https://twitter.com/bxmbn) in this [blog post](https://bxmbn.medium.com/attacking-aws-cloudfront-cdn-19a96d5c0615).

# Usage

The tool accepts a txt file that has URLs in the format https://target.com

> python dos_checker.py urls.txt