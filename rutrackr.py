#!/usr/bin/python
import pyquery


def get_magnet_links(content):
    pq = pyquery.PyQuery(content)
    seen = set()
    for a in pq.find('a'):
        href = a.get('href')
        if href and (href.startswith("magnet")):
            seen.add(href)
    return list(seen)


def get_list():
    print("Enter/Paste your links")
    contents = []
    try:
        while True:
            line = input()
            if line:
                contents.append(line)
            else:
                break
        return contents
    except Exception:
        print("Enter/Paste urls")
        exit(1)


for item in get_list():
    magnets = get_magnet_links(item)
    for m in magnets:
