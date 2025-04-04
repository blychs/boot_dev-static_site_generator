from blocktype import *
from block_to_html import markdown_to_html_node

text = """
    -hola
- Yo
-soy

** test of sanity **

_why?_

![viva la pepa](viva-la-pepa.com)
"""

print(markdown_to_html_node(text))
exit()

text = """
    1. lala
2. 2345
3. comida
"""

print(block_to_block_type(text))
text = """
    # lala
"""

print(block_to_block_type(text))
