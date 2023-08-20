from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_key_response_dto import APIKeyResponseDto


T = TypeVar("T", bound="APIKeyCreateResponseDto")


@_attrs_define
class APIKeyCreateResponseDto:
    """
    Attributes:
        api_key (APIKeyResponseDto):
        secret (str):
    """

    api_key: "APIKeyResponseDto"
    secret: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key = self.api_key.to_dict()

        secret = self.secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_key_response_dto import APIKeyResponseDto

        d = src_dict.copy()
        api_key = APIKeyResponseDto.from_dict(d.pop("apiKey"))

        secret = d.pop("secret")

        api_key_create_response_dto = cls(
            api_key=api_key,
            secret=secret,
        )

        api_key_create_response_dto.additional_properties = d
        return api_key_create_response_dto

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
