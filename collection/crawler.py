import sys
from urllib.request import Request, urlopen
from datetime import datetime


def crawling(
        url='',
        encoding='utf-8',
        proc=lambda html: html,
        store=lambda html: html,
        err=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):

    try:
        request = Request(url)
        resp = urlopen(request)

        try:
            receive = resp.read()
            result = store(proc(receive.decode(encoding)))

        except UnicodeDecodeError:
            result = receive.decode(encoding, 'replace')

        print('%s: success for request [%s]' % (datetime.now(), url))
        return result

    except Exception as e:
        err(e)