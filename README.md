# Aries India - Static Site (Netlify)

## Develop
- Edit HTML files and assets under `assets/`.
- Open `index.html` in a browser to preview locally.

## Deploy to Netlify (free)
1. Create a new Git repo and push this folder.
2. In Netlify: Add new site → Import from Git → select repo.
3. Build command: leave empty. Publish directory: `.`
4. After deploy, enable HTTPS (automatic).

## Connect domain `theariesindia.com`
- In Netlify → Domain management → Add custom domain.
- In Hostinger DNS add records:
  - A `@` → 75.2.60.5
  - A `@` → 99.83.190.102
  - CNAME `www` → your-site-name.netlify.app
- Back in Netlify, verify and set primary (www or apex) and auto-redirect.

## Forms
- Contact form in `contact.html` uses Netlify Forms.
- Submissions appear in Netlify → Forms.

## Edit contact details
- Update phone/WhatsApp/email in header, footer, and `contact.html`.
- Update LocalBusiness JSON-LD in `index.html`.

## SEO
- `sitemap.xml`, `robots.txt`, Open Graph tags, JSON-LD included.
