# -*- coding: UTF-8 -*-
from Products.Five.browser import BrowserView
from plone import api

import logging
logger = logging.getLogger(__name__)


class DojoView(BrowserView):
    """A browser view.
    """

    def dojo(self):
        """Add code here.
        """

        return "Hello Plone!"
