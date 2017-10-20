#!/usr/bin/python2.7


class Topic:
    def __init__(self, id, section, title, content):
        self._id = id
        self._section = section
        self._title = title
        self._content = content

    def _get_id(self):
        return self._id

    def _get_section(self):
        return self._section

    def _get_title(self):
        return self._title

    def _get_content(self):
        return self._content

    id = property(_get_id)
    section = property(_get_section)
    title = property(_get_title)
    content = property(_get_content)
