import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def count_clicks(token, link):

    headers = {
        'Authorization': f'Bearer {token}',
    }

    params = (
        ('unit', 'month'),
        ('units', '1'),
    )

    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary',
        headers=headers, params=params
    )
    response.raise_for_status()
    clicks = response.json()['total_clicks']

    return clicks


def shorten_link(token, url):

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    data = {"long_url":  url}

    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers, json=data
    )
    response.raise_for_status()
    bitlink = response.json()['link']

    return bitlink


def is_bitlink(url, token):

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    parsed_url = urlparse(url)
    if parsed_url.scheme:
        bitly_link = f'{parsed_url.hostname}{parsed_url.path}'
    else:
        bitly_link = parsed_url.path

    data = {"bitlink_id":  bitly_link}

    response = requests.post(
        'https://api-ssl.bitly.com/v4/expand', headers=headers, json=data
    )

    return response.ok, bitly_link


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='+')

    return parser


if __name__ == '__main__':

    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')
    parser = create_parser()
    namespace = parser.parse_args()

    for user_input_url in namespace.name:

        it_is_bitlink, bitlink_path = is_bitlink(
            user_input_url,
            bitly_token
        )

        if it_is_bitlink:

            try:
                clicks_count = count_clicks(
                    bitly_token,
                    bitlink_path
                )
                print('Количество кликов по ссылке: ', clicks_count)
            except requests.exceptions.HTTPError:
                print('Ошибка: не удалось зачитать данные по ссылке')

        else:

            try:
                bitlink = shorten_link(bitly_token, user_input_url)
                print('Битлинк', bitlink)
            except requests.exceptions.HTTPError:
                print('Ошибка в имени ссылки!')
