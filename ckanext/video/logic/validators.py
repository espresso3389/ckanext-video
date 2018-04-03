#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-video
# Created by the Natural History Museum in London, UK

import re
from ckan.common import _
import ckan.lib.navl.dictization_functions as df

from ckanext.video.providers import video_provider_patterns

Invalid = df.Invalid
Missing = df.Missing


def is_valid_video_url(value, context):

    '''Validate a URL is a valid video URL

    :param value: 
    :param context: 

    '''
    for pattern in video_provider_patterns.values():
        if re.search(pattern, value, re.IGNORECASE):
            return value

    raise Invalid(_(u'URL is not a valid video provider'))
