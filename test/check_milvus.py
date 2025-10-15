import os
import socket
import traceback
from urllib.parse import urlparse

from pymilvus import MilvusClient

MILVUS_URI = "https://in03-7b3b56e59d62e9d.serverless.aws-eu-central-1.cloud.zilliz.com"
MILVUS_TOKEN = "30cff684b802d87f26e0c7ea80e43c759237808981ac1563ae400b00316ff84be4261492ee91b9f55ec6ad8a25b7be9b483fc957"  # replace with your token or pass via env var

def simple_tcp_check(uri):
    p = urlparse(uri)
    host = p.hostname
    port = p.port or (443 if p.scheme == "https" else 80)
    s = socket.socket()
    s.settimeout(5)
    try:
        s.connect((host, port))
        return True, f"TCP connect OK {host}:{port}"
    except Exception as e:
        return False, str(e)
    finally:
        s.close()

def test_milvus():
    try:
        ok, msg = simple_tcp_check(MILVUS_URI)
        print("TCP check:", msg)
        client = MilvusClient(uri=MILVUS_URI, token=MILVUS_TOKEN)
        print("MilvusClient created:", type(client))
        # Try introspection calls; some methods vary by pymilvus version
        for try_name in ("list_collections", "has_collection('hybrid_rag_collection')", "get_server_version", "show_collections"):
            if hasattr(client, try_name):
                try:
                    result = getattr(client, try_name)()
                    print(f"{try_name}() ->", result if result is not None else "(empty)")
                except Exception as e:
                    print(f"{try_name}() raised:", e)
        # Fallback: show available methods to debug API
        print("Available client methods (sample):", sorted([m for m in dir(client) if not m.startswith("_")])[:40])
    except Exception as e:
        print("Connection/test failed:")
        traceback.print_exc()

if __name__ == "__main__":
    test_milvus()