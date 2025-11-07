#!/usr/bin/env python3
# lab4-1_collect_headers.py
import requests, json, sys

def collect(urls, out_file="headers.json"):
    results = []
    for url in urls:
        try:
            r = requests.get(url, timeout=5)
            results.append({
                "url": url,
                "status": r.status_code,
                "final_url": r.url,
                "server": r.headers.get("Server"),
                "content_type": r.headers.get("Content-Type"),
                "content_length": r.headers.get("Content-Length")
            })
        except requests.exceptions.RequestException as e:     # Catch any request-related exceptions (timeout, connection error, etc.)
            results.append({"url": url, "error": str(e)})   # store the error information in our results list
    with open(out_file, "w") as fh: # After processing all URLs (both successful and failed), write results to file, Open the output file in write mode
        json.dump(results, fh, indent=2) #Use json.dump to write the results list as formatted JSON, indent=2 creates pretty-printed JSON with 2-space indentation for readability
    print(f"Wrote {len(results)} entries to {out_file}") # Print a summary message to the console showing where results were saved

if __name__ == '__main__':
    urls = sys.argv[1:] #sys.argv[0] is the script name, sys.argv[1:] are the provided URLs
    if not urls: # Check if any URLs were provided
        print("Usage: python lab1_collect_headers.py <url1> <url2> ...") # Usage instruction if no rls found
        sys.exit(1) # Exit with error if no URLs provided
    collect(urls) # if provided Call the collect function with the list of URLs 