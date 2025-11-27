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

def register_routes(app):
    """Register all routes with the Flask app"""
    app.register_blueprint(main_bp)
