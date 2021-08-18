# Storage-mechanism-JSON-format
The project implements a simple JSON formatted storage mechanism to store documents. The document structure can be arbitrary and we need to return all the entities that match the given query

There are three allowed commands:
- add_record: stores the given document.
- get_record: find all the documents having the same properties and values and print them out.
- delete_record: removes all the documents matching the properties and values.

### Example Input 1:
```
add_record {"id":100,"lastname":"Peck","firstname":"Jane","location":{"city":"Binghamton","state":"NY","postalCode":"13905"},"active":true}
add_record {"id":101,"lastname":"Gardner","firstname":"Stanley","location":{"city":"Buffalo","state":"NY","postalCode":"14201"},"active":true}
add_record {"id":103,"lastname":"Cross","firstname":"Victor","location":{"city":"San Francisco","state":"CA","postalCode":"94105"},"active":true}
add_record {"id":104,"lastname":"Peck","firstname":"Jane","location":{"city":"Seattle","state":"WA","postalCode":"98204"},"active":false}
get_record {"location":{"state":"NY"},"active":true}
get_record {"id":101}

```
#### Output:
```
{"id":100,"lastname":"Peck","firstname":"Jane","location":{"city":"Binghamton","state":"NY","postalCode":"13905"},"active":true}
{"id":101,"lastname":"Gardner","firstname":"Stanley","location":{"city":"Buffalo","state":"NY","postalCode":"14201"},"active":true}
{"id":101,"lastname":"Gardner","firstname":"Stanley","location":{"city":"Buffalo","state":"NY","postalCode":"14201"},"active":true}
```

### Example Input 2:
```
add_record {"id":100,"lastname":"Peck","firstname":"Jane","location":{"city":"Binghamton","state":"NY","postalCode":"13905"},"active":true}
add_record {"id":101,"lastname":"Gardner","firstname":"Stanley","location":{"city":"Buffalo","state":"NY","postalCode":"14201"},"active":true}
add_record {"id":103,"lastname":"Cross","firstname":"Victor","location":{"city":"San Francisco","state":"CA","postalCode":"94105"},"active":true}
add_record {"id":104,"lastname":"Peck","firstname":"Jane","location":{"city":"Seattle","state":"WA","postalCode":"98204"},"active":false}
delete_record {"active":true}
get_record {}

```

#### Output:
```
{"id":104,"lastname":"Peck","firstname":"Jane","location":{"city":"Seattle","state":"WA","postalCode":"98204"},"active":false}
```

We need to observe that the documents must be in the exact same format as they were in the input without changing any order. Multiple documents match the properties then we need to emit in the order they were created.

## Handling Lists

This is an additional part of the problem where our mechanism should also support lists in expressions.
### Example Input 3:
```
add_record {"type":"list","list":[11,12,13,14]}
add_record {"type":"list","list":[12,13,14,15]}
add_record {"type":"list","list":[13,14,15,16]}
add_record {"type":"list","list":[14,15,16,17]}
add_record {"type":"list","list":[15,16,17,18]}
add_record {"type":"list","list":[16,17,18,19]}
get_record {"type":"list","list":[11]}
get_record {"type":"list","list":[13,14]}
```
#### Output:
```
{"type":"list","list":[11,12,13,14]}
{"type":"list","list":[11,12,13,14]}
{"type":"list","list":[12,13,14,15]}
{"type":"list","list":[13,14,15,16]}
```

## Terms and Policies

- This repository contains resources that are referenced from multiple online platforms. Users should use the resources for open source projects and self/ non-commercial purposes.
- If any conflict arises, the **user** shall be liable for the damage caused and not the Repository Owner.
- The Repository owner has published some propriety data and intellectual property of others for **ACADEMIC purpose only**.
- Which shall be referred by the user at his **own risk!** If found to be used for any non-Academic usage, **the user shall be liable for any legal proceedings caused in any jurisdiction.**

## Usage

Thank you for visiting my projects. Please use this repository wisely and strictly for Academic Purposes only. If any conflict arises report or contact me directly via email at connect@adityachaudhari.dev

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
No Licenses are required as of now. Users are requested to use the repository wisely.