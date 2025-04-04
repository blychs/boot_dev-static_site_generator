import unittest
from blocktype import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        text = "# lala"
        test = block_to_block_type(text)
        self.assertEqual(BlockType.HEADING, test)
        text = "## lala"
        test = block_to_block_type(text)
        self.assertEqual(BlockType.HEADING, test)
        text = "### lala"
        test = block_to_block_type(text)
        self.assertEqual(BlockType.HEADING, test)
        text = "#### lala"
        test = block_to_block_type(text)
        self.assertEqual(BlockType.HEADING, test)
        text = "##### lala"
        test = block_to_block_type(text)
        self.assertEqual(BlockType.HEADING, test)
        text = "###### lala"
        test = block_to_block_type(text)
        self.assertEqual(BlockType.HEADING, test)
        text = "####### lala"
        test = block_to_block_type(text)
        self.assertEqual(BlockType.PARAGRAPH, test)

    def test_code(self):
        text = """
        ```
            test
            ```
        """
        test = block_to_block_type(text)
        self.assertEqual(BlockType.CODE, test)

    def test_quote(self):
        text = """
            > ahora
            > nunca
            >mas
        """
        test = block_to_block_type(text)
        self.assertEqual(BlockType.QUOTE, test)

    def test_noquote(self):
        text = """
            > ahora
            > nunca
            mas
        """
        test = block_to_block_type(text)
        self.assertEqual(BlockType.PARAGRAPH, test)

    def test_unordered_list(self):
        text = """
            - ahora
            - nunca
            -mas
        """
        test = block_to_block_type(text)
        self.assertEqual(BlockType.UNORDERED_LIST, test)

    def test_ordered_list(self):
        text = """
            1. ahora
            2. nunca
            3.mas
        """
        test = block_to_block_type(text)
        self.assertEqual(BlockType.ORDERED_LIST, test)

    def test_not_ordered_list(self):
        text = """
            1. ahora
            2. nunca
            4.mas
        """
        test = block_to_block_type(text)
        self.assertEqual(BlockType.PARAGRAPH, test)
