# -*- coding: utf-8 -*-
"""A Resoruce Manager that loosely implements Resource Acquisiton as Initialization. """

from contextlib import contextmanager, ExitStack

class ResourceManager():

    """A Resoruce Manager that loosely implements Resource Acquisiton as Initialization."""

    def __init__(self, acquire_resource, release_resource, check_resource_ok=None):
        self.acquire_resource = acquire_resource
        self.release_resource = release_resource
        if check_resource_ok is None: # No release resource once!
           def check_resource_ok(resource):
               return True
        self.check_resource_ok = check_resource_ok

    @contextmanager
    def _cleanup_on_error(self):
        """Clean up Resource"""
        with ExitStack() as stack:
            stack.push(self)
            yield
            stack.pop_all()

    def __enter__(self):
        """Enter Block. Return a clean, validated resource"""
        resource = self.acquire_resource()
        with self._cleanup_on_error():
            if not self.check_resource_ok(resource):
                msg = "Failed validation for {!r}"
                raise RuntimeError(msg.format(resource))
        return resource

    def __exit__(self, *exec_details):
        """Caller release resource"""
        self.release_resource()

