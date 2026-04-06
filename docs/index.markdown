---
layout: default
title: About
nav_order: 0
---

# Service Desk Assistant Agent - Lab Package

## Overview

Complete hands-on lab package for learning agent monitoring and evaluation using Watson Orchestrate. Includes a Service Desk Assistant agent with IT support tools and company policy knowledge base.

### Package Contents

```
ServiceDeskAgent-Package/
├── agents/
│   └── native/
│       └── ServiceDeskAssistant.yaml     # Agent configuration (with tools)
├── knowledge_base/
│   └── company_policies.txt              # IT policies (250 lines, ~50KB)
├── python_tools/
│   ├── ticket_creator_tool.py            # IT ticket creation tool
│   └── policy_lookup_tool.py             # Quick policy lookup tool
├── evaluation/                           # For Lab 2 (created during lab)
│   ├── tools.py                          # Evaluation tool definitions
│   ├── stories.csv                       # User stories for testing
│   ├── output/                           # Generated test cases
│   └── results/                          # Evaluation results
├── import_and_deploy.sh                  # Import and deployment script
├── LAB1_UI_DASHBOARD_GUIDE.md            # Lab 1: UI Dashboard
├── LAB2_EVALUATION_FRAMEWORK_GUIDE.md    # Lab 2: Evaluation Framework
└── README.md                             # This file
```

---

## Quick Start

### Prerequisites

```bash
# Install Watson Orchestrate CLI
pip install ibm-watsonx-orchestrate

# Verify installation
orchestrate --version
```

### Installation (2 minutes)

```bash
# 1. Activate environment with your credentials
orchestrate env activate
# When prompted, enter:
# - WxO Service Instance URL: [Your instance URL]
# - API Key: [Your API key]

# 2. Clone or download this package
cd ServiceDeskAgent-Package

# 3. Run import and deployment script
chmod +x import_and_deploy.sh
./import_and_deploy.sh

# This script will:
#    - Import tools (ticket_creator, policy_lookup)
#    - Import agent (with tools automatically attached)
#    - Deploy the agent
```

### Manual Steps Required

After running the import script:

1. **Upload Knowledge Base** (in UI):
   - Go to Watson Orchestrate UI
   - Navigate to Agents → Service_Desk_Assistant
   - Click 'Knowledge Base' section
   - Upload `knowledge_base/company_policies.txt`
   - Wait 2-3 minutes for processing

2. **Enable Monitoring** (for evaluation):
   - Click hamburger menu (☰)
   - Select 'Analyze'
   - Find 'Service_Desk_Assistant'
   - Toggle 'Monitor' to ON

---

## Lab Structure

### Lab 1: AgentOps UI Dashboard (60 minutes)

**Focus:** Visual monitoring and analysis

**What You'll Learn:**
- Navigate AgentOps dashboard
- Analyze Evaluation metrics (conversations, messages, tools)
- Perform deep Analysis (drill-down investigation)
- Identify cost drivers and performance issues
- Optimize agent behavior

**Key Sections:**
- **Evaluation:** High-level metrics and trends
- **Analysis:** Deep dive into conversations, messages, and tools



---

### Lab 2: Evaluation Framework (60 minutes)

**Focus:** Automated testing and programmatic evaluation

**What You'll Learn:**
- Create user stories for testing
- Define evaluation tools
- Generate synthetic test cases
- Run automated evaluations
- Analyze results programmatically

**Key Steps:**
- Create stories.csv (5 test scenarios)
- Define tools.py (tool definitions)
- Generate test cases (5 synthetic test cases)
- Run evaluation
- Analyze results

---

## Agent Configuration

### Service Desk Assistant

**Purpose:** Help users with IT support and policy questions

**Capabilities:**
1. **IT Ticket Creation** - Create support tickets for hardware, software, access, or security issues
2. **Policy Lookup** - Quick answers to common policy questions
3. **Knowledge Base** - Comprehensive company IT policies

