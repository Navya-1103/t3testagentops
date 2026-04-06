---
layout: default
title: Home
---

<div class="nav-links">
  <a href="index.html">🏠 Home</a>
  <a href="SETUP_INSTRUCTIONS.html">⚙️ Setup</a>
  <a href="lab1.html">📊 Lab 1</a>
  <a href="lab2.html">🧪 Lab 2</a>
</div>

# Service Desk Assistant Labs

Welcome to the hands-on lab package for learning **agent monitoring and evaluation** using Watson Orchestrate.

<div class="card">
  <h3>🎯 What You'll Learn</h3>
  <ul>
    <li>Monitor agent performance in real-time</li>
    <li>Analyze conversation metrics and costs</li>
    <li>Automate testing with synthetic test cases</li>
    <li>Optimize agent behavior based on data</li>
  </ul>
</div>

## 📚 Available Labs

<div class="card">
  <h3><a href="lab1.html">Lab 1: AgentOps UI Dashboard</a></h3>
  <p><strong>Duration:</strong> 60 minutes | <strong>Level:</strong> Beginner</p>
  <p><strong>Focus:</strong> Visual monitoring and analysis</p>
  
  <p><strong>What you'll learn:</strong></p>
  <ul>
    <li>Navigate the AgentOps dashboard</li>
    <li>Analyze conversation, message, and tool metrics</li>
    <li>Perform deep-dive investigations</li>
    <li>Identify cost drivers and performance issues</li>
    <li>Optimize agent behavior</li>
  </ul>
  
  <p><strong>Best for:</strong> Business users, product managers, and anyone who wants high-level insights without diving into code.</p>
  
  <a href="lab1.html" class="btn">Start Lab 1 →</a>
</div>

<div class="card">
  <h3><a href="lab2.html">Lab 2: Evaluation Framework</a></h3>
  <p><strong>Duration:</strong> 60 minutes | <strong>Level:</strong> Intermediate</p>
  <p><strong>Focus:</strong> Automated testing and programmatic evaluation</p>
  
  <p><strong>What you'll learn:</strong></p>
  <ul>
    <li>Create user stories for testing</li>
    <li>Define evaluation tools</li>
    <li>Generate synthetic test cases</li>
    <li>Run automated evaluations</li>
    <li>Analyze results programmatically</li>
  </ul>
  
  <p><strong>Best for:</strong> Developers, data scientists, and QA engineers who need programmatic access and automation.</p>
  
  <a href="lab2.html" class="btn">Start Lab 2 →</a>
</div>

## 🚀 Quick Start

<div class="info-box">
  <strong>⏱️ Total Time:</strong> 2 hours (60 min per lab)<br>
  <strong>📚 Difficulty:</strong> Beginner to Intermediate<br>
  <strong>🎓 Outcome:</strong> Complete understanding of agent monitoring and evaluation
</div>

### Prerequisites

```bash
# Install Watson Orchestrate CLI
pip install ibm-watsonx-orchestrate

# Verify installation
orchestrate --version
```

### Installation Steps

```bash
# 1. Activate environment with your credentials
orchestrate env activate

# 2. Navigate to package directory
cd ServiceDeskAgent-Package

# 3. Run import and deployment script
chmod +x import_and_deploy.sh
./import_and_deploy.sh
```

<div class="warning-box">
  <strong>⚠️ Manual Steps Required:</strong>
  <ol>
    <li>Upload knowledge base in Watson Orchestrate UI</li>
    <li>Enable monitoring for the agent</li>
  </ol>
  See <a href="SETUP_INSTRUCTIONS.html">Setup Instructions</a> for details.
</div>

---

## 📊 Lab Comparison

| Aspect | Lab 1 | Lab 2 |
|--------|-------|-------|
| **Duration** | 60 minutes | 60 minutes |
| **Method** | Manual testing | Automated testing |
| **Interface** | Visual dashboard | Command line |
| **Focus** | Interactive exploration | Programmatic evaluation |
| **Best For** | Development & debugging | Regression testing |
| **Output** | Visual insights | Metrics & reports |

---

## 🛠️ Agent Capabilities

<div class="card">
  <h3>Service Desk Assistant Features</h3>
  
  <p><strong>1. IT Ticket Creation</strong></p>
  <p>Create support tickets for hardware, software, access, or security issues</p>
  
  <p><strong>2. Policy Lookup</strong></p>
  <p>Quick answers to common policy questions</p>
  
  <p><strong>3. Knowledge Base Search</strong></p>
  <p>Comprehensive company IT policies covering:</p>
  <ul>
    <li>Data Handling Policy</li>
    <li>Third Party Access Policy</li>
    <li>Security Incident Reporting Policy</li>
    <li>Acceptable Use Policy</li>
  </ul>
</div>

---

## 📈 Success Metrics

<div class="success-box">
  <strong>Lab 1 Success Criteria:</strong>
  <ul>
    <li>✅ Agent responds to all 9 messages</li>
    <li>✅ Creates tickets when appropriate</li>
    <li>✅ References correct policies</li>
    <li>✅ Provides complete answers</li>
    <li>✅ Reasonable cost per conversation</li>
  </ul>
</div>

<div class="success-box">
  <strong>Lab 2 Success Criteria:</strong>
  <ul>
    <li>✅ 80%+ journey success rate</li>
    <li>✅ High text match scores</li>
    <li>✅ Correct tool calls</li>
    <li>✅ Consistent performance</li>
    <li>✅ Automated evaluation runs successfully</li>
  </ul>
</div>

---

## 🔗 Additional Resources

- [Watson Orchestrate Documentation](https://developer.watson-orchestrate.ibm.com)
- [AgentOps Dashboard Guide](https://developer.watson-orchestrate.ibm.com/evaluate)
- [Evaluation Framework](https://developer.watson-orchestrate.ibm.com/evaluate/framework)
- [LLM Vulnerability Guide](https://developer.watson-orchestrate.ibm.com/evaluate/llm_vulnerability)

---

## 🚦 Ready to Start?

<a href="SETUP_INSTRUCTIONS.html" class="btn">📖 Setup Instructions</a>
<a href="lab1.html" class="btn">🚀 Start Lab 1</a>
<a href="lab2.html" class="btn">🧪 Start Lab 2</a>

---

<div class="info-box">
  <strong>💡 Need Help?</strong>
  <ul>
    <li>Review the lab guides thoroughly</li>
    <li>Check the troubleshooting sections</li>
    <li>Verify prerequisites and credentials</li>
    <li>Ensure Watson Orchestrate CLI is properly installed</li>
  </ul>
</div>

---

*Last Updated: April 2026 | Built with ❤️ for Watson Orchestrate*