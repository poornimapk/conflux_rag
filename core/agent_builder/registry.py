from typing import Union
from pathlib import Path


class AgentCacheRegistry:
    """
    Create new agent, load agent, delete agent all saved
    in local cache at cache directory
    """
    # Constructor
    def __init__(self, dir: Union[str, Path]) -> None:
        self._dir = dir

    def add_new_agent_in_cache(self, agent_id: str):
        """
        - Create a new agent in local cache
        - Save the cache to disk #TODO
        """
        agent_cache_path = f"{self._dir}/{agent_id}"


