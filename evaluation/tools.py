"""
Evaluation Tools for Service Desk Assistant
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import Literal
import json


@tool()
def create_ticket(
    category: Literal["hardware", "software", "access", "security"],
    priority: Literal["low", "medium", "high", "critical"],
    title: str,
    description: str,
    requester_email: str
) -> str:
    """Creates an IT support ticket."""
    result = {
        "status": "success",
        "ticket_number": f"TKT-{category[:3].upper()}-12345",
        "category": category,
        "priority": priority,
        "estimated_resolution": "24 hours"
    }
    return json.dumps(result)


@tool()
def lookup_policy(
    policy_area: Literal["data_storage", "vendor_approval", "incident_reporting", "system_access", "password_requirements"],
    specific_question: str = ""
) -> str:
    """Looks up quick policy information."""
    result = {
        "status": "success",
        "policy_area": policy_area,
        "key_points": ["Policy guidance point 1", "Policy guidance point 2"],
        "contact": "security@company.com"
    }
    return json.dumps(result)


@tool()
def query_knowledge_base(question: str) -> str:
    """Queries the company policies knowledge base."""
    result = {
        "status": "success",
        "question": question,
        "policy_guidance": "Detailed policy guidance",
        "source": "Company IT Policies"
    }
    return json.dumps(result)