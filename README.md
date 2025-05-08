# Python Voice Cloning with Coqui TTS (XTTSv2)

This project demonstrates how to perform voice cloning using Python and the Coqui TTS library, specifically leveraging the powerful XTTSv2 model. It allows you to synthesize speech in a target voice using a short audio sample of that voice.

**⚠️ ETHICAL USE WARNING ⚠️**
Voice cloning technology can be misused for impersonation, creating disinformation, or harassment.
*   **ALWAYS obtain explicit consent** from the person whose voice you intend to clone.
*   **BE TRANSPARENT** about the use of cloned voices.
*   **DO NOT use this technology for malicious or unethical purposes.**
The user of this script is solely responsible for any ethical and legal implications.

## Features

*   Uses Coqui AI's 🐸TTS library.
*   Employs the XTTSv2 model, which is:
    *   **Multilingual:** Supports cloning and synthesis in languages like English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh-cn), Japanese (ja), Hungarian (hu), and Korean (ko).
    *   **Few-shot:** Requires only a short (5-30 seconds) clean audio sample of the target voice.
*   Runs on CPU or GPU (GPU highly recommended for speed).

## Prerequisites

*   **Python:** 3.8 - 3.11 (Python 3.12+ might have compatibility issues with dependencies like PyTorch as of early 2024).
*   **pip:** For installing Python packages.
*   **ffmpeg:** Required for audio processing by Coqui TTS.
    *   **Ubuntu/Debian:** `sudo apt update && sudo apt install ffmpeg`
    *   **macOS (using Homebrew):** `brew install ffmpeg`
    *   **Windows:** Download binaries from [ffmpeg.org](https://ffmpeg.org/download.html) and add the `bin` directory to your system's PATH.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/[your_username]/[your_repo_name].git
    cd [your_repo_name]
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv_tts
    # On Windows
    venv_tts\Scripts\activate
    # On macOS/Linux
    source venv_tts/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: The first time you run the script, Coqui TTS will download the XTTSv2 model files (several GBs). This requires an internet connection and might take some time.*

## Usage

1.  **Prepare your reference audio:**
    *   Create a `.wav` audio file of the voice you want to clone.
    *   **Quality is crucial:** Use a clear, high-quality recording with minimal background noise, no music, and only the target speaker.
    *   **Length:** 5-30 seconds is generally sufficient for XTTSv2.
    *   Place this file in the project directory (e.g., `my_reference_voice.wav`).

2.  **Modify `clone.py` (if needed):**
    Open `clone.py` and update the following variables at the top of the script:
    ```python
    reference_audio_path = "my_reference_voice.wav" # Path to your voice sample
    text_to_speak = "Hello, this is a test of voice cloning. I hope this sounds like the original speaker." # Text to synthesize
    output_audio_path = "cloned_voice_output.wav" # Desired output file name
    language = "en" # Language code for the text and reference audio (e.g., "es", "fr", "de")
    ```

3.  **Run the script:**
    ```bash
    python clone.py
    ```

4.  **Output:**
    The script will generate an audio file (e.g., `cloned_voice_output.wav`) containing the `text_to_speak` synthesized in the voice from your `reference_audio_path`.

## Troubleshooting

*   **Model Download:** The first run downloads models. If it fails, check your internet connection and ensure you have enough disk space.
*   **`Error initializing TTS model: Weights only load failed...` (PyTorch 2.6+ related):**
    This error can occur with newer PyTorch versions (2.6 and above) due to changes in `torch.load`'s default behavior. Coqui TTS might not be fully compatible yet.
    *   **Solution:** Downgrade PyTorch to a version known to be compatible (e.g., 2.3.x or 2.2.x). See comments in `requirements.txt` for example commands.
    ```bash
    # Example for CPU:
    # pip uninstall torch torchvision torchaudio -y
    # pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cpu
    ```
    Replace `cpu` with your CUDA version (e.g., `cu118`, `cu121`) if using GPU. Find commands on the [PyTorch previous versions page](https://pytorch.org/get-started/previous-versions/).
*   **`ffmpeg` not found / `audioread.NoBackendError`:** Ensure `ffmpeg` is installed and accessible in your system's PATH.
*   **Performance:** Voice synthesis is computationally intensive. Using a CUDA-enabled NVIDIA GPU will significantly speed up the process. The script will automatically try to use a GPU if available.
*   **Python Version:** If you face persistent esoteric errors, ensure you are using a Python version compatible with Coqui TTS and its dependencies (typically Python 3.8-3.11).

## Disclaimer

This project is for educational and demonstration purposes only. The creators are not responsible for any misuse of this technology. Always respect ethical guidelines and legal regulations regarding voice cloning and synthesis.

## Acknowledgements

*   This project heavily relies on the amazing work done by the team at [Coqui AI](https://coqui.ai/) and their 🐸TTS library.
*   The XTTSv2 model is a powerful asset for multilingual voice cloning.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details. (You'll need to create a `LICENSE` file, e.g., with the MIT license text if you choose that).