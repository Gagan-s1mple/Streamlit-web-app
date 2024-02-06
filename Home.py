import streamlit as st

def Home():
    # Define a custom HTML template with embedded JavaScript
    custom_html = """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Greywiz Technologies</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }

            header {
                background-color: #02ab21;
                color: white;
                text-align: center;
                padding: 20px;
            }

            .custom-container {
                padding: 20px;
                margin: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                background-color: white;
            }

            .header-box {
                background-color: #02ab21;
                color: white;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
            }

            .info-box {
                background-color: #f5f5f5;
                padding: 15px;
                border-radius: 5px;
                margin-top: 10px;
            }

            img {
                max-width: 100%;
                height: auto;
                border-radius: 5px;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <!-- Your HTML content here -->
        <header>
            <h1>Welcome to Greywiz Technologies</h1>
        </header>

        <div class="custom-container">
            <div class="header-box">
                <h2>About Greywiz</h2>
            </div>
            <div class="info-box">
                <p>Greywiz is a company started by IT veterans with more than 25+ years of experience
                    in developing product solutions and having deep industry experience and operating knowledge.
                    They provide IT Solutions, products, and platforms development.
                    They also provide expert solutions in Business Intelligence, Data Analytics, AI ML-based products.</p>
            </div>
        </div>

        <div class="custom-container">
            <div class="header-box">
                <h2>Consulting</h2>
            </div>
            <div class="info-box">
                <p>Greywiz works with client’s management teams to enhance efficiencies across the organization,
                    automating the processes and technologies, and creating COE in Data Analytics.</p>
            </div>
        </div>

        <div class="custom-container">
            <div class="header-box">
                <h2>What Greywiz Offers?</h2>
            </div>
            <div class="info-box">
                <p>Greywiz has the right tools and technical expertise to provide “Data Analytics Driven” Solutions
                    to HR Operations & Manufacturing Industries. They have expertise to study, analyze and identify the
                    manufacturing industry problems that are related to Operations, Production planning, Quality Assurance and Control,
                    Engineering and Design, R&D, HR, and Finance and provide intelligent data analytics driven solutions.</p>
            </div>
        </div>

        <div class="custom-container">
            <div class="header-box">
                <h2>Data Driven Analytics Solutions for HR OPERATIONS</h2>
            </div>
            <div class="info-box">
                <p>Greywiz provides a “Data Analytics Driven” Solution for HR Operations that can be used by CXOs, HR Groups,
                    right from Improving ROI on HR, planning strategic growth, guiding HR managers, recruiters who can plan recruitment,
                    onboarding, training, employee engagement, measure and control attrition.</p>
            </div>
        </div>

    </body>
    </html>
    """

    # Use st.markdown to embed the custom HTML template
    st.markdown(custom_html, unsafe_allow_html=True)

# Call the Home function to display the custom webpage
Home()