**Tools:**
- `create_ticket` - Creates IT support tickets with priority and category
- `lookup_policy` - Provides quick policy guidance

**Knowledge Base:**
- Data Handling Policy
- Third Party Access Policy
- Security Incident Reporting Policy
- Acceptable Use Policy

---

## Lab Workflow

### Recommended Path

1. **Start with Lab 1** (60 min)
   - Import agent and tools
   - Add knowledge base
   - Generate test conversations
   - Explore AgentOps dashboard
   - Learn Evaluation and Analysis sections

2. **Then Complete Lab 2** (60 min)
   - Create user stories
   - Define evaluation tools
   - Generate test cases
   - Run automated evaluation
   - Analyze results programmatically

3. **Use Both Together**
   - Lab 1 for interactive debugging
   - Lab 2 for automated regression testing

---

## Test Scenarios

### Lab 1: Manual Testing (9 messages, 3 conversations)

**Conversation 1:** Simple policy questions
- Can I store customer data in Google Sheets?
- Is 2FA required for VPN?
- Who approves vendor access?

**Conversation 2:** Complex policy questions
- Vendor approval process walkthrough
- US vs EU vendor differences
- PII exposure incident response

**Conversation 3:** Tool usage and tickets
- Report phishing email (creates ticket)
- Request database access (creates ticket)
- Stolen laptop with data (creates critical ticket)

### Lab 2: Automated Testing (12 test cases)

- Policy questions (data storage, 2FA, vendor approval)
- Process explanations (vendor approval, incident reporting)
- Ticket creation scenarios (phishing, access, stolen device)
- System requirements (passwords, security)

---

## Key Features

### Lab 1 Features

**Real-time Monitoring**
- Live conversation tracking
- Cost analysis per message
- Token usage visualization
- Response time metrics

**Two-Section Dashboard**
- **Evaluation:** Overview, conversation metrics, message metrics, tool metrics
- **Analysis:** Conversation-level, message-level, tool-level deep dives

**Interactive Exploration**
- Drill down into specific issues
- Message-level token analysis
- Tool call inspection
- Security assessment

### Lab 2 Features

**Automated Testing**
- Synthetic test case generation
- Batch evaluation
- Programmatic analysis
- Reproducible results

**Comprehensive Metrics**
- Journey success rates
- Text match quality
- Tool call accuracy
- Performance benchmarks

**CI/CD Ready**
- Command-line interface
- Scriptable evaluation
- Automated regression testing

---

## Success Metrics

### Lab 1 Success Criteria

- Agent responds to all 9 messages
- Creates tickets when appropriate
- References correct policies
- Provides complete answers
- Reasonable cost per conversation

### Lab 2 Success Criteria

- 80%+ journey success rate
- High text match scores
- Correct tool calls
- Consistent performance
- Automated evaluation runs successfully

---

## File Sizes

All files optimized for easy upload:

- **company_policies.txt:** ~50KB (250 lines)
- **ticket_creator_tool.py:** ~4KB
- **policy_lookup_tool.py:** ~5KB
- **Total package:** <1MB

---

## Troubleshooting

### Common Issues

**Issue: Import script fails**
```bash
# Solution: Check CLI installation
orchestrate --version
# Ensure environment is activated
orchestrate env activate
```

**Issue: Knowledge base not working**
```bash
# Solution: Verify document is processed
# In UI: Check document shows "Processed" status
# Wait 2-3 minutes after upload
```

**Issue: No data in dashboard**
```bash
# Solution: 
# 1. Verify monitoring is enabled
# 2. Wait 5-10 minutes for data
# 3. Refresh dashboard
```

**Issue: Evaluation fails**
```bash
# Solution: Check .env file
cat .env
# Verify agent name in stories.csv
orchestrate agents list
```

---

## Best Practices

### Agent Development

