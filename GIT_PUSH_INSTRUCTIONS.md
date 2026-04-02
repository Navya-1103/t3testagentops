# Git Push Instructions for T3_AgentOps Repository

## Step-by-Step Commands

Run these commands from the `ServiceDeskAgent-Package` directory:

```bash
# 1. Initialize git repository (if not already initialized)
cd ServiceDeskAgent-Package
git init

# 2. Add all files
git add .

# 3. Commit with message
git commit -m "Initial commit: ServiceDeskAgent-Package with Lab 1 and Lab 2"

# 4. Rename branch to main
git branch -M main

# 5. Add remote repository
git remote add origin https://github.ibm.com/sriram-Mythili-Sekar/T3_AgentOps.git

# 6. Push to repository
git push -u origin main
```

## If Repository Already Has Content

If the repository already exists and has content, you may need to pull first:

```bash
# Pull existing content
git pull origin main --allow-unrelated-histories

# Then push
git push -u origin main
```

## Verify Push

After pushing, verify at:
https://github.ibm.com/sriram-Mythili-Sekar/T3_AgentOps

## Files Included

The following files will be pushed:
- agents/native/ServiceDeskAssistant.yaml
- knowledge_base/company_policies.txt
- python_tools/ticket_creator_tool.py
- python_tools/policy_lookup_tool.py
- exampleDotEnv.txt
- import_and_deploy.sh
- LAB1_UI_DASHBOARD_GUIDE.md
- LAB2_EVALUATION_FRAMEWORK_GUIDE.md
- README.md
- .gitignore

## Files Excluded (via .gitignore)

The following will NOT be pushed:
- .env (contains credentials)
- evaluation/output/ (generated during labs)
- evaluation/results/ (generated during labs)
- __pycache__/ and other Python artifacts
- .vscode/ and other IDE files

## Troubleshooting

### Authentication Error
If you get an authentication error, you may need to:
1. Use a personal access token instead of password
2. Configure Git credentials: `git config --global credential.helper store`

### Permission Denied
Ensure you have write access to the repository.

### Merge Conflicts
If there are conflicts, resolve them manually and commit again.

---

# Made with Bob