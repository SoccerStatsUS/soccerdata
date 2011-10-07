import datetime
import functools
import hashlib
import json
import leveldb

data_cache_db = leveldb.LevelDB("/home/chris/leveldb/data")

format_string = '%Y-%m-%dT%H:%M:%S'


def cache_format(el):

    def _inner(v):
        if type(v) == type([]):
            l2 = []
            for e in v:
                l2.append(_inner(e))
            return l2

        elif type(v) == type({}):
            d2 = {}
            for key, value in v.items():
                d2[key] = _inner(value)
            return d2

        if isinstance(v, datetime.datetime):
            return v.strftime(format_string)
        
        return v

    return json.dumps(_inner(el))


def cache_unformat(el):


    def _inner(v):
        if type(v) == type([]):
            l2 = []
            for e in v:
                l2.append(_inner(e))
            return l2

        elif type(v) == type({}):
            d2 = {}
            for key, value in v.items():
                d2[key] = _inner(value)
            return d2

        elif type(v) in [type(''), type(u'')]:
            try:
                return datetime.datetime.strptime(v, format_string)
            except:

                pass

        return v


    return _inner(json.loads(el))


def set_data_cache(cache_id, value):
    """
    Set a value in the cache.
    """
    data_cache_db.Put(cache_id, cache_format(value))


def get_data_cache(cache_id):
    """
    Get a value from cache.
    """
    return cache_unformat(data_cache_db.Get(cache_id))


class AbstractCache(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        raise NotImplementedError()

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__
    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)


class data_cache(AbstractCache):
    """
    A cache decorator that uses mongodb as a backend.
    """

    def __call__(self, *args):
        # Should maybe fail rather than returning None?
        # Presumably need kwargs in here too?
        key = hashlib.md5('%s:%s' % (self.func.func_name, args)).hexdigest()

        try:
            data = get_data_cache(key)
            print "Returning %s%s from data cache." % (self.func.func_name, args)
            return data
        except KeyError:
            pass

        value = self.func(*args)
        try:
            set_data_cache(key, value)
        except:
            import pdb; pdb.set_trace()
            x = 5

        return value


class set_cache(AbstractCache):
    """
    A decorator that will set the cache without trying to access it.
    """
    # Use this for overwriting old cache values.

    def __call__(self, *args):
        # Should maybe fail rather than returning None?
        # Presumably need kwargs in here too?
        key = hashlib.md5('%s:%s' % (self.func.func_name, args)).hexdigest()
        value = self.func(*args)
        set_data_cache(key, value)
        return value

                                    

