from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>DevOps Project</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
                height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .container {
                text-align: center;
                padding: 40px;
                border-radius: 20px;
                background-color: rgba(255, 255, 255, 0.05);
                box-shadow: 0 0 30px rgba(0, 0, 0, 0.4);
            }
            h1 {
                font-size: 2.8rem;
                margin-bottom: 10px;
                color: #00d4ff;
            }
            p {
                font-size: 1.2rem;
                color: #d1d1d1;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello from DevOps Project 👋</h1>
            <p>This app is running inside a Docker container via a Jenkins pipeline.</p>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