1. **Start Simple** - Test basic questions first
2. **Iterate** - Use Lab 1 to identify issues
3. **Automate** - Use Lab 2 for regression testing
4. **Monitor** - Keep monitoring enabled
5. **Optimize** - Act on dashboard insights

### Knowledge Base

1. **Clear Structure** - Use section headers
2. **Specific Guidance** - Provide actionable information
3. **Examples** - Include real-world scenarios
4. **Updates** - Re-run evaluation after changes

### Evaluation

1. **Comprehensive Coverage** - Test all capabilities
2. **Regular Runs** - Daily automated evaluation
3. **Track Trends** - Monitor success rates over time
4. **Fix Issues** - Address failures promptly

---

## Additional Resources

### Documentation

- [Watson Orchestrate Docs](https://developer.watson-orchestrate.ibm.com)
- [AgentOps Dashboard](https://developer.watson-orchestrate.ibm.com/evaluate)
- [Evaluation Framework](https://developer.watson-orchestrate.ibm.com/evaluate/framework)
- [LLM Vulnerability Guide](https://developer.watson-orchestrate.ibm.com/evaluate/llm_vulnerability)

### Related Packages

- **EvaluationAgent-Package** - Original framework with comprehensive documentation
- **EVALUATIONAGENT_COMPLETE_DOCUMENTATION.md** - Complete 10-phase guide

---

## Support

### Getting Help

**For Lab Questions:**
- Review lab guide thoroughly
- Check troubleshooting section
- Verify prerequisites

**For Technical Issues:**
- Check Watson Orchestrate status
- Verify credentials in .env
- Review error messages carefully

---

## Version History

### Version 2.0 (April 2026)
- Simplified policy document (single file, 250 lines)
- Added 2 practical tools (ticket creator, policy lookup)
- Streamlined Lab 1 (focus on Evaluation and Analysis sections)
- Simplified Lab 2 (focus on test generation and evaluation)
- Added import script for easy setup
- Optimized for hands-on learning

---

## Quick Reference

### Lab 1 Commands

```bash
# Run import script
./import_agent_and_tools.sh

# Then in UI:
# 1. Add knowledge base
# 2. Enable monitoring (Analyze → Toggle Monitor ON)
# 3. Send 9 test messages (3 conversations, 10 min apart)
# 4. View dashboard (Analyze → View Dashboard)
```

### Lab 2 Commands

```bash
# Generate test cases
orchestrate evaluations generate \
  --stories-path ./evaluation/stories.csv \
  --tools-path ./evaluation/tools.py \
  --output-dir ./evaluation/output

# Run evaluation
orchestrate evaluations evaluate \
  --test-paths ./evaluation/output/Service_Desk_Assistant_*/  \
  --output-dir ./evaluation/results/ \
  --env-file .env

# Analyze results
orchestrate evaluations analyze \
  -d ./evaluation/results/[timestamp]
```

---

## Lab Comparison

| Aspect | Lab 1 | Lab 2 |
|--------|-------|-------|
| **Duration** | 60 min | 60 min |
| **Method** | Manual testing | Automated testing |
| **Interface** | Visual dashboard | Command line |
| **Focus** | Interactive exploration | Programmatic evaluation |
| **Best For** | Development & debugging | Regression testing |
| **Output** | Visual insights | Metrics & reports |

---

**Total Lab Time:** 2 hours  
**Difficulty:** Beginner to Intermediate  
**Outcome:** Complete understanding of agent monitoring and evaluation

<!-- This is the base Jekyll theme. You can find out more info about customizing your Jekyll theme, as well as basic Jekyll usage documentation at [jekyllrb.com](https://jekyllrb.com/)

You can find the source code for Minima at GitHub:
[jekyll][jekyll-organization] /
[minima](https://github.com/jekyll/minima)

You can find the source code for Jekyll at GitHub:
[jekyll][jekyll-organization] /
[jekyll](https://github.com/jekyll/jekyll)


[jekyll-organization]: https://github.com/jekyll -->
