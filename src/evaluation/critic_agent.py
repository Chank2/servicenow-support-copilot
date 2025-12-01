"""
Critic Agent (Agent-as-a-Judge) for ServiceNow incidents.
This module defines a simple "Agent-as-a-Judge" that evaluates
the quality of incidents created by the Worker Agent.
Later, you can replace the scoring logic with an LLM call (e.g. Gemini).
"""
from typing import Dict, Any

def review_incident(
   user_goal: str,
   conversation_summary: str,
   incident_payload: Dict[str, Any],
) -> Dict[str, Any]:
   """
   Evaluate the quality of an incident created by the Worker Agent.
   Args:
       user_goal: what the user wanted to achieve (high-level)
       conversation_summary: a short summary of the dialogue that led to this incident
       incident_payload: the payload used to create the incident
                         (same structure as create_incident(...) "payload" field)
   Returns:
       A JSON-like dict with a verdict and suggestions, e.g.:
       {
         "verdict": "pass" | "fail",
         "score": 0-10,
         "issues": [...],
         "suggestions": [...]
       }
   """
   short_description = incident_payload.get("short_description", "")
   description = incident_payload.get("description", "")
   extra = incident_payload.get("extra_context", {}) or {}
   issues = []
   score = 10
   # Very naive rule-based checks (placeholder for a real LLM-based critic):
   # 1) Short description too short
   if len(short_description.strip()) < 10:
       issues.append("Short description is too short or not descriptive enough.")
       score -= 2
   # 2) Description too short
   if len(description.strip()) < 30:
       issues.append("Description is too short. It may not be enough to reproduce the issue.")
       score -= 3
   # 3) Check if repro steps are mentioned (very naive, keyword-based)
   if "step" not in description.lower() and "repro" not in description.lower():
       issues.append("Description does not explicitly describe reproduction steps.")
       score -= 2
   # 4) Check if we have any extra context
   if not extra:
       issues.append("No extra_context provided (e.g. table, URL, timestamp).")
       score -= 2
   verdict = "pass" if score >= 7 else "fail"
   # Ensure score stays within [0, 10]
   score = max(0, min(score, 10))
   result = {
       "verdict": verdict,
       "score": score,
       "issues": issues,
       "suggestions": [],
   }
   # Simple suggestion generation based on issues
   if "Short description is too short" in " ".join(issues):
       result["suggestions"].append("Provide a short description that clearly states the main problem.")
   if "Description is too short" in " ".join(issues):
       result["suggestions"].append("Add more details to the description (expected behavior, actual behavior, etc.).")
   if "reproduction steps" in " ".join(i.lower() for i in issues):
       result["suggestions"].append("Include step-by-step reproduction steps in the description.")
   if "extra_context" in " ".join(issues):
       result["suggestions"].append("Attach extra context such as table name, URL, timestamp, and screenshot links.")
   return result

if __name__ == "__main__":
   # Small self-test
   fake_incident_payload = {
       "caller": "kun.chen@example.com",
       "short_description": "List is slow",
       "description": "The list is slow.",
       "category": "inquiry",
       "subcategory": "",
       "impact": "3",
       "urgency": "3",
       "extra_context": {},
   }
   review = review_incident(
       user_goal="Report slow performance on a ServiceNow list.",
       conversation_summary="User complained about slow loading list but gave minimal details.",
       incident_payload=fake_incident_payload,
   )
   print("=== Critic Agent Review (self-test) ===")
   print(review)
