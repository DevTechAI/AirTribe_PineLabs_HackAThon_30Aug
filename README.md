# Pine Labs Integration Assistant - ReAct Edition

A **ReAct (Reasoning and Acting)** powered AI assistant that makes integrating Pine Labs Online's payment APIs self-explanatory, fast, and resilient to common mistakes.

## 🤖 What is ReAct?

ReAct is an AI framework that combines **Reasoning** and **Acting** in an iterative process:

1. **🧠 Reason**: Analyze user requests and decide what actions to take
2. **🎯 Act**: Execute specific actions like code generation or validation
3. **👁️ Observe**: Review action results and learn from outcomes
4. **💬 Respond**: Provide clear, actionable responses to users

## ✨ Features

### 🤖 ReAct Agent
- **Intelligent Reasoning**: Analyzes your requests and determines optimal actions
- **Action Execution**: Performs tasks like code generation, validation, testing
- **Result Observation**: Reviews outcomes and provides feedback
- **Conversational Interface**: Natural language interaction with transparent reasoning

### 🧪 Interactive Capabilities
- **Code Generation**: Auto-generate integration code in Python, JavaScript, Java
- **Payload Validation**: Real-time validation of API payloads and error detection
- **Integration Testing**: Test your integrations with simulated responses
- **Error Fixing**: AI-powered error resolution with corrected code

### 📊 Dashboard & Analytics
- **Integration Tracking**: Monitor all your integration attempts
- **Success Metrics**: Track success rates and common issues
- **Visual Analytics**: Charts and graphs for integration insights

### 📚 Smart Documentation
- **Interactive API Reference**: Browse Pine Labs API endpoints
- **Code Examples**: Multi-language integration examples
- **Best Practices**: Integration guidelines and tips

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up Environment
```bash
# Copy environment template
cp .env.example .env

# Edit with your API keys
nano .env
```

**Required environment variables:**
```bash
OPENAI_API_KEY=your_openai_api_key_here
PINE_LABS_BASE_URL=https://api-sandbox.pinelabs.com
PINE_LABS_MERCHANT_ID=your_merchant_id
PINE_LABS_SECRET_KEY=your_secret_key
```

### 3. Initialize Database
```bash
# Set Flask environment
export FLASK_APP=app.py

# Create database tables
flask db upgrade
```

### 4. Run the Application
```bash
python run.py
```

### 5. Access the Interfaces
- **ReAct Agent**: http://localhost:5000/react
- **Playground**: http://localhost:5000/playground
- **Dashboard**: http://localhost:5000/dashboard
- **Documentation**: http://localhost:5000/docs

## 🎯 ReAct Agent Demo

Experience the ReAct agent in action:

```bash
python react_demo.py
```

This demo showcases:
- Code generation workflows
- Payload validation processes
- Integration testing scenarios
- Error fixing capabilities

## 💬 Using the ReAct Agent

### Natural Language Commands

The agent understands natural language requests:
