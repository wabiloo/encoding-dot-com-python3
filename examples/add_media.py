#!/usr/bin/env python
import os
import pprint
import encodingapi

if __name__ == '__main__':
    encoding_instance = encodingapi.Encoding(
        user_id=os.getenv('ENCODING_API_USER_ID', None),
        user_key=os.getenv('ENCODING_API_USER_KEY', None),
        request_format=encodingapi.ENCODING_API_JSON_REQUEST_FORMAT
    )
    print('Grabbing media status')

    formats = [
        {
            "output": "mp4",
            "size": "0x240",
            "maxrate": "300000",
            "two_pass": "yes",
            "metadata_copy": "no",
            "twin_turbo": "no",
            "hint": "no",
            "audio_stream": [],
            "profile": "high",
            "bitrate": "300000",
            "framerate": "copy",
            "force_keyframes": "2s",
            "deinterlacing": "no",
            "use_video_codec_parameters": "yes",
            "video_only": "yes",
            "video_codec": "libx264",
            "cbr": "no",
            "video_codec_parameters": {
                "me_range": "16"
            },
            "rotate": "0",
            "turbo": "no",
            "keep_aspect_ratio": "yes",
            "cut_black": {
                "enable": "no"
            }
        }
    ]

    for i, f in enumerate(formats):
        f['destination'] = os.getenv("DESTINATION_FOLDER") + f"/file{i}.mp4"

    result = encoding_instance.add_media(
        source=os.getenv('SOURCE'),
        formats=formats,
        metadata={
            "MyKey": "MyValue"
        }
    )

    print('AddMedia results:')
    if encoding_instance.format == 'json':
        pprint.pprint(result)

    elif encoding_instance.format == 'xml':
        from lxml import etree

        print(etree.tostring(result, pretty_print=True, encoding='unicode'))

    else:
        print('Skipping attempt to render non-registered request format')
