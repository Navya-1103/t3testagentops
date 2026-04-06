---
layout: page
title: Lab 2
# permalink: /lab2/
nav_order: 2
---


# Lab 2: Evaluation Framework - Automated Testing

## Lab Overview

**Duration:** 60 minutes
**Prerequisites:** Completed Lab 1, CLI installed, Python 3.8+

**Target Audience:** Developers, data scientists, and QA engineers who need programmatic access to detailed metrics, want to automate testing, and require deeper insights than the UI dashboard provides.


---

## Part 1: Setup (10 minutes)

### Step 1.1: Activate Environment

```bash
# If not already activated from Lab 1
orchestrate env activate

# When prompted, enter:
# - WxO Service Instance URL: [Your instance URL]
# - API Key: [Your API key]
```

### Step 1.2: Create Directory Structure

```bash
cd ServiceDeskAgent-Package
mkdir -p evaluation/output evaluation/results
```

### Step 1.3: Verify Agent Name

```bash
orchestrate agents list | grep "Service_Desk"
```


---

## Part 2: Create User Stories (10 minutes)

### Create stories.csv

Create `evaluation/stories.csv`:

**Important:** Replace `[Your_Agent_Name]` with your actual agent name.

```csv
story,agent
Can I store customer data in a shared Google Sheet?,[Your_Agent_Name]
Is two-factor authentication required for VPN access?,[Your_Agent_Name]
I received a phishing email can you help me report it?,[Your_Agent_Name]
I need access to the customer database can you create a ticket?,[Your_Agent_Name]
My laptop was stolen with customer data on it what do I do?,[Your_Agent_Name]
```


---

## Part 3: Define Evaluation Tools (15 minutes)

### Create tools.py

Create `evaluation/tools.py`:

```python
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
```

### Test tools.py

```bash
cd evaluation
python3 tools.py
```


---

## Part 4: Generate Test Cases (10 minutes)

### Run Generate Command

```bash

orchestrate evaluations generate \
  --stories-path ./evaluation/stories.csv \
  --tools-path ./evaluation/tools.py \
  --output-dir ./evaluation/output
```

>
> **ALTERNATIVE APPROACH:** Instead of generating synthetic test cases, you can capture real interactions with your agent:
> - **Via UI:** Chat with your agent in Watson Orchestrate UI, then export the conversation as test data
> - **Via ADK (Agent Development Kit):** Programmatically interact with your agent using the ADK SDK and capture the conversation flow
>
> Synthetic generation (what we're doing here) is faster for creating many test scenarios, while captured interactions provide real-world test data. Choose based on your testing needs.

### Verify Generated Files

```bash
ls -la ./evaluation/output/
ls -1 ./evaluation/output/[Your_Agent_Name]_test_cases/ | wc -l
```

Expected: 5 test case files

### Review Test Case Structure

```bash
cat ./evaluation/output/[Your_Agent_Name]_test_cases/synthetic_test_case_1.json | python3 -m json.tool
```


---

## Part 5: Run Evaluation (10 minutes)

### Configure Environment

Create `.env` file from the example:

```bash
# Copy example file
cp exampleDotEnv.txt .env

# Edit with your credentials
nano .env  # or use your preferred editor
```

Fill in your actual values:
```
WO_API_KEY=your-actual-api-key
WO_INSTANCE=https://your-actual-instance-url
USE_GATEWAY_MODEL_PROVIDER=groq
DEFAULT_MODEL=groq/openai/gpt-oss-120b
```

Verify configuration:
```bash
cat .env
```


### Run Evaluation

```bash
orchestrate evaluations evaluate \
  --test-paths ./evaluation/output/[Your_Agent_Name]_test_cases/ \
  --output-dir ./evaluation/results/ \
  --env-file .env
```


### Locate Results

```bash
ls -la ./evaluation/results/
```

Example: `./evaluation/results/2026-04-02_14-30-15/`

---

## Part 6: Analyze Results (15 minutes)

### View Summary Metrics

```bash
cat ./evaluation/results/2026-04-02_14-30-15/summary_metrics.csv
```


### Calculate Success Rate

```bash
grep "1.0,Summary Matched" ./evaluation/results/2026-04-02_14-30-15/summary_metrics.csv | wc -l
wc -l < ./evaluation/results/2026-04-02_14-30-15/summary_metrics.csv
```

### Run Detailed Analysis

```bash
orchestrate evaluations analyze \
  -d ./evaluation/results/2026-04-02_14-30-15
```

**Navigation:**
- `↓` / `↑` - Scroll
- `Space` - Page down
- `q` - Quit


### Identify Issues

```bash
grep -E "0.0|0.5" ./evaluation/results/2026-04-02_14-30-15/summary_metrics.csv
```


### Review Individual Results

```bash
cat ./evaluation/results/2026-04-02_14-30-15/synthetic_test_case_1.metadata.json | python3 -m json.tool
cat ./evaluation/results/2026-04-02_14-30-15/messages/synthetic_test_case_1.messages.json | python3 -m json.tool
```

---

## Part 7: Key Insights (5 minutes)


### Optimization Opportunities

**Agent Improvements:**
- Refine instructions
- Add examples
- Clarify tool usage

**Test Refinements:**
- Update expected keywords
- Adjust response templates
- Modify tool expectations

**Knowledge Base:**
- Add clearer headers
- Include more examples
- Improve policy wording

### Re-run After Changes

```bash
orchestrate evaluations evaluate \
  --test-paths ./evaluation/output/[Your_Agent_Name]_test_cases/ \
  --output-dir ./evaluation/results/ \
  --env-file .env
```

---

## Lab Comparison

| Aspect | Lab 1 | Lab 2 |
|--------|-------|-------|
| Method | Manual | Automated |
| Interface | Visual | CLI |
| Feedback | Real-time | Batch |
| Use Case | Debugging | Regression |
| Scalability | Limited | High |


---

## Troubleshooting

**Generate fails:**
```bash
orchestrate agents list  # Verify agent name
```

**Evaluation fails with 404:**
- Check model configuration in .env
- Verify matches agent's model

**All scores 0.0:**
- Verify agent has tools assigned
- Check knowledge base processed
- Test agent manually first

---

## Next Steps

1. Automate evaluation (shell script, CI/CD)
2. Expand test coverage
3. Track improvements over time
4. Integrate with deployment pipeline

---



