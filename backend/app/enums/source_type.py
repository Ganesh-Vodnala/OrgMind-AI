from enum import Enum


class SourceType(str, Enum):
    DOCUMENT = "document"
    GITHUB = "github"
    PULL_REQUEST = "pull_request"
    MEETING = "meeting"
    VOICE_NOTE = "voice_note"
    AI_JOURNAL = "ai_journal"
    MICRO_CAPTURE = "micro_capture"
    EXIT_INTERVIEW = "exit_interview"
    CONVERSATION = "conversation"