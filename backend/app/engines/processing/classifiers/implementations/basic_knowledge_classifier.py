from app.engines.processing.classifiers.base.base_knowledge_classifier import (
    BaseKnowledgeClassifier
)

from app.engines.processing.models.knowledge_classification import (
    KnowledgeClassification
)


class BasicKnowledgeClassifier(BaseKnowledgeClassifier):

    def classify(
        self,
        text: str
    ) -> KnowledgeClassification:

        if not text or not text.strip():

            return KnowledgeClassification(
                knowledge_type="UNKNOWN",
                confidence=1.0
            )

        normalized_text = text.lower()

        # Architecture decisions
        architecture_keywords = [
            "we decided",
            "we chose",
            "chosen because",
            "introduced because",
            "architecture decision",
            "design decision"
        ]

        if any(
            keyword in normalized_text
            for keyword in architecture_keywords
        ):

            return KnowledgeClassification(
                knowledge_type="ARCHITECTURE_DECISION",
                confidence=0.90
            )

        # Procedures
        procedure_keywords = [
            "run ",
            "restart ",
            "install ",
            "configure ",
            "deploy ",
            "before restarting",
            "steps to"
        ]

        if any(
            keyword in normalized_text
            for keyword in procedure_keywords
        ):

            return KnowledgeClassification(
                knowledge_type="PROCEDURE",
                confidence=0.85
            )

        # Troubleshooting
        troubleshooting_keywords = [
            "error",
            "failed",
            "failure",
            "issue",
            "problem",
            "because"
        ]

        if any(
            keyword in normalized_text
            for keyword in troubleshooting_keywords
        ):

            return KnowledgeClassification(
                knowledge_type="TROUBLESHOOTING",
                confidence=0.80
            )

        # Requirements
        requirement_keywords = [
            "must",
            "should",
            "required",
            "requirement"
        ]

        if any(
            keyword in normalized_text
            for keyword in requirement_keywords
        ):

            return KnowledgeClassification(
                knowledge_type="REQUIREMENT",
                confidence=0.80
            )

        # General technical knowledge
        technical_keywords = [
            "uses",
            "service",
            "database",
            "api",
            "authentication",
            "redis",
            "python",
            "java",
            "fastapi"
        ]

        if any(
            keyword in normalized_text
            for keyword in technical_keywords
        ):

            return KnowledgeClassification(
                knowledge_type="TECHNICAL_KNOWLEDGE",
                confidence=0.70
            )

        return KnowledgeClassification(
            knowledge_type="GENERAL",
            confidence=0.50
        )