"""
    - This class is a Pydantic model which is used for data validation.
    - Schema validation and serialization are controlled by type annotations.
    - It can emit JSON schema, hence easy integration.
    - Here we are defining the fields(parameters for RAG) while creating a RAG agent and creating
        methods to save it into local cache and load it from local cache
"""
import uuid
from pathlib import Path

from pydantic import BaseModel, Field
from typing import (
    List,
    cast,
    Optional,
)
from llama_index import (
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.chat_engine.types import BaseChatEngine


class ParamCache(BaseModel):
    """
    Cache for RAG agent builder

    """

    # system prompt for RAG agent
    # We need to study more prompt engineering TODO
    system_prompt: Optional[str] = Field(
        default=None, description="System prompt for RAG agent."
    )

    # File names - currently we are supporting only File names
    file_names: List[str] = Field(
        default_factory=list,
        description="File names as data source"
    )

    # urls and directories TODO

    docs: List = Field(default_factory=list,
                       description="Documents for RAG agent to analyze.")

    # tools TODO

    # rag_params like include summarization, top_k, chunk_size etc. TODO

    # builder type default or multimodal(We are not doing multimodal in MVP) TODO

    # vector index, I am not setting this Optional, since we are using Milvus

    vector_index: VectorStoreIndex = Field(
        default=None, description="Vector index for RAG agent."
    )

    # unique agent id
    agent_id: str = Field(
        default_factory=lambda: f"Agent_{str(uuid.uuid4())}",
        description="Agent ID for RAG agent."
    )

    agent: Optional[BaseChatEngine] = Field(default=None, description="RAG agent.")

    def save_to_disk(self, save_dir: str) -> None:
        """Save parameters to local cache"""

        dict_to_serialize = {
            "system_prompt": self.system_prompt,
            "file_names": self.file_names,
            # TODO urls
            # TODO directory
            # TODO tools
            # TODO rag params
            # TODO builder type
            "agent_id": self.agent_id,
        }

        if self.vector_index is None:
            raise ValueError("Must specify vector index in order to save.")
        self.vector_index.storage_context.persist(Path(save_dir) / "storage")
