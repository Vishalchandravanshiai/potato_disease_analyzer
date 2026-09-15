# 🥔 Potato Disease Analyzer

A deep learning-based image classification application that analyzes potato leaf images and predicts whether the plant is **Healthy**, affected by **Early Blight**, or affected by **Late Blight**.

The project uses a Convolutional Neural Network (CNN) trained on potato leaf images and provides a simple interface through **Gradio**.

## 🚀 Live Demo

Try the application on Hugging Face:

👉 [Potato Disease Analyzer – Live Demo](https://huggingface.co/spaces/vishalchandravanshii/potato_disease_analyzer)

## 🐙 GitHub Repository

View the complete source code and project files:

👉 [GitHub Repository](https://github.com/Vishalchandravanshii/potato_disease_analyzer)

## 🤖 Model

The trained model is included in this repository as:

`potato_model.h5`

The same trained model is also used by the Hugging Face Space for the live demonstration.

## 🌱 Supported Classes

- 🟢 **Healthy**
- 🟠 **Early Blight**
- 🔴 **Late Blight**

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- NumPy
- Gradio
- Google Colab
- Hugging Face

## 📁 Project Structure

```text
potato_disease_analyzer/
│
├── app.py
├── potato_model.h5
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Vishalchandravanshii/potato_disease_analyzer.git
cd potato_disease_analyzer
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run Locally

Start the Gradio application:

```bash
python app.py
```

The application will launch a Gradio interface where you can upload a potato leaf image and receive a prediction.

## 🧠 Model Overview

The model was trained using **Google Colab** with **TensorFlow/Keras**.

The training process involved:

- Image preprocessing
- Data augmentation
- CNN-based image classification
- Model training and validation
- Saving the trained model as an `.h5` file

## 📊 Prediction

Upload a potato leaf image through the Gradio interface.

The model predicts one of the following classes:

- Healthy
- Early Blight
- Late Blight

## ⚠️ Disclaimer

This project is intended for **educational and research purposes**. It should not be considered a substitute for professional agricultural diagnosis or expert agricultural advice.

## 👨‍💻 Author

**Vishal Chandravanshi**

B.Tech – Artificial Intelligence & Data Science

---

⭐ If you find this project useful, consider giving the repository a star!
