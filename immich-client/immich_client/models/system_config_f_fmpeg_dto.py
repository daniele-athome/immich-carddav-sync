from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audio_codec import AudioCodec
from ..models.tone_mapping import ToneMapping
from ..models.transcode_hw_accel import TranscodeHWAccel
from ..models.transcode_policy import TranscodePolicy
from ..models.video_codec import VideoCodec

T = TypeVar("T", bound="SystemConfigFFmpegDto")


@_attrs_define
class SystemConfigFFmpegDto:
    """
    Attributes:
        accel (TranscodeHWAccel):
        crf (int):
        max_bitrate (str):
        preset (str):
        target_audio_codec (AudioCodec):
        target_resolution (str):
        target_video_codec (VideoCodec):
        threads (int):
        tonemap (ToneMapping):
        transcode (TranscodePolicy):
        two_pass (bool):
    """

    accel: TranscodeHWAccel
    crf: int
    max_bitrate: str
    preset: str
    target_audio_codec: AudioCodec
    target_resolution: str
    target_video_codec: VideoCodec
    threads: int
    tonemap: ToneMapping
    transcode: TranscodePolicy
    two_pass: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accel = self.accel.value

        crf = self.crf
        max_bitrate = self.max_bitrate
        preset = self.preset
        target_audio_codec = self.target_audio_codec.value

        target_resolution = self.target_resolution
        target_video_codec = self.target_video_codec.value

        threads = self.threads
        tonemap = self.tonemap.value

        transcode = self.transcode.value

        two_pass = self.two_pass

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accel": accel,
                "crf": crf,
                "maxBitrate": max_bitrate,
                "preset": preset,
                "targetAudioCodec": target_audio_codec,
                "targetResolution": target_resolution,
                "targetVideoCodec": target_video_codec,
                "threads": threads,
                "tonemap": tonemap,
                "transcode": transcode,
                "twoPass": two_pass,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        accel = TranscodeHWAccel(d.pop("accel"))

        crf = d.pop("crf")

        max_bitrate = d.pop("maxBitrate")

        preset = d.pop("preset")

        target_audio_codec = AudioCodec(d.pop("targetAudioCodec"))

        target_resolution = d.pop("targetResolution")

        target_video_codec = VideoCodec(d.pop("targetVideoCodec"))

        threads = d.pop("threads")

        tonemap = ToneMapping(d.pop("tonemap"))

        transcode = TranscodePolicy(d.pop("transcode"))

        two_pass = d.pop("twoPass")

        system_config_f_fmpeg_dto = cls(
            accel=accel,
            crf=crf,
            max_bitrate=max_bitrate,
            preset=preset,
            target_audio_codec=target_audio_codec,
            target_resolution=target_resolution,
            target_video_codec=target_video_codec,
            threads=threads,
            tonemap=tonemap,
            transcode=transcode,
            two_pass=two_pass,
        )

        system_config_f_fmpeg_dto.additional_properties = d
        return system_config_f_fmpeg_dto

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
