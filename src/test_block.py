import unittest

from block import BlockType, block_to_block_type


class TestBlock(unittest.TestCase):
    def test_block_to_block_type_ol(self):
        block = """1. Get underwear
2. ???
3. Profit"""
        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST,
        )


if __name__ == "__main__":
    unittest.main()
