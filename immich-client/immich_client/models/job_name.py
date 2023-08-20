from enum import Enum


class JobName(str, Enum):
    BACKGROUNDTASK = "backgroundTask"
    CLIPENCODING = "clipEncoding"
    METADATAEXTRACTION = "metadataExtraction"
    OBJECTTAGGING = "objectTagging"
    RECOGNIZEFACES = "recognizeFaces"
    SEARCH = "search"
    SIDECAR = "sidecar"
    STORAGETEMPLATEMIGRATION = "storageTemplateMigration"
    THUMBNAILGENERATION = "thumbnailGeneration"
    VIDEOCONVERSION = "videoConversion"

    def __str__(self) -> str:
        return str(self.value)
