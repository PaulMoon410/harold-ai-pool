import json
import unittest

from app import app


def call(path, method="GET"):
    captured = {}
    body = b"".join(app({"PATH_INFO": path, "REQUEST_METHOD": method},
                        lambda status, headers: captured.update(status=status)))
    return captured["status"], json.loads(body)


class AppTest(unittest.TestCase):
    def test_health(self):
        self.assertEqual(call("/health"), ("200 OK", {"status": "ok"}))

    def test_extensions_returns_registry(self):
        status, data = call("/extensions/")
        self.assertEqual(status, "200 OK")
        self.assertIsInstance(data["extensions"], list)

    def test_rejects_writes_and_unknown_paths(self):
        self.assertTrue(call("/extensions", "POST")[0].startswith("405"))
        self.assertTrue(call("/nope")[0].startswith("404"))


if __name__ == "__main__":
    unittest.main()
