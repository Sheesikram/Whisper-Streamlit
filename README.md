# 🎧 Audio Transcription App with Whisper AI

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI Whisper](https://img.shields.io/badge/OpenAI_Whisper-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/research/whisper)

A user-friendly web application for converting speech in audio files to text using OpenAI's Whisper speech recognition model.

![image](https://github.com/user-attachments/assets/5f988ff3-b9c2-4755-8e67-9365bb51e9ba)

## ✨ Features

- 🎵 Supports WAV, MP3, and MP4 audio formats
- ⚡ Real-time transcription using AI
- 🔊 Built-in audio player for original file playback
- 🎨 Simple and intuitive Streamlit interface
- 🤖 Powered by OpenAI's Whisper (base model)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- FFmpeg (required by Whisper)

**Install FFmpeg:**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# MacOS
brew install ffmpeg

# Windows (via chocolatey)
choco install ffmpeg
```

### Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/audio-transcription-app.git
cd audio-transcription-app
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

### Usage
```bash
streamlit run app.py
```

## 🛠️ How to Use
1. Upload an audio file through the drag-and-drop interface
2. Click "Transcribe Audio" in the sidebar
3. View transcription results in the main panel
4. Play back original audio using the built-in player

## 📚 Tech Stack
- **Python** (Primary language)
- **Streamlit** (Web interface)
- **OpenAI Whisper** (Speech recognition engine)
- **FFmpeg** (Audio processing)

## 🌟 Roadmap
- [ ] Multilingual transcription support
- [ ] Live audio transcription extension
- [ ] Browser extension development
- [ ] Support for larger Whisper models
- [ ] Enhanced UI with progress indicators

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments
- Special thanks to Muhammad Usama for development support
- OpenAI for creating the Whisper model
- Streamlit for the amazing app framework

## ⚠️ Note
- The base Whisper model has moderate accuracy - consider using larger models for production
- Audio files are processed locally (no cloud storage)
- Maximum file size limited by Streamlit's uploader constraints

---

📄 **License**  
MIT License - See [LICENSE](LICENSE) for details
```

Key elements included:
1. Badges for key technologies
2. Clear installation instructions
3. FFmpeg setup guidance (critical for Whisper)
4. Visual hierarchy with emojis
5. Roadmap aligning with your future goals
6. Acknowledgments section
7. Contribution guidelines
8. Clear usage instructions

To use this:
1. Create a `README.md` file in your project root
2. Copy this content
3. Replace placeholder URLs with your actual repo links
4. Add a real screenshot (replace placeholder URL)
5. Update license if needed

