from dataclasses import dataclass
from typing import Iterator

@dataclass(frozen=True)
class Field:
    id: int
    name: str
    value: str


class Form:

    def __init__(self,name: str, fields: list[Field]) -> None:
        if len({f.name for f in fields}) != len(fields):
            raise ValueError("Duplicate field names in form")

        self.name = name
        self._fields: dict[str, Field] = {f.name: f for f in fields}

    def __iter__(self) -> Iterator[Field]:
        return iter(self._fields.values())

    def __getitem__(self, name: str) -> Field:
        return self._fields[name]
    
    def __contains__(self, name: str) -> bool:
        return name in self._fields
    
    def __str__(self) -> str:
        header = f'Form(name={self.name})\n'
        fields = '\n'.join(str(f) for f in self._fields.values())
        return header + fields
    
    def __len__(self) -> int:
        return len(self._fields)
    
    def __add__(self, another: 'Form') -> 'Form':
        values = (self._fields | another._fields).values()
        new_fields = list(values)
        return Form(name=self.name+another.name, fields=new_fields)
