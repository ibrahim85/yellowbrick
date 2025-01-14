# tests.test_utils.test_decorators
# Tests for the decorators module in Yellowbrick utils.
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Thu May 18 15:14:34 2017 -0400
#
# Copyright (C) 2017 District Data Labs
# For license information, see LICENSE.txt
#
# ID: test_decorators.py [79cd8cf] benjamin@bengfort.com $

"""
Tests for the decorators module in Yellowbrick utils.
"""

##########################################################################
## Imports
##########################################################################

from yellowbrick.utils.decorators import *


##########################################################################
## Decorator Tests
##########################################################################

class TestDecorators(object):
    """
    Tests for the decorator utilities.
    """

    def test_memoization(self):
        """
        Test the memoized property decorator on a class.
        """

        class Visualizer(object):

            @memoized
            def foo(self):
                return "bar"

        viz = Visualizer()
        assert not hasattr(viz, "_foo")
        assert viz.foo == "bar"
        assert viz._foo == "bar"

    def test_docutil(self):
        """
        Test the docutil docstring copying methodology.
        """

        class Visualizer(object):

            def __init__(self):
                """
                This is the correct docstring.
                """
                pass


        def undecorated(*args, **kwargs):
            """
            This is an undecorated function string.
            """
            pass

        # Test the undecorated string to protect from magic
        assert undecorated.__doc__.strip() == "This is an undecorated function string."

        # Decorate manually and test the newly decorated return function.
        decorated = docutil(Visualizer.__init__)(undecorated)
        assert decorated.__doc__.strip() == "This is the correct docstring."

        # Assert that decoration modifies the original function.
        assert undecorated.__doc__.strip() == "This is the correct docstring."

        @docutil(Visualizer.__init__)
        def sugar(*args, **kwargs):
            pass

        # Assert that syntactic sugar works as expected.
        assert sugar.__doc__.strip() == "This is the correct docstring."
