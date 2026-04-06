---
layout: page
title: Lab 1
# permalink: /lab1/
nav_order: 2
---
## Part 1: Setup (15 minutes)

### Step 1.1: Activate Environment

```bash
# Install Watson Orchestrate CLI (if not already installed)
pip install ibm-watsonx-orchestrate

# Verify installation
orchestrate --version

# Activate environment with your credentials
orchestrate env activate

# When prompted, enter:
# - WxO Service Instance URL: [Your instance URL]
# - API Key: [Your API key]
```

### Step 1.2: Run Import Script

```bash
cd ServiceDeskAgent-Package
chmod +x import_and_deploy.sh
./import_and_deploy.sh
```

**What this does:**
- Imports the two Python tools (ticket_creator, policy_lookup)
- Imports the agent with tools automatically attached
- Deploys the agent

### Step 1.3: Add Knowledge Base (Manual)

1. Go to Watson Orchestrate UI
2. Navigate to **Agents** → **Service_Desk_Assistant**
3. Go to **Knowledge Base** section
4. Click **Add Documents**
5. Upload `knowledge_base/company_policies.txt`
6. Add description:

```
Company IT Policies Knowledge Base

This document contains comprehensive IT policies covering:
- Data Handling Policy
- Third Party Access Policy  
- Security Incident Reporting Policy
- Acceptable Use Policy

Use this knowledge base to answer detailed policy questions.
For quick common questions, try the lookup_policy tool first.
```

7. Click **Save**
8. Wait 2-3 minutes for processing

### Step 1.4: Enable Monitoring

1. Click hamburger menu (☰)
2. Select **Analyze**
3. Find **Service_Desk_Assistant**
4. Toggle **Monitor** to **ON**

---

## Part 2: Generate Test Conversations (20 minutes)


### Conversation 1: Simple Policy Questions

**Message 1:**
```
Can I store customer data in a shared Google Sheet?
```

**Message 2:**
```
Is two-factor authentication required for VPN access?
```

**Message 3:**
```
Who do I contact for vendor approval?
```

**⏰ WAIT 10 MINUTES**

---

### Conversation 2: Complex Policy Questions

**Message 1:**
```
Walk me through the complete process for getting a new vendor approved for data access. Include all required approvals and timeline.
```

**Message 2:**
```
What's the difference between approval requirements for US vendors versus EU vendors? Be specific about what additional steps are needed for EU.
```

**Message 3:**
```
If I accidentally expose customer PII, what exactly should I do? Give me the step-by-step incident response process.
```

**⏰ WAIT 10 MINUTES**

---

### Conversation 3: Tool Usage and Tickets

**Message 1:**
```
I received a suspicious email asking for my password. I think it's phishing. Can you help me report this?
```

**Message 2:**
```
I need access to the customer analytics database for Q1 reporting. Can you create a ticket for this access request?
```

**Message 3:**
```
My laptop was stolen from my car last night. It has customer data on it. What do I do?
```

---

## Part 3: Access Dashboard (5 minutes)

1. Click hamburger menu (☰)
2. Select **Analyze**
3. Find **Service_Desk_Assistant**
4. Click **View Dashboard**


---

## Part 4: Evaluation Section (10 minutes)


### 4.1 Overall Alerts and Basic Info

- Total conversations
- Total messages
- Active alerts
- Time range selector

### 4.2 Conversation Metrics

**Charts:**
- Conversations over time
- Average cost per conversation
- Success rate
- Response time trends

**Key Observations:**
- 3 distinct spikes (your conversations)
- 10-minute gaps between spikes
- Cost variation between conversations

### 4.3 Message Metrics

**Charts:**
- Messages over time
- Input tokens vs output tokens
- Average tokens per message
- Token cost breakdown

**Key Observations:**
- Which messages generated most output tokens
- Input/output ratio patterns
- Cost drivers

### 4.4 Tool Metrics


**Note:** For detailed tool analysis, use **Analysis → Tools** tab (covered in Part 5.3).

---

## Part 5: Analysis Section (15 minutes)


### 5.1 Conversation-Level Dashboard

1. Scroll to **Analysis** section
2. Click **Conversations** tab
3. Sort by Cost (descending)
4. Click on most expensive conversation

**What to Show:**
- Conversation metadata
- Full conversation flow
- Cost breakdown

### 5.2 Message-Level Dashboard

1. Click **Messages** tab
2. Sort by output tokens (descending)
3. Click on highest token message

**What to Show:**
- Token breakdown (input, context, output)
- Cost per message
- Response time

**Settings Button:**
1. Click ⚙️ on any message
2. View full message details
3. See knowledge base chunks
4. Review tool calls


### 5.3 Tool-Level Dashboard

1. Click **Tools** tab
2. Review tool calls

**What to Show:**
- create_ticket calls
- lookup_policy calls
- Tool parameters and outputs
- Execution times
- Success rates

---

## Part 6: Key Insights (5 minutes)


### Cost Optimization

**Identify:**
- Most expensive question types
- Verbose responses
- Knowledge base retrieval efficiency
- Tool call optimization

### Performance Optimization

**Review:**
- Average response time
- Slowest queries
- Tool execution impact
- Accuracy assessment

### User Experience

**Evaluate:**
- Response quality
- Completeness
- Tool usage appropriateness

---

## Dashboard Sections Summary

### Evaluation Section
- Overall Alerts
- Conversation Metrics
- Message Metrics
- Tool Metrics (basic)

### Analysis Section
- Conversations (drill-down)
- Messages (token analysis)
- Tools (detailed calls)
- Settings (full details)

---

## Troubleshooting

**No data in dashboard:**
- Wait 5-10 minutes
- Verify monitoring enabled
- Refresh dashboard

**Conversations not showing:**
- Check time range filter
- Verify correct agent
- Ensure conversations completed

---

## Next Steps

After Lab 1, proceed to **Lab 2: Evaluation Framework** for automated testing.

---


