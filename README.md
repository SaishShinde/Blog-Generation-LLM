# blog-generation
Architectural diagram
![image](https://github.com/SaishShinde29/blog-generation/assets/172226158/c2501c6f-5f35-423c-bf5e-d925e1d5f2bf)

![video](https://github.com/SaishShinde/Blog-Generation-LLM/blob/main/Step-By-Step-Explanation.mp4)

# 🤖 LLM-Based Automated Blog Generator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![AWS Bedrock](https://img.shields.io/badge/AWS_Bedrock-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![AWS Lambda](https://img.shields.io/badge/AWS_Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white)

**An automated blog generation system powered by Amazon Bedrock and Llama Chat 13B, with serverless architecture for scalable content creation.**

[Features](#-features) • [Architecture](#-architecture) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-endpoints)

</div>

---

## 🎯 Overview

### Architecture Components

1. **API Gateway**: Entry point for all API requests
2. **AWS Lambda**: Serverless function that processes requests and generates blogs
3. **Amazon Bedrock**: LLM service providing Llama Chat 13B model
4. **Amazon S3**: Storage for generated blog posts
5. **EC2** (Optional): For additional processing or hosting

---

## 🛠️ Technologies Used

### Core Technologies

- **Python 3.8+**: Main programming language
- **Amazon Bedrock**: LLM service for content generation
- **Llama Chat 13B**: Large Language Model for blog generation
- **AWS Lambda**: Serverless compute for API handling
- **API Gateway**: RESTful API endpoint management
- **Amazon S3**: Object storage for blog files
- **boto3**: AWS SDK for Python

### Libraries & Tools

- **Natural Language Processing (NLP)**: For text processing and generation
- **Postman**: API testing and documentation

---

## 📦 Prerequisites

Before you begin, ensure you have the following:

- **AWS Account** with appropriate permissions
- **Python 3.8+** installed
- **AWS CLI** configured with credentials
- **Postman** (optional, for API testing)
- **IAM Permissions** for:
  - AWS Lambda (create, update, invoke)
  - Amazon Bedrock (invoke model)
  - Amazon S3 (read, write)
  - API Gateway (create, deploy)

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SaishShinde/Blog-Generation-LLM.git
cd Blog-Generation-LLM
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up AWS Credentials

Configure your AWS credentials:

```bash
aws configure
```

Or set environment variables:

```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1
```

### 4. Deploy Lambda Layer (boto3)

If using the provided `boto3_layer.zip`:

```bash
aws lambda publish-layer-version \
  --layer-name boto3-layer \
  --zip-file fileb://boto3_layer.zip \
  --compatible-runtimes python3.8 python3.9 python3.10
```

### 5. Create S3 Bucket

```bash
aws s3 mb s3://your-blog-storage-bucket
```

---

## ⚙️ Configuration

### Environment Variables

Set the following environment variables in your Lambda function:

```python
S3_BUCKET_NAME = "your-blog-storage-bucket"
BEDROCK_MODEL_ID = "meta.llama2-13b-chat-v1"  # or your model ID
AWS_REGION = "us-east-1"
```

### Lambda Configuration

- **Runtime**: Python 3.8, 3.9, or 3.10
- **Memory**: 512 MB (minimum recommended)
- **Timeout**: 30 seconds (adjust based on blog length)
- **Layer**: Attach boto3 layer if using

---

## 🚀 Usage

### Local Testing

Run the application locally:

```bash
python app.py
```

### API Request Example

#### Using cURL

```bash
curl -X POST https://your-api-gateway-url.execute-api.us-east-1.amazonaws.com/generate \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Introduction to Machine Learning",
    "length": "medium",
    "tone": "professional"
  }'
```

#### Using Postman

1. Set method to **POST**
2. URL: `https://your-api-gateway-url/generate`
3. Headers: `Content-Type: application/json`
4. Body (raw JSON):

```json
{
  "topic": "The Future of AI",
  "length": "long",
  "tone": "informative",
  "keywords": ["artificial intelligence", "technology", "innovation"]
}
```

### Response Format

```json
{
  "statusCode": 200,
  "body": {
    "message": "Blog generated successfully",
    "blog_id": "blog_1234567890",
    "s3_key": "blogs/blog_1234567890.txt",
    "s3_url": "https://your-bucket.s3.amazonaws.com/blogs/blog_1234567890.txt",
    "generated_at": "2024-01-15T10:30:00Z"
  }
}
```

---

## 🔌 API Endpoints

### Generate Blog

**Endpoint**: `POST /generate`

**Request Body**:

```json
{
  "topic": "string (required)",
  "length": "short|medium|long (optional, default: medium)",
  "tone": "professional|casual|informative (optional, default: professional)",
  "keywords": ["array of strings (optional)"]
}
```

**Response**:

```json
{
  "statusCode": 200,
  "body": {
    "message": "Blog generated successfully",
    "blog_id": "string",
    "s3_key": "string",
    "s3_url": "string",
    "generated_at": "ISO 8601 timestamp"
  }
}
```

### Retrieve Blog

**Endpoint**: `GET /blog/{blog_id}`

**Response**:

```json
{
  "statusCode": 200,
  "body": {
    "blog_id": "string",
    "content": "string",
    "s3_url": "string",
    "created_at": "ISO 8601 timestamp"
  }
}
```

---

## 📁 Project Structure

```
Blog-Generation-LLM/
│
├── app.py                          # Main Lambda function handler
├── requirements.txt                # Python dependencies
├── boto3_layer.zip                 # AWS SDK layer for Lambda
├── Step-By-Step-Explanation.mp4    # Video tutorial
├── README.md                       # This file
│
└── (Architectural diagram image)   # System architecture diagram
```

### Key Files

- **`app.py`**: Main application logic for blog generation
- **`requirements.txt`**: Python package dependencies
- **`boto3_layer.zip`**: Pre-packaged boto3 for Lambda deployment

---

## 📖 Step-by-Step Guide

For a detailed walkthrough, check out the included video:

**📹 [Step-By-Step Explanation Video](./Step-By-Step-Explanation.mp4)**

The video covers:

1. Project setup and configuration
2. AWS services configuration
3. Lambda function deployment
4. API Gateway setup
5. Testing with Postman
6. S3 storage verification

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Guidelines

- Follow PEP 8 style guidelines for Python code
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


