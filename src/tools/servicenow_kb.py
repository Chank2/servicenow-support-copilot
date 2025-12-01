"""
Tool: ServiceNow Knowledge Base search
In the real implementation, this module will call the ServiceNow
Knowledge API (or an MCP server that wraps it) to search KB articles.
"""
from typing import List, Dict
def search_kb(query: str, max_results: int = 5) -> Dict:
   """
   Search ServiceNow KB by keyword.
   Args:
       query: free-text query string
       max_results: maximum number of articles to return
   Returns:
       A dictionary with a list of KB hits, e.g.:
       {
         "results": [
           {
             "number": "KB0012345",
             "short_description": "...",
             "url": "https://example.service-now.com/kb_view.do?sys_id=...",
             "snippet": "..."
           },
           ...
         ]
       }
   """
   # TODO: replace this stub with a real API call or MCP tool invocation.
   # For now, just return a fake result so the agent can be prototyped.
   return {
       "results": [
           {
               "number": "KB0000001",
               "short_description": f"Fake KB result for query: {query}",
               "url": "https://example.service-now.com/kb_view.do?sys_id=FAKE",
               "snippet": "This is a placeholder KB article used for prototyping."
           }
       ][:max_results]
   }
