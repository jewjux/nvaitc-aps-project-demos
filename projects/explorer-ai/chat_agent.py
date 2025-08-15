# Copyright 2024 NVIDIA Corporation and Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_community.chat_models import ChatOllama
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()
agents = {}
checkpointer = None


def get_checkpoint(thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}
    global checkpointer
    if checkpointer is None:
        # open the sqlite file (will create it if it doesn’t exist)
        conn = sqlite3.connect("data/curiosity.db", check_same_thread=False)
        checkpointer = SqliteSaver(conn)
    return checkpointer.get(config)


def get_agent(model_id: str):
    global agents, checkpointer
    if not model_id in agents:
        search = TavilySearchResults(max_results=5, include_images=True)
        tools = [search]
        if checkpointer is None:
            conn = sqlite3.connect("data/curiosity.db", check_same_thread=False)
            checkpointer = SqliteSaver(conn)
        cp = checkpointer
        if model_id == "nvdev/meta/llama-3.1-405b-instruct":
            model = ChatNVIDIA(model=model_id, nvidia_api_key=os.environ["NVIDIA_API_KEY"], base_url="https://integrate.api.nvidia.com/v1", temperature=0)
        elif model_id == "nvdev/meta/llama-3.2-3b-instruct":
            model = ChatNVIDIA(model=model_id, nvidia_api_key=os.environ["NVIDIA_API_KEY"], base_url="https://integrate.api.nvidia.com/v1", temperature=0)
        elif model_id == "nvdev/meta/llama-3.3-70b-instruct":
            model = ChatNVIDIA(model=model_id, nvidia_api_key=os.environ["NVIDIA_API_KEY"], base_url="https://integrate.api.nvidia.com/v1", temperature=0)
        else:
            raise Exception(f"Model not supported: {model_id}")
        agent = create_react_agent(model, tools, checkpointer=cp)
        agents[model_id] = agent
    return agents[model_id]
