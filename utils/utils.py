def to_camel_case(snake_str):
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))


def to_lower_camel_case(snake_str):
    camel_string = to_camel_case(snake_str)
    return snake_str[0].lower() + camel_string[1:]


# def plural_to_singular(snake_str: str):
#     if snake_str.endswith("es"):
#         return snake_str[:-2]
#     elif snake_str.endswith("s"):
#         return snake_str[:-1]
