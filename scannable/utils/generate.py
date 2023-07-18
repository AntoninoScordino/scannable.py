#
# Copyright (C) 2023 Antonino Scordino <a.scordino.07@gmail.com>
#
# SPDX-License-Identifier: WTFPL
#

from spotify_uri import formatURI

class Generate:
    def __init__(self, format, background, text, size, link):
        self.format = format
        self.background = background
        self.text = text
        self.size = size
        self.link = link

        # Gather the ur from the provided link __only__ if the link
        # contains 'open.spotify.com'.
        if 'open.spotify.com' in self.link:
            link = formatURI(self.link)
            # Remove the '$' from the generated 'formatURI'. For whatever
            # reason, it gets generated with some URL, while with other it
            # does not. For example, https://open.spotify.com/artist/3srPc1Mytv5GmTWqsQuoXW.
            if '$' in link:
                link = link.replace("$","")

        print(' :: Your scannable code is:\n' +
            '    https://scannables.scdn.co/uri/plain/' + self.format + '/' + self.background + '/' + self.text + '/' + self.size + '/' + link)
