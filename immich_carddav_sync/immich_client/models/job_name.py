from enum import Enum


class JobName(str, Enum):
    BACKGROUNDTASK = "backgroundTask"
    LIBRARY = "library"
    METADATAEXTRACTION = "metadataExtraction"
    MIGRATION = "migration"
    OBJECTTAGGING = "objectTagging"
    RECOGNIZEFACES = "recognizeFaces"
    SEARCH = "search"
    SIDECAR = "sidecar"
    SMARTSEARCH = "smartSearch"
    STORAGETEMPLATEMIGRATION = "storageTemplateMigration"
    THUMBNAILGENERATION = "thumbnailGeneration"
    VIDEOCONVERSION = "videoConversion"

    def __str__(self) -> str:
        return str(self.value)
