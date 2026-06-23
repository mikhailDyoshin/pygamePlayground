from typing import NamedTuple

class Field(NamedTuple):
    name: str
    value: str


class Form:
    def __init__(self, fields: list[Field]) -> None:
        

        self._fields = fields


    def __len__(self):
        return len(self._fields)
    
    def __getitem__(self, position: int) -> Field:
        return self._fields[position]
    

fields = [
    Field(name='IP', value='124.0.0.1'),
    Field(name='Port', value='5432'),
    Field(name='Plugin', value='handle_errors.cpp')
]

form = Form(fields)

print(f'Fields in form ({len(form)}):')
for field in form:
    print(f'\t{field}')

print(f'The last field: \n\t{form[-1]}')

field_to_check = fields[0]

print(f'Is the field {field_to_check} in the form?')
field_in_form = 'Yes' if field_to_check in form else 'No'
print(f'\t{field_in_form}')

slice = form[:2]

print()