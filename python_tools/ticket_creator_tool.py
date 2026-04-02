"""
IT Ticket Creator Tool for Service Desk Assistant
Creates IT support tickets for various issues.
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import Literal
from datetime import datetime


@tool(
    name="ticket_creator",
    display_name="IT Ticket Creator",
    description="Creates IT support tickets for hardware, software, access, or security issues"
)
def create_ticket(
    category: Literal["hardware", "software", "access", "security"],
    priority: Literal["low", "medium", "high", "critical"],
    title: str,
    description: str,
    requester_email: str
) -> dict:
    """Creates an IT support ticket.
    
    Args:
        category: Type of issue (hardware, software, access, security)
        priority: Urgency level (low, medium, high, critical)
        title: Brief title of the issue
        description: Detailed description of the problem
        requester_email: Email of person requesting support
    
    Returns:
        dict: Ticket details including ticket number and estimated resolution time
    """
    # Generate ticket number
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    ticket_number = f"TKT-{category[:3].upper()}-{timestamp}"
    
    # Estimate resolution time based on priority
    resolution_times = {
        "critical": "4 hours",
        "high": "24 hours",
        "medium": "3 business days",
        "low": "5 business days"
    }
    
    # Determine assignment based on category
    assignments = {
        "hardware": "Hardware Support Team",
        "software": "Software Support Team",
        "access": "Access Management Team",
        "security": "Security Operations Team"
    }
    
    return {
        "status": "success",
        "ticket_number": ticket_number,
        "category": category,
        "priority": priority,
        "title": title,
        "description": description,
        "requester_email": requester_email,
        "assigned_to": assignments[category],
        "estimated_resolution": resolution_times[priority],
        "created_at": datetime.utcnow().isoformat() + "Z",
        "ticket_url": f"https://servicedesk.company.com/tickets/{ticket_number}",
        "message": f"Ticket {ticket_number} created successfully. Assigned to {assignments[category]}. Estimated resolution: {resolution_times[priority]}."
    }


# Test the tool locally
if __name__ == "__main__":
    print("Testing IT Ticket Creator Tool")
    print("=" * 60)
    
    # Test 1: Security incident
    print("\nTest 1: Security Incident")
    result1 = create_ticket(
        category="security",
        priority="critical",
        title="Suspected phishing email received",
        description="Received suspicious email asking for credentials",
        requester_email="john.doe@company.com"
    )
    print(f"Ticket: {result1['ticket_number']}")
    print(f"Assigned to: {result1['assigned_to']}")
    print(f"Resolution: {result1['estimated_resolution']}")
    
    # Test 2: Access request
    print("\nTest 2: Access Request")
    result2 = create_ticket(
        category="access",
        priority="medium",
        title="Request access to customer database",
        description="Need read access to customer analytics database for Q1 reporting",
        requester_email="jane.smith@company.com"
    )
    print(f"Ticket: {result2['ticket_number']}")
    print(f"Assigned to: {result2['assigned_to']}")
    print(f"Resolution: {result2['estimated_resolution']}")
    
    # Test 3: Software issue
    print("\nTest 3: Software Issue")
    result3 = create_ticket(
        category="software",
        priority="low",
        title="Excel crashes when opening large files",
        description="Excel application crashes when trying to open files larger than 50MB",
        requester_email="bob.johnson@company.com"
    )
    print(f"Ticket: {result3['ticket_number']}")
    print(f"Assigned to: {result3['assigned_to']}")
    print(f"Resolution: {result3['estimated_resolution']}")
    
    print("\n" + "=" * 60)

# Made with Bob
