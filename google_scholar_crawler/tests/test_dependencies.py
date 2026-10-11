"""Offline regression checks for the Google Scholar crawler runtime."""
import unittest
from importlib import import_module
from importlib.metadata import version


class CrawlerDependencyTests(unittest.TestCase):
    def test_bibtexparser_retains_v1_api(self):
        # scholarly 1.5.1 imports this module; bibtexparser 2.x removed it.
        module = import_module("bibtexparser.bibdatabase")
        self.assertTrue(hasattr(module, "BibDatabase"))
        self.assertEqual(version("bibtexparser"), "1.4.3")

    def test_scholarly_imports_without_network_access(self):
        module = import_module("scholarly")
        self.assertTrue(callable(module.scholarly.search_author_id))
        self.assertTrue(callable(module.scholarly.fill))


if __name__ == "__main__":
    unittest.main()
