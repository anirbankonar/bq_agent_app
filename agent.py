from google.adk.agents.llm_agent import Agent
from google.adk.tools.bigquery import BigQueryToolset
bigquery_toolset = BigQueryToolset(tool_filter=[
'list_dataset_ids',
'get_dataset_info',
'list_table_ids',
'get_table_info',
'execute_sql',
     ])
     
root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Agent that answers questions about BigQuery data by executing SQL Queries',
    instruction='You are an expert BigQuery data analyst with access to several BigQuery tools, including the ability to query public datasets like `bigquery-public-data.thelook_ecommerce`. Make use of those tools and fully qualified table names (project.dataset.table) to answer user queries.',
    tools=[bigquery_toolset]
)
