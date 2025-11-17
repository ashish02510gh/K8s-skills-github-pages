from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/setup")
def setup():
    return render_template("k8sguide_1.02.html")

@app.route("/ansible")
def ansible():
    return render_template("k8s_ansibleguide.html")

@app.route("/security")
def security():
    return render_template("k8s_security.html")

@app.route("/rbac")
def rbac():
    return render_template("rbacsetup.html")

@app.route("/urlworkflow")
def urlworkflow():
    return render_template("k8s_urlworkflow.html")

@app.route("/roadmap")
def roadmap():
    return render_template("roadmap.html")

@app.route("/flowchart")
def flowchart():
    return render_template("flowchart.html")

@app.route("/comparision_terms")
def comparision_terms():
    return render_template("comparision_terms.html")

@app.route("/cncfscope")
def cncfscop():
    return render_template("CNCFTools.html")

@app.route("/cncftoolscomparision")
def cncftoolscomparision():
    return render_template("cncftoolscomparision.html")

@app.route("/microk8schallenges")
def microk8schallenges():
    return render_template("microk8schallenges.html")

if __name__ == "__main__":
    app.run(debug=True)
