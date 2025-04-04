##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2024 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


import typing as t

import typing_extensions as te
from pydantic import Field

if t.TYPE_CHECKING:
    from atproto_client import models
from atproto_client.models import base


class Params(base.ParamsModelBase):
    """Parameters model for :obj:`app.bsky.unspecced.searchStarterPacksSkeleton`."""

    q: str  #: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.
    cursor: t.Optional[str] = (
        None  #: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
    )
    limit: t.Optional[int] = Field(default=25, ge=1, le=100)  #: Limit.
    viewer: t.Optional[str] = (
        None  #: DID of the account making the request (not included for public/unauthenticated queries).
    )


class ParamsDict(t.TypedDict):
    q: str  #: Search query string; syntax, phrase, boolean, and faceting is unspecified, but Lucene query syntax is recommended.
    cursor: te.NotRequired[
        t.Optional[str]
    ]  #: Optional pagination mechanism; may not necessarily allow scrolling through entire result set.
    limit: te.NotRequired[t.Optional[int]]  #: Limit.
    viewer: te.NotRequired[
        t.Optional[str]
    ]  #: DID of the account making the request (not included for public/unauthenticated queries).


class Response(base.ResponseModelBase):
    """Output data model for :obj:`app.bsky.unspecced.searchStarterPacksSkeleton`."""

    starter_packs: t.List['models.AppBskyUnspeccedDefs.SkeletonSearchStarterPack']  #: Starter packs.
    cursor: t.Optional[str] = None  #: Cursor.
    hits_total: t.Optional[int] = (
        None  #: Count of search hits. Optional, may be rounded/truncated, and may not be possible to paginate through all hits.
    )
