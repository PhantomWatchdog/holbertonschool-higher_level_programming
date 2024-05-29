#!/usr/bin/python3
"""
Create fetch_and_print_posts and fetch_and_save_posts methods
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from a RESTful API and prints their titles.

    This function sends a GET request to the specified URL and
        retrieves a list of posts in JSON format.
    It then iterates over the posts and prints the title of each post.

    Args:
        None

    Returns:
        None
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print('Status Code:', response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetches posts from the given URL and saves them in a CSV file.

    Returns:
        None
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        post_data = []
        for post in posts:
            post_data.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })
        with open('posts.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(post_data)
