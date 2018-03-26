import webbrowser
import requests
import logging

def browse(url):
    webbrowser.open(url=url)

def downloadPage(url, params={}, output=''):
    res = requests.get(url = url, params=params)

    logging.info('url=%s' %(res.url))

    try:
        res.raise_for_status()
        with open(output, 'wb') as f:
            for chunk in res.iter_content(128):
                logging.debug('chunk=>%s' %(chunk))
    except Exception as err:
        logging.error('An exception happened: ' + str(err))
