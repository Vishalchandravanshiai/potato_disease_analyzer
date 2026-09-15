import gradio as gr
import numpy as np
import tensorflow as tf

# ✅ Load model
model = tf.keras.models.load_model("potato_model.h5")

# 🔥 Prediction function
def predict_image(img):

    if img is None:
        return "❌ Please upload an image"

    img = img.resize((128,128))
    img_array = np.array(img)/255.0

    # ✅ Validation checks
    green_ratio = np.mean(img_array[:,:,1])
    std_dev = np.std(img_array)
    color_var = np.var(img_array)

    if green_ratio < 0.25 or std_dev < 0.08 or color_var < 0.01:
        return "❌ Not a potato leaf image"

    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    confidence = np.max(prediction)

    classes = ['Early_Blight', 'Late_Blight', 'Healthy']
    result = classes[np.argmax(prediction)]

    if confidence < 0.6:
        return "❌ Uncertain / Not a valid leaf"

    return f"✅ {result}\nConfidence: {confidence:.2f}"


# 🎨 UI with background + glass effect
with gr.Blocks(
    css="""
.gradio-container {
    background-image: url('https://cdn.mos.cms.futurecdn.net/miWNt5bEYRtnCoqsoK5FQ-1280-80.jpg.webp');
    background-size: cover;
    background-position: center;
    min-height: 100vh;
}

/* Main glass card */
.gradio-container > div {
    background: rgba(0, 0, 0, 0.5) !important;
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 20px;
}

/* 🔥 Upload box glass effect */
input, textarea, .gr-box, .gr-input, .gr-image {
    background: rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(15px) !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-radius: 15px !important;
}

/* Button style */
button {
    background: rgba(255,255,255,0.2) !important;
    backdrop-filter: blur(10px);
    border-radius: 10px !important;
    color: white !important;
}

/* Text color */
h1, h3, label, textarea {
    color: white !important;
}
"""
) as demo:

    gr.Markdown("# 🥔 Potato Disease Analyzer")
    gr.Markdown("### Upload or capture a potato leaf image")

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="📸 Upload / Capture Leaf")
            btn = gr.Button("🔍 Analyze", variant="primary")

        with gr.Column():
            output = gr.Textbox(label="📊 Result", lines=3)

    btn.click(fn=predict_image, inputs=image_input, outputs=output)

# 🚀 Launch (NO share=True in Hugging Face)
demo.launch()