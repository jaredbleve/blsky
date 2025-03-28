from atproto_identity.cache.in_memory_cache import DidInMemoryCache
from atproto_identity.did.resolver import DidResolver

# THESE TESTS ARE NOT MOCKED WITH TEST SERVERS. IT PERFORMS REAL REQUESTS TO THE INTERNET.


def test_did_resolver_cache_with_web_feed() -> None:
    feed_url = 'feed.atproto.blue'
    did_web = f'did:web:{feed_url}'

    cache = DidInMemoryCache()
    resolver = DidResolver(cache=cache)
    did_doc = resolver.ensure_resolve(did_web)

    expected_object_id = id(did_doc)

    for _ in range(10):
        new_did_doc = resolver.ensure_resolve(did_web)
        # Check that the object is cached (same object id)
        assert expected_object_id == id(new_did_doc)

    cached_did_doc = (cache.get(did_web)).document
    assert cached_did_doc is did_doc


def test_did_resolver_cache_with_did_plc() -> None:
    did_plc = 'did:plc:kvwvcn5iqfooopmyzvb4qzba'

    cache = DidInMemoryCache()
    resolver = DidResolver(cache=cache)
    did_doc = resolver.ensure_resolve(did_plc)

    expected_object_id = id(did_doc)
    for _ in range(10):
        new_did_doc = resolver.ensure_resolve(did_plc)
        # Check that the object is cached (same object id)
        assert expected_object_id == id(new_did_doc)

    cached_did_doc = cache.get(did_plc).document
    assert cached_did_doc is did_doc


def test_did_resolver_resolve_no_cache() -> None:
    feed_url = 'feed.atproto.blue'
    did_web = f'did:web:{feed_url}'

    cache = DidInMemoryCache()
    resolver = DidResolver(cache=cache)

    cached_did_doc = resolver.ensure_resolve(did_web)
    new_did_doc = resolver.resolve_no_cache(did_web)

    assert id(cached_did_doc) != id(new_did_doc)


def test_did_resolver_resolve_force() -> None:
    feed_url = 'feed.atproto.blue'
    did_web = f'did:web:{feed_url}'

    cache = DidInMemoryCache()
    resolver = DidResolver(cache=cache)

    cached_did_doc = resolver.ensure_resolve(did_web)
    new_did_doc = resolver.ensure_resolve(did_web, force_refresh=True)

    assert id(cached_did_doc) != id(new_did_doc)


def test_did_resolver_refresh_cache() -> None:
    feed_url = 'feed.atproto.blue'
    did_web = f'did:web:{feed_url}'

    cache = DidInMemoryCache()
    resolver = DidResolver(cache=cache)

    cached_did_doc = resolver.ensure_resolve(did_web)
    resolver.refresh_cache(did_web)
    new_did_doc = resolver.ensure_resolve(did_web)

    assert id(cached_did_doc) != id(new_did_doc)
