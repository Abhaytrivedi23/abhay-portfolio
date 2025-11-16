from flask import Flask

app = Flask(__name__)

# ---- HTML TEMPLATE WITH ADVANCED CSS/JS ----
def page(title, body):
    return f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', sans-serif;
                background: #121212;
                color: #eaeaea;
                overflow-x: hidden;
            }}
            .navbar {{
                display: flex;
                justify-content: center;
                background: #1f1f1f;
                padding: 15px;
                position: sticky;
                top: 0;
                z-index: 10;
                box-shadow: 0 2px 5px rgba(0,0,0,0.4);
            }}
            .navbar a {{
                color: #eaeaea;
                margin: 0 20px;
                text-decoration: none;
                font-size: 18px;
                transition: 0.3s;
            }}
            .navbar a:hover {{
                color: #00e1ff;
                transform: scale(1.1);
            }}
            .container {{
                padding: 40px;
                animation: fadeIn 1s ease;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(20px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            h1 {{
                color: #00e1ff;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 18px;
                line-height: 1.6;
            }}
            .card {{
                background: #1c1c1c;
                padding: 20px;
                margin-top: 20px;
                border-radius: 12px;
                transition: 0.3s;
                box-shadow: 0 0 10px rgba(0, 255, 255, 0.1);
            }}
            .card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
            }}
            .project-title {{
                font-size: 22px;
                color: #00e1ff;
                margin-bottom: 8px;
            }}
            .hero {{
                text-align: center;
                margin-top: 40px;
            }}
            .hero-name {{
                font-size: 40px;
                font-weight: bold;
                color: #00e1ff;
            }}
            .hero-role {{
                font-size: 24px;
                color: #eaeaea;
            }}
            .button {{
                padding: 12px 25px;
                background: #00e1ff;
                color: #000;
                border: none;
                border-radius: 8px;
                margin-top: 20px;
                cursor: pointer;
                font-size: 18px;
                transition: 0.3s;
            }}
            .button:hover {{
                background: #00bdda;
                transform: scale(1.05);
            }}
        </style>

        <script>
            function greetUser() {{
                alert("Welcome to Abhay Trivedi’s Portfolio! 🚀");
            }}
        </script>
    </head>

    <body onload="greetUser()">
        <div class="navbar">
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/projects">Projects</a>
            <a href="/contact">Contact</a>
        </div>

        <div class="container">
            {body}
        </div>
    </body>
    </html>
    """

# ---- PAGES ----

@app.route("/")
def home():
    return page("Home", f"""
        <div class="hero">
            <div class="hero-name">Abhay Trivedi</div>
            <div class="hero-role">Backend Developer</div>
            <button class="button" onclick="location.href='/projects'">View My Projects</button>
        </div>
    """)

@app.route("/about")
def about():
    return page("About", """
        <h1>About Me</h1>
        <div class="card">
            <p>
            I am Abhay Trivedi, a passionate Backend Developer skilled in building 
            efficient server-side applications, working with databases, and creating dashboards. 
            I enjoy solving complex problems and crafting clean backend logic.
            </p>
        </div>
    """)

@app.route("/projects")
def projects():
    return page("Projects", """
        <h1>My Projects</h1>

        <div class="card">
            <div class="project-title">Java Project</div>
            <p>Developed backend features and logic using Java technology.</p>
        </div>

        <div class="card">
            <div class="project-title">Database Project</div>
            <p>Designed and optimized database structure with SQL queries.</p>
        </div>

        <div class="card">
            <div class="project-title">Dashboard Project</div>
            <p>Created interactive dashboards for data visualization.</p>
        </div>
    """)

@app.route("/contact")
def contact():
    return page("Contact", """
        <h1>Contact Me</h1>
        <div class="card">
            <p><b>Phone:</b> 9689161122</p>
            <p><b>Email:</b> abhaytrivedi23@gmail.com</p>
        </div>
    """)

# ---- RUN SERVER ----
if __name__ == "__main__":
    app.run(debug=True)
