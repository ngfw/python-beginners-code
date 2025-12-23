#!/usr/bin/env python3
"""
Chapter 6: Working with Strings
Example 18: Extract Domain from URL

Demonstrates extracting the domain name from a URL.
"""

def extract_domain(url):
    """Extract domain from URL"""
    # Remove protocol
    if "://" in url:
        url = url.split("://")[1]
    # Remove path
    domain = url.split("/")[0]
    return domain

print(extract_domain("https://www.example.com/page"))  # www.example.com
print(extract_domain("http://github.com/user/repo"))   # github.com
