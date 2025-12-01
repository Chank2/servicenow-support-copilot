# servicenow-support-copilot
ServiceNow Support Co-Pilot Agent - Enterprise agent for IT support and incident creation

This repository contains a **prototype enterprise agent** designed to help users troubleshoot ServiceNow issues.  
The system demonstrates a multi-agent architecture, including:
- A **Worker Agent** that searches KB, checks similar incidents, and creates tickets.
- A **Critic Agent** (“Agent-as-a-Judge”) that evaluates the quality of created incidents.
All ServiceNow interactions are **stubbed tools**, making this project easy to run locally without a real ServiceNow instance.
---
## 🚀 Features
### 🔧 Worker Agent (main agent)
- CLI-based interaction
- Searches KB (stub tool)
- Searches similar incidents (stub tool)
- Creates new incident tickets (stub tool)
- Passes incidents to the Critic Agent
### 🧠 Critic Agent (Agent-as-a-Judge)
- Reviews incident payload:
 - Short description  
 - Long description  
 - Reproduction steps  
 - Extra context
- Produces:
 ```json
 {
   "verdict": "pass/fail",
   "score": 0-10,
   "issues": [...],
   "suggestions": [...]
 }


### Structure
```text
src/
 main.py                     # Entry point (skeleton)
 tools/
   servicenow_kb.py          # KB search tool (stub)
   servicenow_incidents.py   # Incident search & create tools (stub)
   performance_log.py        # Performance complaint logging tool (stub)
evalution/
   critic_agent.py


User          Worker Agent          Tools                   Critic Agent
│                 │                  │                           │
│  describe issue │                  │                           │
├────────────────>│                  │                           │
│                 │  search KB       │                           │
│                 ├─────────────────>│                           │
│                 │  KB results      │                           │
│                 ◄──────────────────┤                           │
│                 │ ask user         │                           │
│                 │                  │                           │
│   user chooses to create incident  │                           │
├────────────────────────────────────>│                           │
│                 │ create incident  │                           │
│                 ├─────────────────> IncidentTool               │
│                 │  stub incident   │                           │
│                 ◄──────────────────┤                           │
│                 │ send payload     │                           │
│                 ├─────────────────────────────────────────────>│
│                 │                  │       evaluate            │
│                 │                  │<──────────────────────────┤
│                 │     evaluation results                       │
│<────────────────┤                                              │
