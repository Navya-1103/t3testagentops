# GitHub Pages Setup

This directory contains the GitHub Pages site for the Service Desk Assistant Lab Guide.

## Viewing the Site

Once published, the site will be available at:
`https://[your-username].github.io/[repository-name]/`

## Local Testing

To test locally with Jekyll:

```bash
# Install Jekyll (if not already installed)
gem install bundler jekyll

# Navigate to docs directory
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

## Publishing to GitHub Pages

1. Push this repository to GitHub
2. Go to repository Settings → Pages
3. Under "Source", select "Deploy from a branch"
4. Select branch: `main` (or your default branch)
5. Select folder: `/docs`
6. Click Save

GitHub will automatically build and deploy your site.

## File Structure

```
docs/
├── _config.yml          # Jekyll configuration
├── index.md             # Landing page
├── lab1.md              # Lab 1: UI Dashboard Guide
├── lab2.md              # Lab 2: Evaluation Framework Guide
└── README.md            # This file
```

## Customization

### Theme
The site uses the Cayman theme. To change it, edit `_config.yml`:
```yaml
theme: jekyll-theme-minimal  # or other GitHub Pages themes
```

### Navigation
Add navigation links by editing the markdown files. Use relative links:
```markdown
[Link to Lab 1](lab1.md)
[Back to Home](index.md)
```

## Troubleshooting

**Site not updating:**
- Wait 1-2 minutes after pushing changes
- Check GitHub Actions tab for build status
- Verify Pages is enabled in repository settings

**404 errors:**
- Ensure `/docs` folder is selected in Pages settings
- Check file names match links (case-sensitive)
- Verify `index.md` exists in docs directory

**Theme not applying:**
- Ensure `_config.yml` is in docs directory
- Check theme name is valid GitHub Pages theme
- Clear browser cache

## Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Themes](https://pages.github.com/themes/)