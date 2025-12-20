# 🎓 IELTS & PTE AI Coach

An intelligent, AI-powered exam preparation chatbot designed to help students master IELTS and PTE exams through specialized coaching modes and expert guidance.

[![Live Demo](https://img.shields.io/badge/🤗-Live%20Demo-yellow)](https://huggingface.co/spaces/mutahharbhutta/ielts_pte_chatbot)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/mutahharbhutta/ielts_pte_chatbot)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-red)](LICENSE)

---
- Try the [live demo](https://huggingface.co/spaces/mutahharbhutta/ielts_pte_chatbot)
---
## ✨ Features

### 🎯 Four Specialized Coaching Modes
- **General Help**: Comprehensive exam guidance, study strategies, and format explanations
- **Writing Task**: Essay structure, grammar feedback, Task 1 & 2 coaching
- **Speaking Practice**: Mock sessions, Part 1-3 questions, fluency techniques
- **Reading & Listening**: Strategies, question types, time management tips

### ⚡ Powered by Advanced AI
- **Llama 3.3 70B** via GROQ API for lightning-fast, accurate responses
- Expert-level system prompts tailored for each exam section
- Adjustable creativity controls for personalized learning experiences

### 🎨 Premium User Experience
- Beautiful, modern UI with smooth animations
- Gradient-animated branding
- Quick-action buttons for instant access to common queries
- Responsive design that works seamlessly across devices
- Glass-morphism card panels with elegant shadows

### 📚 Comprehensive Coverage
- Both IELTS (Academic & General) and PTE exam formats
- Band descriptors and scoring criteria explanations
- Sample answers and model responses
- Common mistakes and how to avoid them
- Time management strategies

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- GROQ API key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/mutahharbhutta/ielts_pte_chatbot.git
cd ielts_pte_chatbot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

4. **Run the application**
```bash
python app.py
```

The app will launch at `http://localhost:7860`

---

## 🎮 Usage

### Selecting a Mode
Choose from four coaching modes in the control panel:
- **General Help** - Overall exam guidance
- **Writing Task** - Essay and report coaching
- **Speaking Practice** - Conversational practice
- **Reading & Listening** - Comprehension strategies

### Quick Actions
Use pre-configured buttons for instant help:
- Writing Scoring Criteria
- Speaking Part 2 Topics
- Reading Strategies
- Essay Templates
- IELTS vs PTE Comparison
- Time Management Tips

### Adjusting Creativity
Use the temperature slider (0.1 - 1.0) to control response style:
- **Low (0.1-0.4)**: Precise, factual, structured responses
- **Medium (0.5-0.7)**: Balanced creativity and accuracy
- **High (0.8-1.0)**: More creative, varied expressions

---

## 🛠️ Technology Stack

- **Frontend**: Gradio 6.0 (Python-based UI framework)
- **Backend**: Python 3.8+
- **AI Model**: Llama 3.3 70B (via GROQ API)
- **API**: GROQ Cloud API
- **Styling**: Custom CSS with gradient animations
- **Environment**: python-dotenv for configuration

---

## 📁 Project Structure

```
ielts_pte_chatbot/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── README.md             # This file
└── .gitignore            # Git ignore rules
```

---

## 🎯 Key Functionalities

### Intelligent System Prompts
Each mode uses carefully crafted system prompts that mimic real IELTS/PTE instructors:
- Detailed exam format knowledge
- Scoring criteria expertise
- Common mistake identification
- Actionable study strategies

### Conversation Memory
The chatbot maintains context throughout conversations, allowing for:
- Follow-up questions
- Progressive learning
- Personalized feedback based on previous interactions

### Error Handling
- Timeout protection (30-second limit)
- API error handling with user-friendly messages
- Input validation

---

## 🌟 Use Cases

- **Students**: Prepare for IELTS/PTE exams with 24/7 AI coaching
- **Teachers**: Use as a supplementary teaching tool
- **Self-learners**: Get instant feedback on practice tasks
- **Test-takers**: Quick access to exam strategies and tips

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions
- Add more quick-action questions
- Implement voice input for speaking practice
- Add progress tracking features
- Create practice test generators
- Add multilingual support

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Developer

**Mutahhar Ahmad**
- GitHub: [@mutahharbhutta](https://github.com/mutahharbhutta)

---

## 🙏 Acknowledgments

- **GROQ** for providing fast, powerful AI infrastructure
- **Gradio** for the excellent Python UI framework
- **Meta AI** for the Llama 3.3 model
- The IELTS and PTE teaching community for inspiration

---

## 📧 Support

If you encounter any issues or have questions:
- Open an issue on [GitHub](https://github.com/mutahharbhutta/ielts_pte_chatbot/issues)
- Try the [live demo](https://huggingface.co/spaces/mutahharbhutta/ielts_pte_chatbot)

---

<div align="center">

**If you find this project helpful, please consider giving it a ⭐ on GitHub!**

Made with ❤️ and AI

</div>
