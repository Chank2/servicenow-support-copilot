"""
Tool: ServiceNow Incident search / create
In production this would wrap the ServiceNow Incident REST API
(or an MCP server that exposes these APIs as tools).
"""
from typing import Dict, List
def search_incidents(short_description: str, limit: int = 5) -> Dict:
   """
   Search recent incidents with a similar short_description.
   Returns:
       {
         "results": [
           {"number": "INC0001", "short_description": "...", "url": "..."},
           ...
         ]
       }
   """
   # TODO: replace stub with real implementation.
   return {
       "results": [
           {
               "number": "INC0001",
               "short_description": f"Fake incident similar to: {short_description}",
               "url": "https://example.service-now.com/incident.do?sys_id=FAKE",
           }
       ][:limit]
   }

def create_incident(
   caller: str,
   short_description: str,
   description: str,
   category: str = "inquiry",
   subcategory: str = "",
   impact: str = "3",
   urgency: str = "3",
   extra_context: Dict = None,
) -> Dict:
   """
   Create a new incident ticket (prototype version).
   Args:
       caller: user identifier (e.g. email or user_id)
       short_description: title of the incident
       description: detailed description
       category, subcategory, impact, urgency: classification fields
       extra_context: dict with extra diagnostic info (table, URL, screenshot, etc.)
   Returns:
       { "number": "...", "sys_id": "...", "url": "..." }
   """
   extra_context = extra_context or {}
   # TODO: replace stub with real POST call to ServiceNow
   fake_number = "INC9999999"
   fake_sys_id = "FAKE_SYS_ID_123"
   fake_url = f"https://example.service-now.com/incident.do?sys_id={fake_sys_id}"
   return {
       "number": fake_number,
       "sys_id": fake_sys_id,
       "url": fake_url,
       "payload": {
           "caller": caller,
           "short_description": short_description,
           "description": description,
           "category": category,
           "subcategory": subcategory,
           "impact": impact,
           "urgency": urgency,
           "extra_context": extra_context,
       },
   }
