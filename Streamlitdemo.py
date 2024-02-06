import streamlit as st
import pymongo

def get_mongo_data():
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/database_one")
    db = client.Simpledatabase
    collection = db.Students

    # Fetch data from MongoDB
    data = list(collection.find())

    return data

def preprocess_data(data):
    # Convert MongoDB ObjectId to str
    for record in data:
        if "_id" in record:
            record["_id"] = str(record["_id"])

    # Flatten nested structures or handle other complex data types as needed
    # You might need to customize this based on the structure of your MongoDB documents

    return data

def main():
    st.title('About Us')

    st.write("""
    ## Our Mission
    Our mission is to empower employment by connecting job seekers and employers in a fast and efficient manner.

    ## Who We Are
    We are a dedicated team of professionals committed to improving the recruitment process. We believe that finding the right job should be easier than splitting an atom. Steered by a team of technologists and recruitment experts, we are transforming the way employers discover talent and job seekers discover opportunities.

    ## What We Do
    We provide a comprehensive platform for job seekers to connect with potential employers. With an ever-growing database of jobs across various industries and functions, we strive to make job search as seamless as possible.

    ## Contact Us
    We'd love to hear from you! Reach out to us at support@jobportal.com.
    """)

    st.markdown(
        """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Team Photo</title>
        <link rel="stylesheet" href="index.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    </head>
    <body>
        <div class="container">
            <img src="https://media.glassdoor.com/l/98/41/c3/04/sunnyvale-ca-office.jpg" alt="Team Photo" style="width:100%;height:auto;">
            <br>
            <form>
                <label for="salary" class="form-label">Expected Salary (in LPA)</label>
                <div class="input-group">
                    <input type="number" id="salary" class="form-control">
                    <button class="btn btn-primary">Calculate</button>
                </div>
                <div class="form-floating">
                    <input type="email" id="location" class="form-control" placeholder="Enter your location" required>
                    <label for="location" class="form-label">Current Location</label>
                </div>
            </form>
            <br>
            <button class="btn btn-danger">Connect with the Team</button>
        </div>
    </body>
    </html>
        """,
        unsafe_allow_html=True,
    )  # Replace with your actual image URL

    # Display MongoDB data in an attractive table using Streamlit components
    st.title("Employee Table")

    mongo_data = get_mongo_data()
    processed_data = preprocess_data(mongo_data)

    # Display table using Streamlit components
    st.table(processed_data)

if __name__ == "__main__":
    main()
