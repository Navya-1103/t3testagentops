---
layout: page
title: Lab 1
# permalink: /lab1/
nav_order: 1
---
## Part 1: Setup

### Step 1.1: Activate Environment

```bash
# Install Watson Orchestrate CLI (if not already installed)
uv init 
uv add ibm-watsonx-orchestarte 

OR 

pip install ibm-watsonx-orchestrate 

# Create a virtual environment in the project root
python3.12 -m venv .venv

# Activate it
source .venv/bin/activate    # macOS/Linux

# Install ADK CLI + evaluation support
pip install --upgrade "ibm-watsonx-orchestrate[agentops]"

# Verify installation
orchestrate --version

# Create environment
orchestrate env add -n <environment-name> -u <service-instance-url>

# When prompted, enter:
# - API Key: [Your API key]

# Activate environment with your credentials
orchestrate env activate <environment name>

```

### Step 1.2: Import the tools, knowledge bases and agents 

### Tools 

```bash
orchestrate tools import -k python -f `[The_path_to_your_tools_file]`
```

Expected result:
```
[INFO] - Tool `[Your_tool_name]` imported successfully
```
**Important:** Ensure all you import the four python tools: escalate_ticket.py, request_software.py, diagnose_vpn.py, reset_password.py. 


### Knowledge Base

```bash
orchestrate knowledge-bases import -f `[The_path_to_your_knowledge_bases_file]`
```

Expected result:
```
[INFO] - Tool `[Your_knowledge-bases_name]` imported successfully
```

### Agent


**Important:** Before you import the agent, ensure you change the name of the agent to `[Your_initials]_it_helpdesk_agent`

  ![image](./imgs/prereq/rename-step1.png)

  ![image](./imgs/prereq/rename-step2.png)

```bash
orchestrate agents import -f `[The_path_to_your_agents_file]`
```

Expected result:
```
[INFO] - Tool `[Your_knowledge-bases_name]` imported successfully
```

### Step 1.3 Deploy your agent 

1. Launch your watsonx orchestrate 

  ![image](./imgs/lab1/lab1-step1.png)

2. Click on the hamburger menu and click the **Build** dropdown 

  ![image](./imgs/lab1/lab1-step2.png)

  ![image](./imgs/lab1/lab1-step3.png)

3. Click on your agent 

  ![image](./imgs/lab1/lab1-step4.png)

4. Now click on deploy to make your agent a Live, to allow you to monitor your analytics 

  ![image](./imgs/lab1/lab1-step5.png)

Wait a couple of minutes for your agent to be delpoyed. 

5. Once your agent is deployed, activate monitoring when you receive the notification 

  ![image](./imgs/lab1/lab1-step6.png)

6. Click on the hamburger menu and Navigate to **Analyze**

  ![image](./imgs/lab1/lab1-step7.png)

Wait for the toggle to turn green to indicate the monitoring activated 

  ![image](./imgs/lab1/lab1-step8.png)

---

## Part 2: Generate Test Conversations

1. Click hamburger menu (☰)
2. Select **Chat**

  ![image](./imgs/lab1/lab1-step9.png)

3. Click on **Your_Agent_Name**

  ![image](./imgs/lab1/lab1-step10.png)


### Conversation with Agent 

YOUR AGENT NAME 

**Message 1:**

```
The printer is not working 
```
```
EMP7080
```

```
I cannot print anything
```

  ![image](./imgs/lab1/lab1-step11.png)

**Message 2:**

```
Can I store customer data in a shared google sheet?
```

  ![image](./imgs/lab1/lab1-step12.png)

**Message 3:**

```
I forgot my password. My employee ID is EMP1234.
```
  ![image](./imgs/lab1/lab1-step13.png)

**Message 4:**

```
I really need to install Photoshop, ugh I need it for client meeting. I am so frustrated 
```
```
Can you submit a request? My employee ID is EMP1234
```
  ![image](./imgs/lab1/lab1-step14.png)

**Message 5**

```
This is so annoying that I have to apply for accessing for vscode, why can I not access vscode
```
```
EMP5678
```
  ![image](./imgs/lab1/lab1-step19.png)  

**Message 6:**

```
VPN is not connecting. I keep getting timeout errors. My Employee ID is EMP5678
```
```
slow connection
```

  ![image](./imgs/lab1/lab1-step16.png)


---

## Part 3: Access Dashboard

1. Click hamburger menu (☰)
2. Select **Analyze**

  ![image](./imgs/lab1/lab1-step17.png)

3. Find and Click View Dashboard on **Your_Agent**

  ![image](./imgs/lab1/lab1-step18.png)

---

## Part 4: Evaluation Section


### 4.1 Overall Alerts and Basic Info

- Total conversations
- Total messages
- Active alerts
- Time range selector

  ![image](./imgs/lab1/lab1-step20.png)

### 4.2 Conversation Metrics

**Charts:**
- Conversations over time
- Average cost per conversation
- Success rate
- Response time trends

  ![image](./imgs/lab1/lab1-step21.png)

### 4.3 Message Metrics

**Charts:**
- Messages over time
- Input tokens vs output tokens
- Average tokens per message
- Token cost breakdown

  ![image](./imgs/lab1/message1.png)

#### Agent Content Safety Performance**

  ![image](./imgs/lab1/message3.png)

**Input HAP**: Escalates from 0.0 to 0.87, indicating users submitted queries containing hate, abuse, or profanity content

**Output HAP**: Remains at 0.0 throughout, despite high Input HAP
Agent Performance Assessment:

- The agent successfully maintains safe outputs even when receiving problematic inputs. The agent does NOT respond with HAP content when users send HAP inputs. This demonstrates effective content filtering and safety controls. No PII leakage detected in either inputs or outputs

#### Agent Retrieval and Answer Quality Performance**

  ![image](./imgs/lab1/message.png)

**Answer Relevance**: Scores 0.97 to 1.0 (near perfect). Agent responses directly address user questions

**Context Relevance**: Scores 0.90 to 1.0 (improving over time).Knowledge base retrieval is highly effective

**Faithfulness**: Scores 0.98 to 1.0 (consistently excellent).Agent responses are accurate and grounded in source material without hallucination

- The knowledge base does not need to be changed as all metrics are above 0.90 at 95th percentile. The agent retrieves relevant information and provides accurate as shown by high retrieval quality, high answer quality and faithfulness, scores due to the effective knowledge base. 

#### When to Take Action

##### Modify Knowledge Base If:

- Answer relevance drops below 0.8
- Context relevance shows inconsistent scores
- Users frequently ask follow-up questions

##### Review Agent Instructions If:

- Output HAP score increases above 0
- Responses become too verbose or too brief
- Tool usage patterns seem inefficient


### 4.4 Tool Metrics

  ![image](./imgs/lab1/lab1-step23.png)

---

## Part 5: Analysis Section


### 5.1 Conversation-Level Dashboard

1. Navigate to **Analysis** section
2. Click **Conversations** tab

  ![image](./imgs/lab1/lab1-step24.png)

3. Navigate tabs to view the **Message** to influence what graphs you want to analyze 

  ![image](./imgs/lab1/lab1-step25.png)

---

## Part 6: Key Insights - Message Metrics Analysis

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


