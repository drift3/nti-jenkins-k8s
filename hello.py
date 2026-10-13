```python
from flask import Flask
from datetime import datetime, timezone

app = Flask(__name__)


@app.route('/')
def home():
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="30">
        <title>DevOps Lab | Application Status</title>

        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: Arial, Helvetica, sans-serif;
                background: #080d19;
                color: #f1f5f9;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 30px 18px;
                background-image:
                    radial-gradient(circle at 15% 20%, #123b5944, transparent 35%),
                    radial-gradient(circle at 85% 80%, #42287833, transparent 35%);
            }}

            .container {{
                width: 100%;
                max-width: 950px;
            }}

            .topbar {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 15px;
                flex-wrap: wrap;
                margin-bottom: 35px;
            }}

            .brand {{
                font-size: 20px;
                font-weight: 800;
                letter-spacing: 1px;
            }}

            .brand span {{
                color: #38bdf8;
            }}

            .live {{
                border: 1px solid #166534;
                background: #052e1b;
                color: #4ade80;
                border-radius: 30px;
                padding: 9px 15px;
                font-size: 12px;
                font-weight: bold;
                letter-spacing: 1px;
            }}

            .hero {{
                background: linear-gradient(145deg, #111c30, #0c1424);
                border: 1px solid #26364d;
                border-radius: 24px;
                padding: 55px 30px;
                text-align: center;
                box-shadow: 0 25px 80px #00000055;
            }}

            .check {{
                width: 100px;
                height: 100px;
                border-radius: 50%;
                border: 2px solid #34d399;
                color: #34d399;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 54px;
                margin: 0 auto 28px;
                background: #064e3b44;
                box-shadow: 0 0 40px #10b98122;
            }}

            .eyebrow {{
                color: #38bdf8;
                font-size: 12px;
                letter-spacing: 3px;
                font-weight: bold;
                margin-bottom: 16px;
            }}

            h1 {{
                font-size: clamp(30px, 6vw, 52px);
                line-height: 1.15;
                margin-bottom: 18px;
            }}

            h1 span {{
                color: #34d399;
            }}

            .description {{
                color: #a7b5c9;
                font-size: 16px;
                line-height: 1.8;
                max-width: 620px;
                margin: 0 auto;
            }}

            .cards {{
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 16px;
                margin-top: 22px;
            }}

            .card {{
                background: #111c30cc;
                border: 1px solid #26364d;
                border-radius: 16px;
                padding: 24px;
                transition: transform 0.2s, border-color 0.2s;
            }}

            .card:hover {{
                transform: translateY(-4px);
                border-color: #38bdf8;
            }}

            .card-label {{
                color: #94a3b8;
                font-size: 12px;
                letter-spacing: 1.5px;
                margin-bottom: 12px;
            }}

            .card-value {{
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 8px;
            }}

            .card-detail {{
                color: #94a3b8;
                font-size: 13px;
                line-height: 1.6;
            }}

            .green {{
                color: #4ade80;
            }}

            .blue {{
                color: #38bdf8;
            }}

            .purple {{
                color: #c4b5fd;
            }}

            .footer {{
                text-align: center;
                color: #64748b;
                font-size: 12px;
                line-height: 1.9;
                margin-top: 28px;
            }}

            .footer strong {{
                color: #94a3b8;
            }}

            @media (max-width: 520px) {{
                .hero {{
                    padding: 40px 20px;
                }}

                .cards {{
                    grid-template-columns: 1fr;
                }}

                .topbar {{
                    align-items: flex-start;
                }}
            }}
        </style>
    </head>

    <body>
        <main class="container">

            <header class="topbar">
                <div class="brand">DEVOPS<span>FORGE</span></div>
                <div class="live">● SYSTEM ONLINE</div>
            </header>

            <section class="hero">
                <div class="check">&#10003;</div>

                <div class="eyebrow">DEPLOYMENT SUCCESSFUL</div>

                <h1>Your Application Is <span>Running!</span></h1>

                <p class="description">
                    Congratulations! Your Flask application is live and responding
                    successfully. This page demonstrates an end-to-end DevOps
                    deployment using Docker, Jenkins, and Kubernetes.
                </p>
            </section>

            <section class="cards">

                <div class="card">
                    <div class="card-label">APPLICATION</div>
                    <div class="card-value green">● Flask Online</div>
                    <div class="card-detail">
                        Python application is responding to HTTP requests.
                    </div>
                </div>

                <div class="card">
                    <div class="card-label">CONTAINERIZATION</div>
                    <div class="card-value blue">Docker</div>
                    <div class="card-detail">
                        Application packaged into a Docker image.
                    </div>
                </div>

                <div class="card">
                    <div class="card-label">CI/CD PIPELINE</div>
                    <div class="card-value purple">Jenkins</div>
                    <div class="card-detail">
                        Automated build, image publishing, and deployment pipeline.
                    </div>
                </div>

                <div class="card">
                    <div class="card-label">ORCHESTRATION</div>
                    <div class="card-value green">Kubernetes</div>
                    <div class="card-detail">
                        Running in your Kubernetes cluster. Check actual pod
                        readiness with kubectl.
                    </div>
                </div>

            </section>

            <footer class="footer">
                <strong>DEVOPS LAB</strong><br>
                Built with Python Flask · Docker · Docker Hub · Jenkins · Kubernetes
                <br>
                Server response time: {current_time}
                <br>
                Page refreshes every 30 seconds
            </footer>

        </main>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
