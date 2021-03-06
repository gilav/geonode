# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from geonode.tests.base import GeoNodeBaseTestSupport

import json
from django.urls import reverse
from geonode.compat import ensure_string
from geonode.catalogue import get_catalogue
from geonode.base.models import ResourceBase


class CatalogueTest(GeoNodeBaseTestSupport):

    def setUp(self):
        super(CatalogueTest, self).setUp()

    def test_get_catalog(self):
        """Tests the get_catalogue function works."""

        c = get_catalogue()  # noqa

    def test_data_json(self):
        """Test that the data.json representation behaves correctly"""

        response = self.client.get(reverse('data_json')).content
        data_json = json.loads(ensure_string(response))

        len1 = len(ResourceBase.objects.all())
        len2 = len(data_json)
        self.assertEqual(len1, len2, 'Expected equality of json and repository lengths')

        record_keys = [
            u'publisher',
            u'title',
            u'description',
            u'mbox',
            u'keyword',
            u'modified',
            u'contactPoint',
            u'accessLevel',
            u'distribution',
            u'identifier',
        ]

        for record in data_json:
            self.assertEqual(
                sorted(record_keys),
                sorted(list(record.keys())),
                'Expected specific list of fields to output')
