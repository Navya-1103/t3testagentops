---
layout: default
title: GitHub Pages Setup Instructions
---

[← Back to Home](index.md)

# GitHub Pages Setup Instructions

This guide will help you publish this lab guide to GitHub Pages.

## Step 1: Push to GitHub

If you haven't already, push this repository to GitHub:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Add Service Desk Assistant lab guides"

# Add remote (replace with your repository URL)
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

# Push to GitHub
git push -u origin main
```

## Step 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. In the left sidebar, click **Pages**
4. Under **Source**:
   - Select branch: `main` (or your default branch)
   - Select folder: `/docs`
5. Click **Save**

## Step 3: Wait for Deployment

- GitHub will automatically build and deploy your site
- This usually takes 1-2 minutes
- You'll see a green checkmark when it's ready
- Your site will be available at: `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`

## Step 4: Verify Your Site

Visit your GitHub Pages URL and verify:
- ✅ Home page loads correctly
- ✅ Navigation links work
- ✅ Lab 1 guide is accessible
- ✅ Lab 2 guide is accessible
- ✅ Code blocks are formatted properly
- ✅ Theme is applied

## Updating Your Site

After making changes:

```bash
# Add changes
git add docs/

# Commit
git commit -m "Update lab guides"

# Push
git push

# Wait 1-2 minutes for GitHub to rebuild
```

## Troubleshooting

### Site Not Loading

**Problem:** 404 error when visiting GitHub Pages URL

**Solutions:**
1. Verify Pages is enabled in repository settings
2. Check that `/docs` folder is selected as source
3. Ensure `index.md` exists in docs directory
4. Wait a few more minutes (initial deployment can take up to 10 minutes)

### Theme Not Applied

**Problem:** Site shows plain text without styling

**Solutions:**
1. Verify `_config.yml` exists in docs directory
2. Check theme name is correct: `jekyll-theme-cayman`
3. Clear browser cache and refresh
4. Check GitHub Actions tab for build errors

### Links Not Working

**Problem:** Navigation links return 404

**Solutions:**
1. Ensure file names match exactly (case-sensitive)
2. Use relative links: `[Link](lab1.md)` not `[Link](/lab1.md)`
3. Verify all referenced files exist in docs directory

### Build Failures

**Problem:** GitHub Actions shows build errors

**Solutions:**
1. Check `_config.yml` syntax is valid YAML
2. Ensure no special characters in file names
3. Verify markdown syntax is correct
4. Check GitHub Actions logs for specific errors

## Custom Domain (Optional)

To use a custom domain:

1. Add a `CNAME` file to docs directory:
   ```bash
   echo "yourdomain.com" > docs/CNAME
   ```

2. Configure DNS with your domain provider:
   - Add CNAME record pointing to: `YOUR-USERNAME.github.io`

3. In GitHub repository settings → Pages:
   - Enter your custom domain
   - Enable "Enforce HTTPS"

## Local Testing (Optional)

To test locally before pushing:

```bash
# Install Jekyll
gem install bundler jekyll

# Navigate to docs
cd docs

# Create Gemfile
cat > Gemfile << 'EOF'
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
gem "jekyll-relative-links"
EOF

# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# View at http://localhost:4000
```

## Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Supported Themes](https://pages.github.com/themes/)
- [Markdown Guide](https://www.markdownguide.org/)

---

[← Back to Home](index.md)