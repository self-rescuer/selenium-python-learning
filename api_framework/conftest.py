import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.request_client import RequestClient


@pytest.fixture(scope="session")
def client():
    """全局共享一个 RequestClient 实例"""
    return RequestClient()