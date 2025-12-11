import logging
from .. import Neo4jClient
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

class Neo4jRepo:
    def __init__(self, database, uri: str, username: str, password: str):
        """Initialize the Neo4j repository and establish a connection."""
        self._client = Neo4jClient(uri)
        self._driver = self._client.connect(username, password, database)
        self._database = database

        logger.info("Neo4jRepo initialized successfully.")

    def execute_query(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Execute a Cypher query and return the results as a list of dictionaries.
        """
        try:
            assert self._driver, RuntimeError("Neo4j driver is not initialized.")
            parameters = parameters or {}
            with self._driver.session() as session:
                result = session.run(query, parameters=parameters)
                data = [record.data() for record in result]
                print(f"Executed query: {query} with params: {parameters}, returned {len(data)} rows.")
                return data
        except Exception as e:
            logger.exception(f"Failed to execute query: {query}, error: {e}")

    def create_node(self, label: str, properties: Dict[str, Any]) -> bool:
        """
        Create a node with a given label and properties.
        """
        try:
            assert self._driver, RuntimeError("Neo4j driver is not initialized.")
            properties = properties or {}
            query = f"CREATE (n:{label} $props)"
            with self._driver.session() as session:
                session.run(query, props=properties)
                print(f"Node with label '{label}' created successfully.")
                return True
        except Exception as e:
            logger.exception(f"Failed to create node with label '{label}': {e}")

    # def create_nodes(self, labels: List[str], properties_list: List[Dict[str, Any]]) -> bool:
    #     """
    #     Create multiple nodes with given labels and properties.
    #     """
    #     try:
    #         assert self._driver, RuntimeError("Neo4j driver is not initialized.")
    #         if len(labels) != len(properties_list):
    #             raise ValueError("Labels and properties_list must have the same length.")
    #         with self._driver.session() as session:
    #             for label, properties in zip(labels, properties_list):
    #                 query = f"CREATE (n:{label} $props)"
    #                 session.run(query, props=properties)
    #             print(f"{len(labels)} nodes created successfully.")
    #             return True
    #     except Exception as e:
    #         logger.exception(f"Failed to create multiple nodes: {e}")

    def create_relationship(self, from_label: str, from_key: Dict[str, Any],
                            to_label: str, to_key: Dict[str, Any],
                            rel_type: str, rel_props: Optional[Dict[str, Any]] = None) -> bool:
        """
        Create a relationship between two nodes.
        """
        try:
            assert self._driver, RuntimeError("Neo4j driver is not initialized.")
            rel_props = rel_props or {}
            query = (
                f"MATCH (a:{from_label}), (b:{to_label}) "
                f"WHERE ALL(k IN keys($from_key) WHERE a[k] = $from_key[k]) "
                f"AND ALL(k IN keys($to_key) WHERE b[k] = $to_key[k]) "
                f"CREATE (a)-[r:{rel_type} $rel_props]->(b)"
            )
            with self._driver.session() as session:
                session.run(query, rel_props=rel_props, from_key=from_key, to_key=to_key)
                print(f"Relationship '{rel_type}' created between {from_label} and {to_label}.")
                return True
        except Exception as e:
            logger.exception(f"Failed to create relationship '{rel_type}': {e}")

    def find_nodes(self, label: str, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Find nodes by label and optional filters.
        """
        try:
            assert self._driver, RuntimeError("Neo4j driver is not initialized.")
            filters = filters or {}
            query = f"MATCH (n:{label} $filters) RETURN n"
            with self._driver.session() as session:
                result = session.run(query, filters=filters)
                data = [record["n"] for record in result]
                print(f"Found {len(data)} nodes with label '{label}' and filters {filters}.")
                return data
        except Exception as e:
            logger.exception(f"Failed to find nodes with label '{label}': {e}")

    def update_node(self, label: str, match_props: Dict[str, Any], update_props: Dict[str, Any]) -> int:
        """
        Update node properties based on a match filter.
        """
        try:
            assert self._driver, RuntimeError("Neo4j driver is not initialized.")
            query = f"MATCH (n:{label} $match_props) SET n += $update_props RETURN COUNT(n) AS count"
            with self._driver.session() as session:
                result = session.run(query, match_props=match_props, update_props=update_props)
                count = result.single()["count"]
                print(f"Updated {count} node(s) with label '{label}'.")
                return count
        except Exception as e:
            logger.exception(f"Failed to update node with label '{label}': {e}")

    def delete_node(self, label: str, match_props: Dict[str, Any]) -> int:
        """
        Delete nodes matching given properties.
        """
        try:
            assert self._driver, RuntimeError("Neo4j driver is not initialized.")
            query = f"MATCH (n:{label} $match_props) DETACH DELETE n RETURN COUNT(n) AS count"
            with self._driver.session() as session:
                result = session.run(query)
                count = result.single()["count"]
                print(f"Deleted {count} node(s) with label '{label}'.")
                return count
        except Exception as e:
            logger.exception(f"Failed to delete node with label '{label}': {e}")

    def close(self):
        """Close the Neo4j driver connection."""
        try:
            assert self._driver, RuntimeError("Neo4j driver is not initialized.")
            self._driver.close()
            logger.info("Neo4j driver closed successfully.")
        except Exception as e:
            logger.exception(f"Failed to close Neo4j driver: {e}")

    def verify_connection(self) -> bool:
        """Verify the connectivity to the Neo4j database."""
        try:
            assert self._driver, RuntimeError("Neo4j driver is not initialized.")
            is_connected = self._driver.verify_connectivity()
            logger.info(f"Neo4j connectivity verified: {is_connected}")
            return is_connected
        except Exception as e:
            logger.exception(f"Failed to verify Neo4j connectivity: {e}")
        