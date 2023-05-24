from utils.utils import to_lower_camel_case


def generate_class_name(json_dict):
    # class_name = plural_to_singular(to_lower_camel_case(json_dict["name"]))
    class_name = to_lower_camel_case(json_dict["name"])
    return class_name[0].upper() + class_name[1:]


def generate_attributes_camelcase(json_dict):
    attributes_cc = []
    for attribute in json_dict["attributes"]:
        attribute_name = to_lower_camel_case(attribute["key"])
        attribute_type = attribute["type"]
        if attribute_type == "string":
            attribute_type = "String"
        elif attribute_type == "integer":
            attribute_type = "int"
        elif attribute_type == "boolean":
            attribute_type = "bool"
        elif attribute_type == "double":
            attribute_type = "double"
        elif attribute_type == "date" or attribute_type == "datetime":
            attribute_type = "DateTime"
        attributes_cc.append(
            {"name": attribute_name, "type": attribute_type})
    return attributes_cc


def generate_attributes_snakecase(json_dict):
    attributes_snakecase = []
    for attribute in json_dict["attributes"]:
        attributes_snakecase.append(
            {"name": attribute["key"], "type": attribute["type"]})
    return attributes_snakecase


def dict_attributes_plus_id(json_dict):
    attributes = json_dict["attributes"]
    attributes.insert(0, {"key": "id", "type": "string"})
    return json_dict


def generate_import():
    return "import 'dart:convert';"


def generate_class_definition(class_name):
    return "class " + class_name + " {" + "\n"


def generate_attributes_string(attributes_cc):
    attributes_string = ""
    for attribute in attributes_cc:
        attributes_string += "  " + \
            attribute["type"] + " " + attribute["name"] + ";\n"
    return attributes_string + "\n"


def generate_constructor(class_name, attributes_cc):
    aux = ""
    aux += "  " + class_name + "({" + "\n"
    for attribute in attributes_cc:
        aux += "    required this." + attribute["name"] + "," + "\n"
    aux += "  });" + "\n"
    return aux + "\n"


def generate_copy_with(class_name, attributes_cc):
    aux = ""
    aux += "  " + class_name + " copyWith({" + "\n"
    for attribute in attributes_cc:
        aux += "    " + attribute["type"] + \
            "? " + attribute["name"] + "," + "\n"
    aux += "  }) {" + "\n"
    aux += "    return " + class_name + "(" + "\n"
    for attribute in attributes_cc:
        aux += "      " + attribute["name"] + ": " + \
            attribute["name"] + " ?? this." + attribute["name"] + "," + "\n"
    aux += "    );" + "\n"
    aux += "  }" + "\n"
    return aux + "\n"


def generate_to_map(attributes_snakecase):
    aux = ""
    aux += "  Map<String, dynamic> toMap() {" + "\n"
    aux += "    return {" + "\n"
    for attribute in attributes_snakecase:
        aux += "      '" + attribute["key"] + "': " + \
            to_lower_camel_case(attribute["key"]) + "," + "\n"
    aux += "    };" + "\n"
    aux += "  }" + "\n"
    return aux + "\n"


def generate_from_map(class_name, attributes_snakecase):
    aux = ""
    aux += "  factory " + class_name + \
        ".fromMap(Map<String, dynamic> map) {" + "\n"
    aux += "    return " + class_name + "(" + "\n"
    for attribute in attributes_snakecase:
        if to_lower_camel_case(attribute["key"]) == "id":
            aux += "      " + to_lower_camel_case(attribute["key"]) + ": map['\$" + \
                attribute["key"] + "'].toString()," + "\n"
        else:
            aux += "      " + to_lower_camel_case(attribute["key"]) + ": map['" + \
                attribute["key"] + "']," + "\n"
    aux += "    );" + "\n"
    aux += "  }" + "\n"
    return aux + "\n"


def generate_to_json():
    return "  String toJson() => json.encode(toMap());"


def generate_from_json(class_name):
    return "  factory " + class_name + ".fromJson(String source) => " + class_name + ".fromMap(json.decode(source));"


def generate_to_string(class_name, attributes_cc):
    aux = ""
    aux += "  @override" + "\n"
    aux += "  String toString() {" + "\n"
    aux += "    return '" + class_name + "("
    for attribute in attributes_cc:
        aux += attribute["name"] + ": $" + attribute["name"] + ", "
    aux = aux[:-2]
    aux += ")';" + "\n"
    aux += "  }" + "\n"
    return aux + "\n"


def generate_operator(class_name, attributes_cc):
    aux = ""
    aux += "  @override" + "\n"
    aux += "  bool operator ==(Object other) {" + "\n"
    aux += "    if (identical(this, other)) return true;" + "\n"
    aux += "    return other is " + class_name + " &&" + "\n"
    for attribute in attributes_cc:
        aux += "      other." + \
            attribute["name"] + " == " + attribute["name"] + " &&" + "\n"
    aux = aux[:-4] + "; \n"
    aux += "  }" + "\n"
    return aux + "\n"


def generate_hash_code(attributes_cc):
    aux = ""
    aux += "  @override" + "\n"
    aux += "  int get hashCode {" + "\n"
    aux += "    return " + "\n"
    for attribute in attributes_cc:
        aux += "      " + attribute["name"] + ".hashCode ^ " + "\n"
    aux = aux[:-4] + "; \n"
    aux += "  }" + "\n"
    return aux


def generate_class_end():
    return "}"


def json_to_dart_string(class_name, json_dict):
    attributes_camelcase = generate_attributes_camelcase(json_dict)
    attributes_snakecase = json_dict["attributes"]

    dart_content = ""
    dart_content += generate_import() + "\n" + "\n"
    dart_content += generate_class_definition(class_name)
    dart_content += generate_attributes_string(attributes_camelcase)
    dart_content += generate_constructor(class_name, attributes_camelcase)
    dart_content += generate_copy_with(class_name, attributes_camelcase)
    dart_content += generate_to_map(attributes_snakecase)
    dart_content += generate_from_map(class_name, attributes_snakecase)
    dart_content += generate_to_json() + "\n" + "\n"
    dart_content += generate_from_json(class_name) + "\n" + "\n"
    dart_content += generate_to_string(class_name, attributes_camelcase)
    dart_content += generate_operator(class_name, attributes_camelcase)
    dart_content += generate_hash_code(attributes_camelcase)
    dart_content += generate_class_end()

    return dart_content
