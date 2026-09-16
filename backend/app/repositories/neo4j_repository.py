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
    def close(self):

        self.driver.close()