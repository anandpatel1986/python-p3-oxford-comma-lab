def oxford_comma(items):
    if len(items) == 1:
        return f"{items[0]}"
    elif len(items) == 2:
        return "{} and {}".format(items[0], items[1])
    else:
        return "{}, and {}".format(", ".join(items[:-1]), items[-1])
        