"""
General vibe:

- convert everything to unicode table
- annotate every cell with width
- calculate max width available (use border style here)
- backpropogate cell widths to column scores (average of all widths)
- while we have too little space
    - remove character from longest cell in widest column
        - widest is the column with highest std dev

"""

from builtins import str
from past.builtins import basestring


def _cellify(data):
    if isinstance(data, basestring):
        return str(data)
    return str(repr(data))


def _rowify(data):
    if isinstance(data, (list, set, tuple)):
        return [_cellify(d) for d in data]
    return [_cellify(data)]


def tablify(data, maxrows=10000):
    """
    Convert some incoming data structure to a 2D table with variable column counts.

    TODO: handle embedded style info (what lines are headers)

    Args:
        data (list, dict, tuple, set, generator): incoming data structure
        maxrows (int): maximum number of rows to use/consider (useful when consuming a generator)

    Returns:
        List[List[unicode]]: cells with unicode data strings
    """

    if isinstance(data, (list, set, tuple)):
        return [_rowify(row) for row in data]

    if isinstance(data, dict):
        return [_rowify(pair) for pair in data.items()]

    if isinstance(data, basestring):
        return [_rowify(data)]

    try:
        i = iter(data)
        count = 0
        newdata = []
        for item in i:
            newdata.append(_rowify(item))
            count += 1
            if count >= maxrows:
                break
        return newdata
    except Exception:
        pass

    return [_rowify(repr(data))]
