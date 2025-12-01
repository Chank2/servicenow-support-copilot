"""
ServiceNow Support Co-Pilot Agent (CLI Demo)
This is a minimal prototype:
- Ask the user for a ServiceNow-related problem.
- Search the (stub) Knowledge Base tool.
- Optionally search similar incidents.
- Optionally create an incident using the incident tool.
- Evaluate the created incident using a Critic Agent (Agent-as-a-Judge).
Later we will:
- Replace stubs with real ServiceNow / MCP integration.
- Replace the rule-based critic with an LLM-based critic.
"""
from typing import Dict
# Worker agent tools
from tools.servicenow_kb import search_kb
from tools.servicenow_incidents import search_incidents, create_incident
# Critic Agent (Agent-as-a-Judge)
from evaluation.critic_agent import review_incident

def ask_user_question() -> str:
   """Ask the user for a problem description."""
   print("==== ServiceNow Support Co-Pilot (CLI Demo) ====")
   print("Describe your issue with ServiceNow (or type 'exit' to quit):")
   user_input = input("> ").strip()
   return user_input

def show_kb_results(kb_results: Dict) -> None:
   """Pretty-print KB search results."""
   results = kb_results.get("results", [])
   if not results:
       print("\nNo KB articles found.")
       return
   print("\n🔎 KB search results:")
   for i, item in enumerate(results, start=1):
       print(f"  [{i}] {item.get('short_description')}")
       print(f"      KB Number: {item.get('number')}")
       print(f"      URL:       {item.get('url')}")
       print(f"      Snippet:   {item.get('snippet')}")
       print()

def main():
   while True:
       user_problem = ask_user_question()
       if user_problem.lower() in ("exit", "quit"):
           print("Bye! 👋")
           break
       if not user_problem:
           print("Please describe your issue before we continue.\n")
           continue
       # We'll treat the user's free-text description as the "user goal" for the critic.
       user_goal = user_problem
       # 1) Search KB
       print("\n[Step 1] Searching Knowledge Base...")
       kb_results = search_kb(user_problem, max_results=3)
       show_kb_results(kb_results)
       # 2) Ask if any KB solved the problem
       print("Did any of these KB articles solve your issue? (y/n)")
       solved = input("> ").strip().lower()
       if solved == "y":
           print("Great! No incident needed. ✅\n")
           continue
       # 3) Check for similar incidents
       print("\n[Step 2] Searching for similar incidents...")
       inc_results = search_incidents(user_problem, limit=3)
       results = inc_results.get("results", [])
       if results:
           print("\n📂 Similar incidents found:")
           for i, item in enumerate(results, start=1):
               print(f"  [{i}] {item.get('number')} - {item.get('short_description')}")
               print(f"      URL: {item.get('url')}")
           print()
       else:
           print("No similar incidents found.\n")
       # 4) Ask if the user wants to create a new incident
       print("Do you want to create a new incident for this issue? (y/n)")
       create = input("> ").strip().lower()
       if create != "y":
           print("OK, not creating an incident.\n")
           continue
       # --- collect minimal fields for incident ---
       caller = input("Caller (e.g. your email or user ID): ").strip() or "unknown_caller"
       short_desc = user_problem[:80]  # simple default short description
       print("Please provide a more detailed description of the issue:")
       description = input("> ").strip() or user_problem
       # For prototype, use default classification values
       category = "inquiry"
       subcategory = ""
       impact = "3"
       urgency = "3"
       # Extra context (in real life: table name, URL, timestamp, screenshot, etc.)
       extra_context = {
           "source": "cli-demo",
       }
       print("\n[Step 3] Creating incident (prototype)...")
       incident = create_incident(
           caller=caller,
           short_description=short_desc,
           description=description,
           category=category,
           subcategory=subcategory,
           impact=impact,
           urgency=urgency,
           extra_context=extra_context,
       )
       print("\n✅ Incident created (stub):")
       print(f"  Number: {incident.get('number')}")
       print(f"  URL:    {incident.get('url')}")
       print("  Payload:")
       payload = incident.get("payload", {})
       for k, v in payload.items():
           print(f"    {k}: {v}")
       print("\n---")
       # 5) Call Critic Agent to review the incident
       print("[Step 4] Critic Agent reviewing incident quality...")
       # For now, conversation_summary is a simple string.
       # Later you can replace it with a real session summary.
       conversation_summary = (
           "User reported a ServiceNow issue. "
           "KB search and incident search were performed. "
           "User chose to create a new incident via CLI demo."
       )
       review = review_incident(
           user_goal=user_goal,
           conversation_summary=conversation_summary,
           incident_payload=payload,
       )
       print("\n🧠 Critic Agent Evaluation:")
       print(f"  Verdict: {review.get('verdict')}")
       print(f"  Score:   {review.get('score')}/10")
       issues = review.get("issues", [])
       suggestions = review.get("suggestions", [])
       if issues:
           print("  Issues:")
           for i in issues:
               print(f"    - {i}")
       else:
           print("  Issues: none")
       if suggestions:
           print("  Suggestions:")
           for s in suggestions:
               print(f"    - {s}")
       else:
           print("  Suggestions: none")
       print("\n=== End of one incident flow ===\n")
if __name__ == "__main__":
   main()
