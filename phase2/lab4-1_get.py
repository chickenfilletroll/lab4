#!/usr/bin/env python3
# lab4-1_get.py
import requests #requests: Popular HTTP library for making web requests
import sys #sys: System-specific parameters and functions, used here for command-line arguments




def simple_get(url): # Creates a function called simple_get that takes a URL as parameter
    try:
        r = requests.get(url, timeout=5, allow_redirects=True) #requests.get(): Sends GET request to the specified URL
#timeout=5: Request will timeout after 5 seconds if no response
#allow_redirects=True: Automatically follows HTTP redirects (301, 302, etc.)
        print(f"[+] URL: {url}") #URL: Original requested URL
        print(f"    Status Code: {r.status_code}") #Status Code: HTTP status code (200 = OK, 404 = Not Found, etc.)
        print(f"    Final URL:   {r.url}") #Final URL: Actual URL after following redirects
        print(f"    Content-Type: {r.headers.get('Content-Type', 'N/A')}") #Content-Type: Type of content returned (HTML, JSON, etc.)
        print(f"    Server:       {r.headers.get('Server', 'N/A')}") #Server: Web server software information
        print(f"    Content-Length: {r.headers.get('Content-Length', 'Unknown')}") #Content-Length: Size of response content in bytes
#Uses .get() with default values to handle missing headers gracefully
                
        return r # Returns the response object for potential further processing
    except requests.exceptions.RequestException as e:
        print(f"[!] Request error for {url}: {e}")
        return None #Error handling: Catches any request-related exceptions and prints error message

if __name__ == '__main__': #Main guard: Ensures code only runs when script is executed directly (not imported
    if len(sys.argv) < 2: #Argument check: Verifies that a URL was provided as command-line argument
        print("Usage: python lab1_get.py <url>") #Usage instruction: Shows how to run the script correctly
        sys.exit(1) #Exit with error: Terminates if no URL provided


    simple_get(sys.argv[1])  #Function call: Passes the first command-line argument (the URL) to the simple_get function