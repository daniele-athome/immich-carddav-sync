from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audio_codec import AudioCodec
from ..models.cq_mode import CQMode
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
        bframes (int):
        cq_mode (CQMode):
        crf (int):
        gop_size (int):
        max_bitrate (str):
        npl (int):
        preset (str):
        refs (int):
        target_audio_codec (AudioCodec):
        target_resolution (str):
        target_video_codec (VideoCodec):
        temporal_aq (bool):
        threads (int):
        tonemap (ToneMapping):
        transcode (TranscodePolicy):
        two_pass (bool):
    """

    accel: TranscodeHWAccel
    bframes: int
    cq_mode: CQMode
    crf: int
    gop_size: int
    max_bitrate: str
    npl: int
    preset: str
    refs: int
    target_audio_codec: AudioCodec
    target_resolution: str
    target_video_codec: VideoCodec
    temporal_aq: bool
    threads: int
    tonemap: ToneMapping
    transcode: TranscodePolicy
    two_pass: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accel = self.accel.value

        bframes = self.bframes
        cq_mode = self.cq_mode.value

        crf = self.crf
        gop_size = self.gop_size
        max_bitrate = self.max_bitrate
        npl = self.npl
        preset = self.preset
        refs = self.refs
        target_audio_codec = self.target_audio_codec.value

        target_resolution = self.target_resolution
        target_video_codec = self.target_video_codec.value

        temporal_aq = self.temporal_aq
        threads = self.threads
        tonemap = self.tonemap.value

        transcode = self.transcode.value

        two_pass = self.two_pass

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accel": accel,
                "bframes": bframes,
                "cqMode": cq_mode,
                "crf": crf,
                "gopSize": gop_size,
                "maxBitrate": max_bitrate,
                "npl": npl,
                "preset": preset,
                "refs": refs,
                "targetAudioCodec": target_audio_codec,
                "targetResolution": target_resolution,
                "targetVideoCodec": target_video_codec,
                "temporalAQ": temporal_aq,
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

        bframes = d.pop("bframes")

        cq_mode = CQMode(d.pop("cqMode"))

        crf = d.pop("crf")

        gop_size = d.pop("gopSize")

        max_bitrate = d.pop("maxBitrate")

        npl = d.pop("npl")

        preset = d.pop("preset")

        refs = d.pop("refs")

        target_audio_codec = AudioCodec(d.pop("targetAudioCodec"))

        target_resolution = d.pop("targetResolution")

        target_video_codec = VideoCodec(d.pop("targetVideoCodec"))

        temporal_aq = d.pop("temporalAQ")

        threads = d.pop("threads")

        tonemap = ToneMapping(d.pop("tonemap"))

        transcode = TranscodePolicy(d.pop("transcode"))

        two_pass = d.pop("twoPass")

        system_config_f_fmpeg_dto = cls(
            accel=accel,
            bframes=bframes,
            cq_mode=cq_mode,
            crf=crf,
            gop_size=gop_size,
            max_bitrate=max_bitrate,
            npl=npl,
            preset=preset,
            refs=refs,
            target_audio_codec=target_audio_codec,
            target_resolution=target_resolution,
            target_video_codec=target_video_codec,
            temporal_aq=temporal_aq,
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
