# Routes Map - K8s Skills Flask Application

Complete documentation of all application routes and their corresponding templates.

## Route Definitions

| Route | Method | Template File | Page Title | Purpose |
|-------|--------|---------------|-----------|---------|
| `/` | GET | `index.html` | K8s Skills - Learning Path | Homepage with navigation cards to all learning topics |
| `/setup` | GET | `k8sguide_1.02.html` | Setting Up Kubernetes | Comprehensive guide to deploying high-availability Kubernetes clusters |
| `/ansible` | GET | `k8s_ansibleguide.html` | Ansible Automation for Kubernetes | Automate Kubernetes cluster setup using Ansible playbooks and roles |
| `/security` | GET | `k8s_security.html` | Kubernetes Cluster Security | Securing Kubernetes clusters with RBAC, network policies, and hardening |
| `/rbac` | GET | `rbac_setup.html` | RBAC Plan for Kubernetes | Implementing Role-Based Access Control for secure cluster management |
| `/urlworkflow` | GET | `k8s_urlworkflow.html` | Microservice Workflow in Kubernetes | How user requests flow through Kubernetes components |
| `/flowchart` | GET | `flowchart.html` | Kubernetes Request Flow Diagram | Visual representation of request journey through K8s |
| `/comparision_terms` | GET | `comparision_terms.html` | Cloud Terminology Comparison | Equivalent terminology across Azure, AWS, GCP, and open-source |
| `/cncfscope` | GET | `CNCFTools.html` | CNCF Landscape | Cloud Native Computing Foundation tools and services overview |
| `/cncftoolscomparision` | GET | `cncftoolscomparision.html` | CNCF Tools Comparison | Detailed comparison of CNCF solutions with cloud provider services |
| `/pod-security` | GET | `pod_security.html` | Pod Security Standards | Security contexts, privilege restrictions, and policy enforcement |
| `/k8s-security-index` | GET | `k8s_security_index.html` | Kubernetes Security | Comprehensive security index and best practices |
| `/network-policies` | GET | `network_policies.html` | Network Policies | Pod isolation and zero-trust networking |
| `/secrets-management` | GET | `secrets_management.html` | Secrets Management | Encryption, rotation, and credential management |
| `/certificate-management` | GET | `certificate_management.html` | Certificate Management | TLS/SSL certificates and automated renewal |
| `/etcd-security` | GET | `etcd_security.html` | etcd Security | Database protection and backup |
| `/audit-logging` | GET | `audit_logging_monitoring.html` | Audit Logging | Event tracking, monitoring, and forensics |
| `/image-scanning` | GET | `image-scanning-registry.html` | Image Scanning | Vulnerability scanning and registry security |
| `/supply-chain-security` | GET | `supply_chain_security.html` | Supply Chain Security | CI/CD security and artifact signing |
| `/compliance` | GET | `compliance_standards.html` | Compliance & Standards | CIS, PCI-DSS, HIPAA, SOC 2 compliance |

## Error Routes

| Route | Status Code | Template File | Purpose |
|-------|-------------|---------------|---------|
| (any invalid route) | 404 | `404.html` | Page Not Found - Graceful error handling |
| (server error) | 500 | `500.html` | Internal Server Error - Server error handling |
| (forbidden access) | 403 | `403.html` | Access Forbidden - Permission denied |

## Route Guidelines

### Adding a New Route

1. **Add to `routes.py`:**
```python
@main_bp.route("/new-route")
def new_route():
    """Brief description of what this page does"""
    return render_template("new-template.html")
```

2. **Create template `templates/new-template.html`:**
```django-html
{% extends 'base.html' %}
{% block title %}Page Title Here{% endblock %}
{% block description %}SEO description for search engines{% endblock %}
{% block page_header %}
<h1><i class="fas fa-icon"></i> Page Title</h1>
<p>Subtitle or description</p>
{% endblock %}
{% block content %}
<!-- Your content here -->
{% endblock %}
```

3. **Add navigation link to `index.html` (optional):**
Add a card in the `.nav-grid` section if this is a main topic.

### Route Naming Conventions

- Use lowercase with hyphens for URL routes: `/new-page-name`
- Use underscores for function names: `def new_page_name():`
- Use descriptive names that indicate content: `/kubernetes-setup` not `/page1`
- Keep routes short: `/rbac` not `/role-based-access-control`

### Template Naming Conventions

- Match route name with template filename when possible
- Use lowercase with hyphens: `new-page.html`
- Prefix related pages: `k8s-*.html` for Kubernetes topics, `cncf-*.html` for CNCF tools

## Navigation Structure

The homepage (`index.html`) displays 10 navigation cards:

```
┌─────────────────────────────────────────┐
│  K8s Skills - Learning Path             │
├─────────────────────────────────────────┤
│  [Setup] [Ansible] [Security] [RBAC]    │
│  [Workflow] [Flowchart] [Cloud Terms]   │
│  [CNCF Landscape] [CNCF Comparison]     │
│  [Microservices Challenges]             │
└─────────────────────────────────────────┘
```

Each card:
- Has an icon from Font Awesome
- Links to the corresponding route
- Provides brief description

## Performance Notes

### Route Performance
- All routes serve static HTML from templates
- No database queries (fully static site)
- Average response time: <50ms
- Browser caches pages for 1 hour (HTML) and 30 days (CSS/fonts)

### Optimization Tips
- Caching headers are automatically added by `app.py`
- CSS is centralized in `static/style.css`
- CDN used for external libraries (Google Fonts, Font Awesome)
- All pages extend `base.html` for efficient markup delivery

## Development Workflow

### Local Testing
```bash
# Start development server
python app.py

# Test route
curl http://localhost:5000/setup
```

### Adding Content
1. Create template in `templates/`
2. Add route in `routes.py`
3. Test locally
4. Update homepage navigation (if main topic)
5. Commit and push

### Deployment
Routes automatically work in production:
```bash
FLASK_ENV=production python app.py
# or
gunicorn app:create_app()
```

## Route Modifications

### Future Considerations

- **Blueprints**: If routes grow beyond 20+, organize into multiple blueprints
  - `main_bp` - Homepage, navigation
  - `kubernetes_bp` - /setup, /security, /rbac, /workflow
  - `cloud_bp` - /comparision_terms, /cncfscope, /cncftoolscomparision

- **Documentation Routes**: Add `/docs`, `/api`, `/about` if needed

- **External Links**: Consider `/blog`, `/resources` for external content

## SEO Metadata

All routes support SEO optimization via base.html blocks:

```django-html
{% block title %}Page Title | Site Name{% endblock %}
{% block description %}45-160 character description for search engines{% endblock %}
```

**Current Implementation:**
- Title: Route-specific, typically under 60 characters
- Description: Route-specific, typically 100-150 characters
- Open Graph / Twitter Card tags can be added to base.html

## Testing Routes

### Manual Testing Checklist
- [ ] All routes return 200 status code
- [ ] 404 page displays for invalid routes
- [ ] CSS loads correctly on all pages
- [ ] Fonts and icons load from CDN
- [ ] Links between pages work
- [ ] Back to Home links work
- [ ] Social media links in footer work
- [ ] Page loads within <2 seconds

### Automated Testing (Future)
```python
def test_routes():
    """Test all routes return 200 status"""
    routes = ['/','setup','ansible','security',...]
    for route in routes:
        response = client.get(f'/{route}')
        assert response.status_code == 200
```

---

**Last Updated:** November 28, 2025
**Version:** 1.0.0
**Maintainer:** K8s Skills Learning Team
