import streamlit as st
import requests
import boto3
from datetime import datetime

# Endpoint URL for the Lambda function
API_URL = 'https://7d4carpcd7.execute-api.us-east-2.amazonaws.com/dev/blog-generation'

def generate_blog(blog_type):
    """Trigger the Lambda function to generate a blog."""
    response = requests.post(API_URL, json={"blog_topic": blog_type})
    if response.status_code == 200:
        try:
            return response.json()  # Assuming the API returns a JSON object
        except Exception as e:
            st.error(f"Failed to parse response: {e}")
            return None
    else:
        st.error(f"Failed to generate blog: {response.text}")
        return None

def get_blog_from_s3(s3_key):
    """Retrieve the blog from S3."""
    s3_client = boto3.client('s3')
    bucket_name = 'aws-bedrockbloggen'
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=s3_key)
        return response['Body'].read().decode('utf-8')
    except Exception as e:
        st.error(f"Failed to retrieve the blog: {str(e)}")
        return None

def main():
    st.title('Blog Generator')
    blog_type = st.text_input('Enter the blog type:')
    
    if st.button('Generate Blog'):
        st.info("Generating blog. Please wait...")
        result = generate_blog(blog_type)
        st.write("Blog generation initiated. Waiting for result...")
        st.write(result)  # Log the result for debugging
        if result and 's3_key' in result:
            s3_key = result['s3_key']
            st.info(f"Retrieving blog content from {s3_key}...")
            blog_content = get_blog_from_s3(s3_key)
            if blog_content:
                st.text_area("Blog Content", blog_content, height=300)
            else:
                st.error("Blog content not found. Please try again later.")
        else:
            st.error("Failed to retrieve S3 key from the result. Result was:")
            st.write(result)

if __name__ == '__main__':
    main()
