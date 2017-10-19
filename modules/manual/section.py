#!/usr/bin/python2.7


class Section:
    def __init__(self, id, section):
        self._id = id
        self._section = section

    def _get_id(self):
        return self._id

    def _get_section(self):
        return self._section

    id = property(_get_id)
    section = property(_get_section)
