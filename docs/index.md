---
layout: default
title: Home
---

# Service Desk Assistant - Lab Guide

Welcome to the hands-on lab package for learning agent monitoring and evaluation using Watson Orchestrate.

## 📚 Available Labs
📖 **[Setup Instructions](SETUP_INSTRUCTIONS.md)** - How to publish this site to GitHub Pages


### [Lab 1: AgentOps UI Dashboard](lab1.md)
**Duration:** 60 minutes  
**Focus:** Visual monitoring and analysis

Learn to:
- Navigate the AgentOps dashboard
- Analyze conversation, message, and tool metrics
- Perform deep-dive investigations
- Identify cost drivers and performance issues
- Optimize agent behavior

**Best for:** Business users, product managers, and anyone who wants high-level insights without diving into code.

---

### [Lab 2: Evaluation Framework](lab2.md)
**Duration:** 60 minutes  
**Focus:** Automated testing and programmatic evaluation

Learn to:
- Create user stories for testing
- Define evaluation tools
- Generate synthetic test cases
- Run automated evaluations
- Analyze results programmatically

**Best for:** Developers, data scientists, and QA engineers who need programmatic access and automation.

---

## 🚀 Quick Start

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

# 2. Clone or download the package
cd ServiceDeskAgent-Package

# 3. Run import and deployment script
chmod +x import_and_deploy.sh
./import_and_deploy.sh
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

## 📦 Package Contents

The lab package includes:

- **Service Desk Assistant Agent** - Pre-configured agent with IT support capabilities
- **Python Tools** - Ticket creator and policy lookup tools
- **Knowledge Base** - Company IT policies document
- **Lab Guides** - Step-by-step instructions for both labs
- **Import Script** - Automated setup for quick deployment

---

## 🎯 Learning Path

### Recommended Approach

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

## 📊 Lab Comparison

| Aspect | Lab 1 | Lab 2 |
|--------|-------|-------|
| **Duration** | 60 min | 60 min |
| **Method** | Manual testing | Automated testing |
| **Interface** | Visual dashboard | Command line |
| **Focus** | Interactive exploration | Programmatic evaluation |
| **Best For** | Development & debugging | Regression testing |
| **Output** | Visual insights | Metrics & reports |

---

## 🛠️ Agent Capabilities

The Service Desk Assistant can help with:

1. **IT Ticket Creation** - Create support tickets for hardware, software, access, or security issues
2. **Policy Lookup** - Quick answers to common policy questions
3. **Knowledge Base Search** - Comprehensive company IT policies

**Available Tools:**
- `create_ticket` - Creates IT support tickets with priority and category
- `lookup_policy` - Provides quick policy guidance

**Knowledge Base Topics:**
- Data Handling Policy
- Third Party Access Policy
- Security Incident Reporting Policy
- Acceptable Use Policy

---

## 📈 Success Metrics

### Lab 1 Success Criteria
- ✅ Agent responds to all 9 messages
- ✅ Creates tickets when appropriate
- ✅ References correct policies
- ✅ Provides complete answers
- ✅ Reasonable cost per conversation

### Lab 2 Success Criteria
- ✅ 80%+ journey success rate
- ✅ High text match scores
- ✅ Correct tool calls
- ✅ Consistent performance
- ✅ Automated evaluation runs successfully

---

## 🔗 Additional Resources

- [Watson Orchestrate Documentation](https://developer.watson-orchestrate.ibm.com)
- [AgentOps Dashboard Guide](https://developer.watson-orchestrate.ibm.com/evaluate)
- [Evaluation Framework](https://developer.watson-orchestrate.ibm.com/evaluate/framework)
- [LLM Vulnerability Guide](https://developer.watson-orchestrate.ibm.com/evaluate/llm_vulnerability)

---

## 🚦 Getting Started

Ready to begin? Start with **[Lab 1: UI Dashboard](lab1.md)**!

**Total Lab Time:** 2 hours  
**Difficulty:** Beginner to Intermediate  
**Outcome:** Complete understanding of agent monitoring and evaluation

---

## 💡 Support

For questions or issues:
- Review the lab guides thoroughly
- Check the troubleshooting sections
- Verify prerequisites and credentials
- Ensure Watson Orchestrate CLI is properly installed

---

*Last Updated: April 2026*