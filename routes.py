from flask import Blueprint, render_template

# Create blueprint for all routes
main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    """Homepage with navigation to all learning paths"""
    return render_template("index.html")

@main_bp.route("/setup")
def setup():
    """Kubernetes cluster setup guide"""
    return render_template("k8sguide_1.02.html")

@main_bp.route("/ansible")
def ansible():
    """Ansible automation for Kubernetes"""
    return render_template("k8s_ansibleguide.html")

@main_bp.route("/security")
def security():
    """Kubernetes cluster security"""
    return render_template("k8s_security.html")

@main_bp.route("/rbac")
def rbac():
    """RBAC setup and implementation"""
    return render_template("rbac_setup.html")

@main_bp.route("/urlworkflow")
def urlworkflow():
    """Microservice workflow in Kubernetes"""
    return render_template("k8s_urlworkflow.html")

@main_bp.route("/flowchart")
def flowchart():
    """Kubernetes request flow diagram"""
    return render_template("flowchart.html")

@main_bp.route("/comparision_terms")
def comparision_terms():
    """Cloud terminology comparison"""
    return render_template("comparision_terms.html")

@main_bp.route("/cncfscope")
def cncfscope():
    """CNCF landscape and tools"""
    return render_template("CNCFTools.html")

@main_bp.route("/cncftoolscomparision")
def cncftoolscomparision():
    """CNCF tools comparison"""
    return render_template("cncftoolscomparision.html")

@main_bp.route("/microk8schallenges")
def microk8schallenges():
    """Microservices architecture challenges"""
    return render_template("microk8schallenges.html")

@main_bp.route("/security-hub")
def security_hub():
    """Kubernetes Security Hub - comprehensive security guide"""
    return render_template("security_hub.html")

@main_bp.route("/api-server-security")
def api_server_security():
    """API Server Hardening and Security"""
    return render_template("api_server_security.html")

@main_bp.route("/pod-security")
def pod_security():
    """Pod Security Standards and implementation"""
    return render_template("pod_security.html")

@main_bp.route("/k8s-security-index")
def k8s_security_index():
    """Kubernetes security comprehensive index"""
    return render_template("k8s_security_index.html")

@main_bp.route("/network-policies")
def network_policies():
    """Network policies and pod isolation"""
    return render_template("network_policies.html")

@main_bp.route("/secrets-management")
def secrets_management():
    """Secrets and data protection"""
    return render_template("secrets_management.html")

@main_bp.route("/certificate-management")
def certificate_management():
    """Certificate management and TLS"""
    return render_template("certificate_management.html")

@main_bp.route("/etcd-security")
def etcd_security():
    """etcd security and backup"""
    return render_template("etcd_security.html")

@main_bp.route("/audit-logging")
def audit_logging():
    """Audit logging and monitoring"""
    return render_template("audit_logging_monitoring.html")

@main_bp.route("/image-scanning")
def image_scanning():
    """Image scanning and registry security"""
    return render_template("image-scanning-registry.html")

@main_bp.route("/supply-chain-security")
def supply_chain_security():
    """Supply chain security"""
    return render_template("supply_chain_security.html")

@main_bp.route("/compliance")
def compliance():
    """Compliance and standards"""
    return render_template("compliance_standards.html")

def register_routes(app):
    """Register all routes with the Flask app"""
    app.register_blueprint(main_bp)
