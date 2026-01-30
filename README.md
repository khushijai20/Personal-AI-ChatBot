# Personal AI ChatBot

A modern, production-ready conversational AI application built with Streamlit and Google's Generative AI. This project demonstrates best practices in creating interactive AI-powered interfaces with a polished user experience.

## Overview

Personal AI ChatBot is a sophisticated web application that provides real-time conversational capabilities powered by advanced language models. The application features a responsive design, session management, and professional-grade UI/UX.

## Key Features

- **Real-Time Conversational AI**: Seamless integration with Google's Generative AI models
- **Professional UI/UX**: Custom CSS styling with gradient backgrounds and smooth interactions
- **Responsive Design**: Optimized for desktop and mobile viewing
- **Session Persistence**: Maintains conversation history throughout user sessions
- **Performance Optimized**: Efficient message handling and response generation
- **Environment Configuration**: Secure API key management through environment variables

## Technology Stack

| Component | Technology |
|-----------|------------|
| **Frontend Framework** | Streamlit |
| **AI Engine** | Google Generative AI (Gemini) |
| **Language** | Python 3.8+ |
| **Styling** | Custom CSS + Streamlit Components |
| **Version Control** | Git |

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google API credentials (obtain from [Google AI Studio](https://aistudio.google.com/app/apikey))
- Internet connection

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/khushijai20/Personal-AI-ChatBot.git
cd Personal-AI-ChatBot
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file in the project root directory:

```
GOOGLE_API_KEY=your_google_api_key_here
```

**Note**: Never commit the `.env` file to version control. It's already included in `.gitignore`.

## Usage

### Running the Application

```bash
streamlit run contact_gpt.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

### User Guide

1. **Starting a Conversation**: Type your message in the input field at the bottom
2. **Sending Messages**: Press Enter or click the Send button
3. **Viewing History**: All messages in the current session are displayed in chronological order
4. **Clear Conversation**: Use the sidebar options to manage your session

## Project Structure

```
Personal-AI-ChatBot/
├── contact_gpt.py          # Main application entry point
├── README.md               # Project documentation
├── requirements.txt        # Python package dependencies
├── .env                    # Environment variables (create this)
├── .gitignore              # Git ignore configuration
└── .github/                # GitHub specific files
    └── workflows/          # CI/CD workflows
```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Generative AI API key | Yes |

### Streamlit Configuration

The application uses the following Streamlit settings (configured in `contact_gpt.py`):

- **Page Title**: Personal AI Chat
- **Layout**: Wide
- **Theme**: Dark mode with custom styling
- **Sidebar**: Expanded by default

## Dependencies

Core dependencies managed in `requirements.txt`:

```
streamlit>=1.28.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
```

## Performance Considerations

- **Response Time**: Dependent on Google API latency and model selection
- **Concurrency**: Streamlit handles a single user per session
- **Memory**: Application maintains conversation history in session state
- **Scalability**: For production deployment, consider containerization and load balancing

## Security Best Practices

✅ **Implemented**:
- API key stored in environment variables
- No credentials in source code
- Secure API communication over HTTPS

⚠️ **For Production**:
- Use secrets management service (AWS Secrets Manager, Azure Key Vault, etc.)
- Implement rate limiting
- Add user authentication
- Enable HTTPS for deployment
- Implement audit logging

## Deployment

### Local Deployment

Follow the installation steps above and run with Streamlit.

### Cloud Deployment Options

**Streamlit Cloud** (Recommended for Streamlit apps):
1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Add `GOOGLE_API_KEY` in app secrets
4. Deploy automatically

**Other Platforms**:
- **Heroku**: Use Procfile and requirements.txt
- **AWS**: Use EC2 or Elastic Beanstalk with Docker
- **Google Cloud**: Deploy to Cloud Run with containerization
- **Azure**: Use App Service with container support

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| API key not recognized | Verify `.env` file exists and API key is correct |
| Port 8501 already in use | Run `streamlit run contact_gpt.py --server.port 8502` |
| Slow responses | Check internet connection and Google API quotas |
| CSS not rendering | Clear browser cache and restart Streamlit |

## Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 style guide
- Add docstrings to functions
- Include comments for complex logic
- Test changes before submitting PR

## Roadmap

- [ ] Multi-turn conversation optimization
- [ ] User authentication and profiles
- [ ] Conversation export (PDF/JSON)
- [ ] Dark/Light theme toggle
- [ ] Multiple AI model selection
- [ ] Conversation analytics dashboard
- [ ] Docker containerization
- [ ] CI/CD pipeline automation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) - Web app framework
- [Google Generative AI](https://ai.google.dev/) - AI capabilities
- Community contributors and testers

## Contact & Support

- **Author**: [khushijai20](https://github.com/khushijai20)
- **GitHub Issues**: [Report a bug or request a feature](https://github.com/khushijai20/Personal-AI-ChatBot/issues)
- **Discussions**: [Join community discussions](https://github.com/khushijai20/Personal-AI-ChatBot/discussions)

## Changelog

### Version 1.0.0 (January 30, 2026)
- Initial release
- Core chat functionality
- Google Generative AI integration
- Professional UI design

---

**Last Updated**: January 30, 2026  
**Maintained By**: khushijai20  
**Status**: Active Development ✅