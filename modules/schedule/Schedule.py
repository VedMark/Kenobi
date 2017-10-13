#!/usr/bin/python2.7


class Schedule:
    def __init__(self, id, group, subject, day, lesson):
        self._id = id
        self._group = group
        self._subject = subject
        self._day = day
        self._lesson = lesson

    def _get_id(self):
        return self._id

    def _get_group(self):
        return self._group

    def _get_subject(self):
        return self._subject

    def _get_day(self):
        return self._day

    def _get_lesson(self):
        return self._lesson

    id = property(_get_id)
    group = property(_get_group)
    subject = property(_get_subject)
    day = property(_get_day)
    lesson = property(_get_lesson)
