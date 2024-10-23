from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerAboutResponseDto")


@_attrs_define
class ServerAboutResponseDto:
    """
    Attributes:
        licensed (bool):
        version (str):
        version_url (str):
        build (Union[Unset, str]):
        build_image (Union[Unset, str]):
        build_image_url (Union[Unset, str]):
        build_url (Union[Unset, str]):
        exiftool (Union[Unset, str]):
        ffmpeg (Union[Unset, str]):
        imagemagick (Union[Unset, str]):
        libvips (Union[Unset, str]):
        nodejs (Union[Unset, str]):
        repository (Union[Unset, str]):
        repository_url (Union[Unset, str]):
        source_commit (Union[Unset, str]):
        source_ref (Union[Unset, str]):
        source_url (Union[Unset, str]):
        third_party_bug_feature_url (Union[Unset, str]):
        third_party_documentation_url (Union[Unset, str]):
        third_party_source_url (Union[Unset, str]):
        third_party_support_url (Union[Unset, str]):
    """

    licensed: bool
    version: str
    version_url: str
    build: Union[Unset, str] = UNSET
    build_image: Union[Unset, str] = UNSET
    build_image_url: Union[Unset, str] = UNSET
    build_url: Union[Unset, str] = UNSET
    exiftool: Union[Unset, str] = UNSET
    ffmpeg: Union[Unset, str] = UNSET
    imagemagick: Union[Unset, str] = UNSET
    libvips: Union[Unset, str] = UNSET
    nodejs: Union[Unset, str] = UNSET
    repository: Union[Unset, str] = UNSET
    repository_url: Union[Unset, str] = UNSET
    source_commit: Union[Unset, str] = UNSET
    source_ref: Union[Unset, str] = UNSET
    source_url: Union[Unset, str] = UNSET
    third_party_bug_feature_url: Union[Unset, str] = UNSET
    third_party_documentation_url: Union[Unset, str] = UNSET
    third_party_source_url: Union[Unset, str] = UNSET
    third_party_support_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        licensed = self.licensed

        version = self.version

        version_url = self.version_url

        build = self.build

        build_image = self.build_image

        build_image_url = self.build_image_url

        build_url = self.build_url

        exiftool = self.exiftool

        ffmpeg = self.ffmpeg

        imagemagick = self.imagemagick

        libvips = self.libvips

        nodejs = self.nodejs

        repository = self.repository

        repository_url = self.repository_url

        source_commit = self.source_commit

        source_ref = self.source_ref

        source_url = self.source_url

        third_party_bug_feature_url = self.third_party_bug_feature_url

        third_party_documentation_url = self.third_party_documentation_url

        third_party_source_url = self.third_party_source_url

        third_party_support_url = self.third_party_support_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "licensed": licensed,
                "version": version,
                "versionUrl": version_url,
            }
        )
        if build is not UNSET:
            field_dict["build"] = build
        if build_image is not UNSET:
            field_dict["buildImage"] = build_image
        if build_image_url is not UNSET:
            field_dict["buildImageUrl"] = build_image_url
        if build_url is not UNSET:
            field_dict["buildUrl"] = build_url
        if exiftool is not UNSET:
            field_dict["exiftool"] = exiftool
        if ffmpeg is not UNSET:
            field_dict["ffmpeg"] = ffmpeg
        if imagemagick is not UNSET:
            field_dict["imagemagick"] = imagemagick
        if libvips is not UNSET:
            field_dict["libvips"] = libvips
        if nodejs is not UNSET:
            field_dict["nodejs"] = nodejs
        if repository is not UNSET:
            field_dict["repository"] = repository
        if repository_url is not UNSET:
            field_dict["repositoryUrl"] = repository_url
        if source_commit is not UNSET:
            field_dict["sourceCommit"] = source_commit
        if source_ref is not UNSET:
            field_dict["sourceRef"] = source_ref
        if source_url is not UNSET:
            field_dict["sourceUrl"] = source_url
        if third_party_bug_feature_url is not UNSET:
            field_dict["thirdPartyBugFeatureUrl"] = third_party_bug_feature_url
        if third_party_documentation_url is not UNSET:
            field_dict["thirdPartyDocumentationUrl"] = third_party_documentation_url
        if third_party_source_url is not UNSET:
            field_dict["thirdPartySourceUrl"] = third_party_source_url
        if third_party_support_url is not UNSET:
            field_dict["thirdPartySupportUrl"] = third_party_support_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        licensed = d.pop("licensed")

        version = d.pop("version")

        version_url = d.pop("versionUrl")

        build = d.pop("build", UNSET)

        build_image = d.pop("buildImage", UNSET)

        build_image_url = d.pop("buildImageUrl", UNSET)

        build_url = d.pop("buildUrl", UNSET)

        exiftool = d.pop("exiftool", UNSET)

        ffmpeg = d.pop("ffmpeg", UNSET)

        imagemagick = d.pop("imagemagick", UNSET)

        libvips = d.pop("libvips", UNSET)

        nodejs = d.pop("nodejs", UNSET)

        repository = d.pop("repository", UNSET)

        repository_url = d.pop("repositoryUrl", UNSET)

        source_commit = d.pop("sourceCommit", UNSET)

        source_ref = d.pop("sourceRef", UNSET)

        source_url = d.pop("sourceUrl", UNSET)

        third_party_bug_feature_url = d.pop("thirdPartyBugFeatureUrl", UNSET)

        third_party_documentation_url = d.pop("thirdPartyDocumentationUrl", UNSET)

        third_party_source_url = d.pop("thirdPartySourceUrl", UNSET)

        third_party_support_url = d.pop("thirdPartySupportUrl", UNSET)

        server_about_response_dto = cls(
            licensed=licensed,
            version=version,
            version_url=version_url,
            build=build,
            build_image=build_image,
            build_image_url=build_image_url,
            build_url=build_url,
            exiftool=exiftool,
            ffmpeg=ffmpeg,
            imagemagick=imagemagick,
            libvips=libvips,
            nodejs=nodejs,
            repository=repository,
            repository_url=repository_url,
            source_commit=source_commit,
            source_ref=source_ref,
            source_url=source_url,
            third_party_bug_feature_url=third_party_bug_feature_url,
            third_party_documentation_url=third_party_documentation_url,
            third_party_source_url=third_party_source_url,
            third_party_support_url=third_party_support_url,
        )

        server_about_response_dto.additional_properties = d
        return server_about_response_dto

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
