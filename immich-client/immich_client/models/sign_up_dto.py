from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SignUpDto")


@_attrs_define
class SignUpDto:
    """
    Attributes:
        email (str):  Example: testuser@email.com.
        first_name (str):  Example: Admin.
        last_name (str):  Example: Doe.
        password (str):  Example: password.
    """

    email: str
    first_name: str
    last_name: str
    password: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        first_name = self.first_name
        last_name = self.last_name
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        password = d.pop("password")

        sign_up_dto = cls(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        sign_up_dto.additional_properties = d
        return sign_up_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
