#!/bin/bash

# ServiceDeskAssistant Import and Deployment Script
# This script imports tools and agent into watsonx Orchestrate
# Knowledge base must be added manually in the UI

set -e  # Exit on error

echo "=========================================="
echo "Service Desk Assistant Import and Deployment"
echo "=========================================="
echo ""

# Change to the script directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "Working directory: $SCRIPT_DIR"
echo ""

# Step 1: Remove existing resources
echo "Step 1: Removing existing resources..."
echo "---------------------------------------"
orchestrate agents remove --kind native --name Service_Desk_Assistant 2>/dev/null || echo "Service_Desk_Assistant not found, skipping..."
orchestrate tools remove --name ticket_creator 2>/dev/null || echo "ticket_creator not found, skipping..."
orchestrate tools remove --name policy_lookup 2>/dev/null || echo "policy_lookup not found, skipping..."
echo "✓ Existing resources removed"
echo ""

# Step 2: Import Python Tools
echo "Step 2: Importing Python tools..."
echo "----------------------------------"
cd python_tools

echo "  Importing ticket_creator_tool..."
orchestrate tools import -k python -f ticket_creator_tool.py

echo "  Importing policy_lookup_tool..."
orchestrate tools import -k python -f policy_lookup_tool.py

cd ..
echo "✓ All tools imported"
echo ""

# Step 3: Import Agent (with tools automatically attached)
echo "Step 3: Importing Service_Desk_Assistant..."
echo "-------------------------------------"
orchestrate agents import -f agents/native/ServiceDeskAssistant.yaml
echo "✓ Agent imported (tools automatically attached)"
echo ""

# Step 4: Deploy Agent
echo "Step 4: Deploying Service_Desk_Assistant..."
echo "-------------------------------------"
orchestrate agents deploy --name Service_Desk_Assistant
echo "✓ Agent deployed"
echo ""

echo "=========================================="
echo "✓ Import completed successfully!"
echo "=========================================="
echo ""
echo "Summary:"
echo "  - Tools: ticket_creator, policy_lookup (imported and attached to agent)"
echo "  - Agent: Service_Desk_Assistant (deployed)"
echo ""
echo "⚠️  MANUAL STEP REQUIRED:"
echo "=========================================="
echo ""
echo "Upload Knowledge Base (in UI):"
echo "   1. Go to Watson Orchestrate UI"
echo "   2. Navigate to Agents → Service_Desk_Assistant"
echo "   3. Click 'Knowledge Base' section"
echo "   4. Click 'Add Documents'"
echo "   5. Upload: knowledge_base/company_policies.txt"
echo "   6. Name: Company IT Policies"
echo "   7. Description: Comprehensive IT policies covering data handling,"
echo "      vendor approval, security incidents, and acceptable use"
echo "   8. Click 'Save' and wait 2-3 minutes for processing"
echo ""
echo "Enable Monitoring (for evaluation):"
echo "   1. Click hamburger menu (☰)"
echo "   2. Select 'Analyze'"
echo "   3. Find 'Service_Desk_Assistant'"
echo "   4. Toggle 'Monitor' to ON"
echo ""
echo "You're ready for the labs!"
echo "   - LAB1_UI_DASHBOARD_GUIDE.md"
echo "   - LAB2_EVALUATION_FRAMEWORK_GUIDE.md"
echo ""
echo "=========================================="

# Made with Bob