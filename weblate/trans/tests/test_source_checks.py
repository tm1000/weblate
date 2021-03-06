# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2018 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

"""
Tests for source checks.
"""

from __future__ import unicode_literals
from django.test import TestCase
from weblate.trans.checks.source import (
    OptionalPluralCheck,
    EllipsisCheck,
)
from weblate.trans.tests.test_checks import MockUnit


class OptionalPluralCheckTest(TestCase):
    def setUp(self):
        self.check = OptionalPluralCheck()

    def test_none(self):
        self.assertFalse(
            self.check.check_source(
                ['text'],
                MockUnit(),
            )
        )

    def test_plural(self):
        self.assertFalse(
            self.check.check_source(
                ['text', 'texts'],
                MockUnit(),
            )
        )

    def test_failing(self):
        self.assertTrue(
            self.check.check_source(
                ['text(s)'],
                MockUnit(),
            )
        )


class EllipsisCheckTest(TestCase):
    def setUp(self):
        self.check = EllipsisCheck()

    def test_none(self):
        self.assertFalse(
            self.check.check_source(
                ['text'],
                MockUnit(),
            )
        )

    def test_good(self):
        self.assertFalse(
            self.check.check_source(
                ['text…'],
                MockUnit(),
            )
        )

    def test_failing(self):
        self.assertTrue(
            self.check.check_source(
                ['text...'],
                MockUnit(),
            )
        )
