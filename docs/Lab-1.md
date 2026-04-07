---
layout: page
title: Lab 1
# permalink: /lab1/
nav_order: 1
---
## Part 1: Setup (15 minutes)

### Step 1.1: Activate Environment

```bash
# Install Watson Orchestrate CLI (if not already installed)
pip install ibm-watsonx-orchestrate

# Verify installation
orchestrate --version

# Create environment
orchestrate env add -n <environment-name> -u <service-instance-url>

# Activate environment with your credentials
orchestrate env activate <environment name>

# When prompted, enter:
# - API Key: [Your API key]
```

### Step 1.2: Run Import Script

```bash
chmod +x import_and_deploy.sh
./import_and_deploy.sh
```

**What this does:**
- Imports the two Python tools (ticket_creator, policy_lookup)
- Imports the agent with tools automatically attached
- Deploys the agent

### Step 1.3: Add Knowledge Base (Manual)

1. Go to Watson Orchestrate UI

2. Navigate to **Build** → **Service Desk Assistant**

  ![image](./imgs/lab1/step_1a.png)
  ![image](./imgs/lab1/step_1b.png)

3. Go to **Knowledge Base** section and Click **Add source**

  ![image](./imgs/lab1/step_1c.png)

4. Click **New Knowledge** and then click **Upload files** and **Next**

  ![image](./imgs/lab1/step_1d.png)
  ![image](./imgs/lab1/step_1e.png)

5. Upload [Company policies](./knowledge_base/company_policies.txt) under the **knowledge_base** folder


  ![image](./imgs/lab1/step_1f.png)

6. Add name and description

```
Company policies 
```

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

  ![image](./imgs/lab1/step_1h.png)

8. Wait 2-3 minutes for processing

### Step 1.4: Enable Monitoring

1. Click hamburger menu (☰)
2. Select **Analyze**

3. Find **Service Desk Assistant**

4. Toggle **Monitor** to **ON**

  ![image](./imgs/lab1/step_2a.png)

  ![image](./imgs/lab1/step_2c.png)

---

## Part 2: Generate Test Conversations (20 minutes)

1. Click hamburger menu (☰)
2. Select **Chat**

  ![image](./imgs/lab1/step_2d.png)

3. Click on **Service Desk Assistant**

  ![image](./imgs/lab1/step_2e.png)

### Conversation 1: Simple Policy Questions

**Message 1:**
```
Can I store customer data in a shared Google Sheet?
```
  ![image](./imgs/lab1/sda_simple_step1.png)

**Message 2:**
```
Is two-factor authentication required for VPN access?
```

  ![image](./imgs/lab1/sda_simple_step2.png)

**Message 3:**
```
Who do I contact for vendor approval?
```

  ![image](./imgs/lab1/sda_simple_step3.png)

---

### Conversation 2: Complex Policy Questions

**Message 1:**
```
Walk me through the complete process for getting a new vendor approved for data access. Include all required approvals and timeline.
```

  ![image](./imgs/lab1/sda_complex_step1.png)

**Message 2:**
```
What's the difference between approval requirements for US vendors versus EU vendors? Be specific about what additional steps are needed for EU.
```

  ![image](./imgs/lab1/sda_complex_step2.png)

**Message 3:**
```
If I accidentally expose customer PII, what exactly should I do? Give me the step-by-step incident response process.
```
  ![image](./imgs/lab1/sda_complex_step3.png)

---

### Conversation 3: Tool Usage and Tickets

**Message 1:**

```
I received a suspicious email asking for my password. I think it's phishing. Can you help me report this?
```

```
abc123@gmail.com
```

  ![image](./imgs/lab1/sda_tool_step1.png)

**Message 2:**
```
I need access to the customer analytics database for Q1 reporting. Can you create a ticket for this access request?
```

```
abc123@gmail.com
```

  ![image](./imgs/lab1/sda_tool_step2.png)

**Message 3:**
```
My laptop was stolen from my car last night. It has customer data on it. What do I do?
```

  ![image](./imgs/lab1/sda_tool_step3.png)

---

## Part 3: Access Dashboard (5 minutes)

1. Click hamburger menu (☰)
2. Select **Analyze**

  ![image](./imgs/lab1/step_2a.png)

3. Find and Click on **Service_Desk_Assistant**

  ![image](./imgs/lab1/step_3b.png)

4. Click **View Dashboard**

  ![image](./imgs/lab1/step_3c.png)

---

## Part 4: Evaluation Section (10 minutes)


### 4.1 Overall Alerts and Basic Info

- Total conversations
- Total messages
- Active alerts
- Time range selector

  ![image](./imgs/lab1/step_4a.png)

### 4.2 Conversation Metrics

**Charts:**
- Conversations over time
- Average cost per conversation
- Success rate
- Response time trends

  ![image](./imgs/lab1/conversation.png)

### 4.3 Message Metrics

**Charts:**
- Messages over time
- Input tokens vs output tokens
- Average tokens per message
- Token cost breakdown

  ![image](./imgs/lab1/step_4b.png)


### 4.4 Tool Metrics

  ![image](./imgs/lab1/step_4c.png)


**Note:** For detailed tool analysis, use **Analysis → Tools** tab (covered in Part 5.3).

---

## Part 5: Analysis Section (15 minutes)


### 5.1 Conversation-Level Dashboard

1. Navigate to **Analysis** section
2. Click **Conversations** tab


  ![image](./imgs/lab1/step_5a.png)

3. Sort by Cost (descending)
4. Click on most expensive conversation

### 5.2 Message-Level Dashboard

1. Click **Messages** tab


  ![image](./imgs/lab1/step_5b.png)

2. Sort by output tokens (descending)
3. Click on highest token message

### 5.3 Tool-Level Dashboard

1. Click **Tools** tab


  ![image](./imgs/lab1/step_5c.png)

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


