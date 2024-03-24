import streamlit as st
import requests

# Main Streamlit application
def main():
    st.title("Job Recommendation System")
    
    # User inputs
    title = st.text_input("Enter job title:", "Software Engineer")
    location = st.text_input("Enter location:", "Berlin")
    rows = st.slider("Number of jobs to fetch:", min_value=1, max_value=100, value=10)
    
    if st.button("Fetch Jobs"):
        # API request payload
        payload = {
            "title": title,
            "location": location,
            "rows": rows
        }
        
        # API request headers
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "0c63117868msh5a2f12f252b5985p1ff156jsn28a528f984ba",
            "X-RapidAPI-Host": "linkedin-jobs-scraper-api.p.rapidapi.com"
        }
        
        # Make API request
        try:
            response = requests.post(
                "https://linkedin-jobs-scraper-api.p.rapidapi.com/jobs",
                json=payload,
                headers=headers
            )
            if response.status_code == 200:
                job_data = response.json()
                
                # Display scraped jobs
                st.subheader("Scraped Jobs:")
                for job in job_data:
                    st.write(f"Title: {job['title']}")
                    st.write(f"Company: {job['company']}")
                    st.write(f"Location: {job['location']}")
                    st.write(f"Description: {job['description']}")
                    st.write("-" * 50)
                
                st.success("Jobs fetched successfully!")
            else:
                st.error(f"Error fetching jobs: {response.text}")
        except Exception as e:
            st.error(f"Error fetching jobs: {e}")


if __name__ == "__main__":
    main()