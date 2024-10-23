from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.avatar_response import AvatarResponse
    from ..models.download_response import DownloadResponse
    from ..models.email_notifications_response import EmailNotificationsResponse
    from ..models.folders_response import FoldersResponse
    from ..models.memories_response import MemoriesResponse
    from ..models.people_response import PeopleResponse
    from ..models.purchase_response import PurchaseResponse
    from ..models.ratings_response import RatingsResponse
    from ..models.tags_response import TagsResponse


T = TypeVar("T", bound="UserPreferencesResponseDto")


@_attrs_define
class UserPreferencesResponseDto:
    """
    Attributes:
        avatar (AvatarResponse):
        download (DownloadResponse):
        email_notifications (EmailNotificationsResponse):
        folders (FoldersResponse):
        memories (MemoriesResponse):
        people (PeopleResponse):
        purchase (PurchaseResponse):
        ratings (RatingsResponse):
        tags (TagsResponse):
    """

    avatar: "AvatarResponse"
    download: "DownloadResponse"
    email_notifications: "EmailNotificationsResponse"
    folders: "FoldersResponse"
    memories: "MemoriesResponse"
    people: "PeopleResponse"
    purchase: "PurchaseResponse"
    ratings: "RatingsResponse"
    tags: "TagsResponse"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avatar = self.avatar.to_dict()

        download = self.download.to_dict()

        email_notifications = self.email_notifications.to_dict()

        folders = self.folders.to_dict()

        memories = self.memories.to_dict()

        people = self.people.to_dict()

        purchase = self.purchase.to_dict()

        ratings = self.ratings.to_dict()

        tags = self.tags.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatar": avatar,
                "download": download,
                "emailNotifications": email_notifications,
                "folders": folders,
                "memories": memories,
                "people": people,
                "purchase": purchase,
                "ratings": ratings,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.avatar_response import AvatarResponse
        from ..models.download_response import DownloadResponse
        from ..models.email_notifications_response import EmailNotificationsResponse
        from ..models.folders_response import FoldersResponse
        from ..models.memories_response import MemoriesResponse
        from ..models.people_response import PeopleResponse
        from ..models.purchase_response import PurchaseResponse
        from ..models.ratings_response import RatingsResponse
        from ..models.tags_response import TagsResponse

        d = src_dict.copy()
        avatar = AvatarResponse.from_dict(d.pop("avatar"))

        download = DownloadResponse.from_dict(d.pop("download"))

        email_notifications = EmailNotificationsResponse.from_dict(d.pop("emailNotifications"))

        folders = FoldersResponse.from_dict(d.pop("folders"))

        memories = MemoriesResponse.from_dict(d.pop("memories"))

        people = PeopleResponse.from_dict(d.pop("people"))

        purchase = PurchaseResponse.from_dict(d.pop("purchase"))

        ratings = RatingsResponse.from_dict(d.pop("ratings"))

        tags = TagsResponse.from_dict(d.pop("tags"))

        user_preferences_response_dto = cls(
            avatar=avatar,
            download=download,
            email_notifications=email_notifications,
            folders=folders,
            memories=memories,
            people=people,
            purchase=purchase,
            ratings=ratings,
            tags=tags,
        )

        user_preferences_response_dto.additional_properties = d
        return user_preferences_response_dto

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
