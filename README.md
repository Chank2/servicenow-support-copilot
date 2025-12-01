# servicenow-support-copilot
ServiceNow Support Co-Pilot Agent - Enterprise agent for IT support and incident creation

An enterprise agent for helping internal users with ServiceNow:
- Answer "how-to" questions using the knowledge base
- Search for similar incidents
- Create high-quality incident tickets
- Log performance complaints (slow tables / list views)
This repository contains the prototype code for my Agent Intensive capstone project
under the **Enterprise Agents** track.
## Structure
```text
src/
 main.py                     # Entry point (skeleton)
 tools/
   servicenow_kb.py          # KB search tool (stub)
   servicenow_incidents.py   # Incident search & create tools (stub)
   performance_log.py        # Performance complaint logging tool (stub)
