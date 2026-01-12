from google.adk.agents.llm_agent import Agent
from google.adk.tools.bigquery import BigQueryToolset
from typing import Any

from google.adk.agents import LlmAgent
from google.adk.apps.app import App
from google.adk.plugins import ReflectAndRetryToolPlugin
from google.adk.plugins import LoggingPlugin

USER_ID = "test_user"
bigquery_toolset = BigQueryToolset(tool_filter=[
'list_dataset_ids',
'get_dataset_info',
'list_table_ids',
'get_table_info',
'execute_sql',
     ])

class CustomRetryPlugin(ReflectAndRetryToolPlugin):

  async def extract_error_from_result(
      self, *, tool, tool_args, tool_context, result
  ):
    if isinstance(result, list):
      for item in result:
        if isinstance(item, dict) and item.get("status") == "error":
          return item
      return None
    return result if isinstance(result, dict) and result.get("status") == "error" else None

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Agent that answers questions about BigQuery data by executing SQL Queries',
    instruction='You are an expert BigQuery data analyst with access to several BigQuery tools, including the ability to query public datasets like `bigquery-public-data.thelook_ecommerce`. Make use of those tools and fully qualified table names (project.dataset.table) to answer user queries.',
    tools=[bigquery_toolset],
       
)
# app = App(
#     name=APP_NAME,
#     root_agent=root_agent,
#     plugins=[
#         CustomRetryPlugin(
#             max_retries=3, throw_exception_if_retry_exceeded=False
#         ),
#         LoggingPlugin(),
#     ],
# )
