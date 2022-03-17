#!/usr/bin/env python
import os
import pprint
import encodingdotcom_api as api

if __name__ == '__main__':

    encoding_instance = api.Encoding(
        user_id=os.getenv('ENCODING_API_USER_ID', None),
        user_key=os.getenv('ENCODING_API_USER_KEY', None),
        request_format=api.ENCODING_API_JSON_REQUEST_FORMAT
    )
    print('Grabbing media status')
    result = encoding_instance.get_status(ids=[os.getenv('MEDIA_ID')])

    print('Media status results:')
    if encoding_instance.format == 'json':
        pprint.pprint(result)

    elif encoding_instance.format == 'xml':
        from lxml import etree

        print(etree.tostring(result, pretty_print=True, encoding='unicode'))

    else:
        print('Skipping attempt to render non-registered request format')
