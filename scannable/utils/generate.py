#
# Copyright (C) 2023 Antonino Scordino <a.scordino.07@gmail.com>
#
# SPDX-License-Identifier: WTFPL
#

class Generate:
    def __init__(self, format, background, text, size, link):

        # Set default values. They are required, otherwise the picture
        # won't be generated at all.
        format = 'png'
        background = '000000'
        text = 'white'
        size = '512'

        self.format = format
        self.background = background
        self.text = text
        self.size = size
        self.link = link
        