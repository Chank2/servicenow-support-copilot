"""
Tool: Log performance complaints for slow tables or lists in ServiceNow.
This helps the platform/infra team reproduce and diagnose performance issues.
"""
from typing import Dict

def log_performance_issue(
   table_name: str,
   url: str,
   timestamp: str,
   user_id: str,
   repro_steps: str,
   screenshot_url: str = "",
) -> Dict:
   """
   Log a performance complaint.
   In a real implementation, this tool would write to:
     - a custom ServiceNow table, or
     - an external logging system / database.
   For the prototype, we just return a structured record.
   """
   record = {
       "table_name": table_name,
       "url": url,
       "timestamp": timestamp,
       "user_id": user_id,
       "repro_steps": repro_steps,
       "screenshot_url": screenshot_url,
       "status": "logged",
   }
   # TODO: persist this record somewhere (e.g. DB, file, ServiceNow table).
   # For now, just return it so the agent can display/confirm it.
   return record
