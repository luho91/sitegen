import unittest

from extract import extract_title


class TestExtraction(unittest.TestCase):
    def test_extract_title(self):
        t = "# Nigger"
        self.assertEqual(extract_title(t), "Nigger")


    def test_extract_title1(self):
        t = """```
haha, this is just
code lol
you don't even know man
```

but also this *is* a _paragraph_, wow!

for good measure, we put the h1 at the bottom and the h2 on top of it

## Nogger

# Absolute garbage dumpster"""
        
        self.assertEqual(extract_title(t), "Absolute garbage dumpster")


if __name__ == "__main__":
    unittest.main()
