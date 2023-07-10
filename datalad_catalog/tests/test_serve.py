from datalad.support.exceptions import InsufficientArgumentsError
from datalad.tests.utils_pytest import (
    assert_in_results,
    assert_result_count,
)
from datalad_catalog.serve import Serve
import pytest


from datalad_next.constraints.exceptions import CommandParametrizationError

catalog_serve = Serve()


def test_no_args():
    """The catalog argument is required"""
    with pytest.raises(CommandParametrizationError):
        catalog_serve()


# TODO: is it necessary to test that the server actually serves the catalog content?
