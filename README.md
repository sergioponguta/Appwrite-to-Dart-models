# APPWRITE COLLECTIONS TO DART MODELS

![Logo](/img/0.png)

## 📝 Description

This function will convert an [appwrite.json](https://appwrite.io/docs/command-line-deployment#appwriteJSON) file, from Appwrite [Appwrite](https://github.com/appwrite). To `dart` files with the models of the collections in the `appwrite.json`.

It will iterates over every collection in that file an produce a new file with the same name as the collection. The output will be a `dart` file with the model of the collection.

## 🚀 How to use it

### **Input:**

Just put your `appwrite.json` file in the `json` folder and run the `main.py` function. You will get the `dart` files with the models in the `dart` folder.

**Expected format** (Just a normal `appwrite.json` file):

```json
{
  "projectId": "test",
  "projectName": "TEST",
  "collections": [
    {
      "$id": "countries",
      "$createdAt": "2023-04-27T16:11:07.400446+00:00",
      "$updatedAt": "2023-04-27T16:11:07.400446+00:00",
      "$permissions": [],
      "databaseId": "test_db",
      "name": "COUNTRIES",
      "enabled": true,
      "attributes": [
        {
          "key": "id_country",
          "type": "integer",
          "status": "available",
          "required": true,
          "array": false,
          "default": null,
          "min": -9223372036854775808,
          "max": 9223372036854775807
        },
        {
          "key": "name_country",
          "type": "string",
          "status": "available",
          "required": true,
          "array": false,
          "default": null,
          "size": 30
        }
      ],
      "indexes": [
        {
          "key": "IDX_COUNTRY_PK",
          "type": "unique",
          "status": "available",
          "attributes": ["id_country"],
          "orders": ["DESC"]
        }
      ]
    }
  ]
}
```

### **Output:**

```dart
import 'dart:convert';

class Countries {
  int idCountry;
  String nameCountry;

  Countries({
    required this.idCountry,
    required this.nameCountry,
  });

  Countries copyWith({
    int? idCountry,
    String? nameCountry,
  }) {
    return Countries(
      idCountry: idCountry ?? this.idCountry,
      nameCountry: nameCountry ?? this.nameCountry,
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'id_country': idCountry,
      'name_country': nameCountry,
    };
  }

  factory Countries.fromMap(Map<String, dynamic> map) {
    return Countries(
      idCountry: map['id_country'],
      nameCountry: map['name_country'],
    );
  }

  String toJson() => json.encode(toMap());

  factory Countries.fromJson(String source) => Countries.fromMap(json.decode(source));

  @override
  String toString() {
    return 'Countries(idCountry: $idCountry, nameCountry: $nameCountry)';
  }

  @override
  bool operator ==(Object other) {
    if (identical(this, other)) return true;
    return other is Countries &&
      other.idCountry == idCountry &&
      other.nameCountry == nameCountry;
  }

  @override
  int get hashCode {
    return
      idCountry.hashCode ^
      nameCountry.hashCode;
  }
}
```

## 👉 Example

There is already an example inside the `json` folder. It's an `appwrite.json` file. Run the function and you will get the `dart` files in the `dart` folder.

## 📷 Screenshots

![Download](/img/1.png)

## ✅ TODO

- [x] Read `appwrite.json` from json folder
- [x] Generate separate dart files
- [x] Support for `integer` datatype
- [x] Support for `string` datatype
- [x] Support for `boolean` datatype
- [x] Support for `datetime` datatype
- [x] Support for `double` datatype
- [ ] Create input parameters on main to specify the input file and output folders
