"""
Policy Lookup Tool for Service Desk Assistant
Provides quick policy information and guidance.
"""

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from typing import Literal


@tool(
    name="policy_lookup",
    display_name="Policy Quick Lookup",
    description="Provides quick answers to common policy questions without searching full documents"
)
def lookup_policy(
    policy_area: Literal["data_storage", "vendor_approval", "incident_reporting", "system_access", "password_requirements"],
    specific_question: str = ""
) -> dict:
    """Looks up quick policy information.
    
    Args:
        policy_area: The policy area to look up
        specific_question: Optional specific question for more targeted response
    
    Returns:
        dict: Policy information and guidance
    """
    
    policy_responses = {
        "data_storage": {
            "summary": "Customer data storage requirements",
            "key_points": [
                "Customer data MUST NOT be stored in shared Google Sheets",
                "Use company OneDrive/SharePoint for approved storage",
                "2FA required for all customer data systems",
                "Downloads require approval, max 30 days retention"
            ],
            "approved_locations": ["OneDrive", "SharePoint", "Approved databases"],
            "prohibited_locations": ["Google Sheets", "Personal cloud", "Unencrypted USB"],
            "contact": "security@company.com"
        },
        "vendor_approval": {
            "summary": "Third party vendor approval process",
            "key_points": [
                "Low risk (no customer data): Manager approval, 5 days",
                "Medium risk (internal data): Manager + IT + Procurement, 10 days",
                "High risk (customer data): Manager + CISO + DPO + Legal, 20-30 days"
            ],
            "us_vendors": "SOC 2 certification preferred, insurance required",
            "eu_vendors": "GDPR compliance + SCCs + DPA required, additional approvals needed",
            "contact": "vendor-security@company.com"
        },
        "incident_reporting": {
            "summary": "Security incident reporting procedures",
            "key_points": [
                "Report immediately: Call x5555 (24/7)",
                "Critical incidents: Response within 15 minutes",
                "Do not investigate on your own",
                "Preserve evidence, document what happened"
            ],
            "severity_levels": {
                "Critical (P1)": "Customer PII exposed, ransomware, data exfiltration",
                "High (P2)": "Suspected breach, malware on multiple systems",
                "Medium (P3)": "Isolated malware, failed access attempts"
            },
            "emergency_contact": "x5555",
            "email": "security@company.com"
        },
        "system_access": {
            "summary": "System access and authentication requirements",
            "key_points": [
                "2FA required for: VPN, email (remote), cloud apps, customer data systems",
                "Unique credentials only (no shared accounts)",
                "Least privilege access principle",
                "Access reviewed quarterly"
            ],
            "vpn_requirements": "2FA required, use only from secure networks",
            "remote_work": "VPN required for all remote access, no public WiFi without VPN",
            "contact": "itsupport@company.com"
        },
        "password_requirements": {
            "summary": "Password and authentication requirements",
            "key_points": [
                "Minimum 12 characters",
                "Mix of uppercase, lowercase, numbers, symbols",
                "Changed every 90 days",
                "No password reuse (last 12 passwords)",
                "Never share passwords"
            ],
            "mfa_required": ["VPN", "Email (remote)", "Cloud applications", "Customer data systems"],
            "password_manager": "Recommended for complex passwords",
            "contact": "itsupport@company.com"
        }
    }
    
    response = policy_responses.get(policy_area, {})
    
    return {
        "status": "success",
        "policy_area": policy_area,
        "specific_question": specific_question,
        "summary": response.get("summary", ""),
        "key_points": response.get("key_points", []),
        "additional_info": {k: v for k, v in response.items() if k not in ["summary", "key_points"]},
        "recommendation": "For detailed policy information, refer to the full company policies document or contact the listed department.",
        "note": "This is a quick reference. Always consult full policy documents for complete guidance."
    }


# Test the tool locally
if __name__ == "__main__":
    print("Testing Policy Lookup Tool")
    print("=" * 60)
    
    # Test 1: Data storage
    print("\nTest 1: Data Storage Policy")
    result1 = lookup_policy(
        policy_area="data_storage",
        specific_question="Can I use Google Sheets for customer data?"
    )
    print(f"Summary: {result1['summary']}")
    print("Key Points:")
    for point in result1['key_points']:
        print(f"  - {point}")
    
    # Test 2: Vendor approval
    print("\nTest 2: Vendor Approval Process")
    result2 = lookup_policy(
        policy_area="vendor_approval",
        specific_question="How long does EU vendor approval take?"
    )
    print(f"Summary: {result2['summary']}")
    print("Key Points:")
    for point in result2['key_points']:
        print(f"  - {point}")
    
    # Test 3: Incident reporting
    print("\nTest 3: Incident Reporting")
    result3 = lookup_policy(
        policy_area="incident_reporting",
        specific_question="What do I do if I accidentally expose customer PII?"
    )
    print(f"Summary: {result3['summary']}")
    print(f"Emergency Contact: {result3['additional_info']['emergency_contact']}")
    
    print("\n" + "=" * 60)

# Made with Bob
