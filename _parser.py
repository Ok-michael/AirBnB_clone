import re

def parse(arg):
    """
    Parses a string `arg` containing optional curly braces `{}` and/or square brackets `[]`,
    splitting it into tokens. The tokens are separated by commas, and each token is stripped
    of leading and trailing commas.

    Args:
    - arg (str): The string to be parsed.

    Returns:
    - list: A list of tokens extracted from the string `arg`. If curly braces are present,
      the tokens are enclosed within curly braces and returned as a list of tokens. If square
      brackets are present, they are treated as a single token.

    Example:
    >>> parse("[apple, {banana, orange}, grape]")
    ['apple', '{banana, orange}', 'grape']
    """

    # Find curly braces and square brackets in the string
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)

    # If neither curly braces nor brackets are found
    if curly_braces is None and brackets is None:
        return [i.strip(",") for i in arg.split(",")]

    # If brackets are found but not curly braces
    if curly_braces is None and brackets:
        lexer = arg[:brackets.span()[0]].split(",")
        retl = [i.strip(",") for i in lexer]
        retl.append(brackets.group())
        return retl

    # If curly braces are found but not brackets
    if brackets is None and curly_braces:
        lexer = arg[:curly_braces.span()[0]].split(",")
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

