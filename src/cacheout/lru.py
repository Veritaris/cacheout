"""The lru module provides the :class:`LRUCache` (Least Recently Used) class."""

import typing as t

from .cache import Cache


T = t.TypeVar("T")


class LRUCache(t.Generic[T], Cache[T]):
    """
    Like :class:`.Cache` but uses a least-recently-used eviction policy.

    The primary difference with :class:`.Cache` is that cache entries are moved to the end of the
    eviction queue when both :meth:`get` and :meth:`set` are called (as opposed to :class:`.Cache`
    that only moves entries on ``set()``.
    """

    def get(self, key: t.Hashable, default: t.Union[T, object, None] = None) -> T | None:
        with self._lock:
            value = super().get(key, default=default)
            if key in self._cache:
                self._cache.move_to_end(key)
            return value

    get.__doc__ = Cache.get.__doc__
