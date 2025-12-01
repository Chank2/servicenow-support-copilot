# servicenow-support-copilot
**ServiceNow Support Co-Pilot Agent — Enterprise agent for IT support and incident creation**
This repository contains a **prototype enterprise agent** designed to help users troubleshoot ServiceNow issues.  
It demonstrates a **multi-agent architecture**, including:
- A **Worker Agent** that searches KB, checks similar incidents, and creates tickets  
- A **Critic Agent** (“Agent-as-a-Judge”) that evaluates the quality of created incidents  
All ServiceNow interactions are implemented as **stubbed tools**, making this project easy to run locally **without requiring a real ServiceNow instance**.
---
## 🚀 Features
### 🔧 Worker Agent (main agent)
- CLI-based interaction  
- Searches KB (stub tool)  
- Searches similar incidents (stub tool)  
- Creates new incident tickets (stub tool)  
- Passes created incidents to the Critic Agent  
### 🧠 Critic Agent (Agent-as-a-Judge)
Evaluates the quality of incident payloads, including:
- Short description  
- Long description  
- Reproduction steps  
- Extra context  
Produces structured evaluation output:
```json
{
 "verdict": "pass/fail",
 "score": 0-10,
 "issues": [],
 "suggestions": []
}
```
---
## 📁 Project Structure
```text
servicenow-support-copilot/
├── README.md
├── requirements.txt
└── src/
   ├── main.py                     # Worker Agent CLI entry point
   ├── tools/
   │   ├── servicenow_kb.py        # KB search tool (stub)
   │   ├── servicenow_incidents.py # Incident search & creation (stub)
   │   └── performance_log.py      # Performance complaint logging tool (stub)
   └── evaluation/
       └── critic_agent.py         # Critic Agent (Agent-as-a-Judge)
```
---
## 🔁 Worker Agent → Critic Agent Sequence Diagram
```text
User          Worker Agent          Tools                     Critic Agent
│                 │                  │                             │
│  describe issue │                  │                             │
├────────────────>│                  │                             │
│                 │  search KB       │                             │
│                 ├─────────────────>│                             │
│                 │  KB results      │                             │
│                 ◄──────────────────┤                             │
│                 │ ask user         │                             │
│                 │                  │                             │
│  user chooses to create incident   │                             │
├────────────────────────────────────>│                             │
│                 │ create incident  │                             │
│                 ├─────────────────> IncidentTool                 │
│                 │  stub incident   │                             │
│                 ◄──────────────────┤                             │
│                 │ send payload     │                             │
│                 ├───────────────────────────────────────────────>│
│                 │                  │          evaluate            │
│                 │                  │<─────────────────────────────┤
│                 │      evaluation results                         │
│<────────────────┤
```
---
## 🧪 How to Run
Inside the project root:
```bash
pip install -r requirements.txt
python -m src.main
Example prompt:
==== ServiceNow Support Co-Pilot (CLI Demo) ====
Describe your issue with ServiceNow:
>
