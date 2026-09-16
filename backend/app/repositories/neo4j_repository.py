from neo4j import GraphDatabase

from app.core.config import settings


class Neo4jRepository:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(
                settings.NEO4J_USERNAME,
                settings.NEO4J_PASSWORD
            )
        )

    def verify_connection(self) -> bool:

        try:

            with self.driver.session() as session:

                result = session.run(
                    "RETURN 1 AS value"
                )

                record = result.single()

                return record["value"] == 1

        except Exception:

            return False

    def upsert_entity(
        self,
        name: str,
        entity_type: str
    ):

        with self.driver.session() as session:

            result = session.run(
                """
                MERGE (e:Entity {
                    name: $name,
                    type: $entity_type
                })
                RETURN e
                """,
                name=name,
                entity_type=entity_type
            )

            return result.single()
    def upsert_relationship(
        self,
        source_name: str,
        source_type: str,
        target_name: str,
        target_type: str,
        relationship_type: str,
        confidence: float | None = None,
        evidence: str | None = None
    ):

        safe_relationship_type = relationship_type.upper()

        with self.driver.session() as session:

            query = f"""
                MERGE (source:Entity {{
                    name: $source_name,
                    type: $source_type
                }})

                MERGE (target:Entity {{
                    name: $target_name,
                    type: $target_type
                }})

                MERGE (source)-[r:{safe_relationship_type}]->(target)

                SET r.confidence = $confidence,
                    r.evidence = $evidence

                RETURN r
            """

            result = session.run(
                query,
                source_name=source_name,
                source_type=source_type,
                target_name=target_name,
                target_type=target_type,
                confidence=confidence,
                evidence=evidence
            )

            return result.single()
    def close(self):

        self.driver.close()