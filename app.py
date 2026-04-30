from flask import Flask, render_template, jsonify, request
import datetime, random, os

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    with open(os.path.join(os.path.dirname(__file__), 'index.html')) as f:
        return f.read()

@app.route('/api/status')
def status():
    return jsonify({
        "status": "running",
        "uptime": "99.9%",
        "server": "Flask/DevOps Pipeline",
        "timestamp": datetime.datetime.now().isoformat(),
        "requests": random.randint(1000, 9999)
    })

@app.route('/api/deploy', methods=['POST'])
def deploy():
    data = request.json or {}
    env = data.get('env', 'production')
    return jsonify({
        "success": True,
        "message": f"Update Deployment to {env} triggered successfully 🚀",
        "build_id": f"build-{random.randint(1000,9999)}",
        "timestamp": datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
