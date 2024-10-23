from enum import Enum


class JobName(str, Enum):
    BACKGROUNDTASK = "backgroundTask"
    DUPLICATEDETECTION = "duplicateDetection"
    FACEDETECTION = "faceDetection"
    FACIALRECOGNITION = "facialRecognition"
    LIBRARY = "library"
    METADATAEXTRACTION = "metadataExtraction"
    MIGRATION = "migration"
    NOTIFICATIONS = "notifications"
    SEARCH = "search"
    SIDECAR = "sidecar"
    SMARTSEARCH = "smartSearch"
    STORAGETEMPLATEMIGRATION = "storageTemplateMigration"
    THUMBNAILGENERATION = "thumbnailGeneration"
    VIDEOCONVERSION = "videoConversion"

    def __str__(self) -> str:
        return str(self.value)
