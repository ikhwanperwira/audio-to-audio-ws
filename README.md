# Minimalist WebSocket Audio to Audio

This project is a minimalistic implementation of a real-time audio streaming application using WebSockets. The server receives audio data from the client, processes it (in this case, simply echoes it back), and the client plays the received audio. This setup serves as a foundational example of a more complex sound-to-sound WebSocket system.

## Overview

- **Client**: Captures audio from the user's microphone, down-samples it, and sends it to the server via WebSocket.
- **Server**: Receives the audio data, processes it, and sends it back to the client.

## Technologies Used

- **HTML5** and **JavaScript** for the client-side implementation.
- **Python** with the **websockets** and **numpy** libraries for the server-side implementation.

## Parameters in `client.html`

### TARGET_DOWNSAMPLE_RATE
```javascript
const TARGET_DOWNSAMPLE_RATE = 16384; // 16 kHz
```
- **Description**: This parameter defines the target sample rate to which the audio captured from the microphone will be down-sampled. In this case, it is set to 16 kHz (16,000 Hz), which is commonly used for voice audio applications to balance quality and data size.

### EXPECTED_BUFFER_SIZE
```javascript
const EXPECTED_BUFFER_SIZE = 1024;
```
- **Description**: This parameter represents the expected size of the audio buffer processed at one time. It is used in calculating the `CALCULATED_BUFFER_SIZE` based on the client sample rate and the target downsample rate. Adjusting this value affects the latency and responsiveness of the audio streaming.

### CALCULATED_BUFFER_SIZE
```javascript
const CALCULATED_BUFFER_SIZE = Math.pow(2, Math.round(Math.log2((EXPECTED_BUFFER_SIZE * sampleRate) / TARGET_DOWNSAMPLE_RATE)));
```
- **Description**: This dynamically calculated buffer size ensures that the buffer length used in the `ScriptProcessorNode` is an appropriate power of two, which is often required for optimal audio processing performance.

## How It Works

1. When the user clicks the "Start" button, the client requests access to the microphone and initializes a WebSocket connection to the server with the target downsample rate.
2. The audio input is captured in real-time and downsampled to the target sample rate.
3. The downsampled audio buffer is sent to the server through the WebSocket connection.
4. The server receives the audio data, and in this minimalistic version, it simply echoes the data back to the client.
5. The client receives the echoed audio data and plays it back.

## Installation

To run this project, you need to have Python and the necessary libraries installed:

1. Clone this repository.
2. Navigate to the project directory.
3. Install the required Python packages:
   ```bash
   pip install websockets numpy
   ```
4. Run the server:
   ```bash
   python server.py
   ```
5. Open `client.html` in a web browser and click the "Start" button to begin audio processing.

## Notes

- This project is intended as a minimalistic version of a sound-to-sound WebSocket application. It can be expanded upon for more complex audio processing tasks, such as applying effects or analyzing audio.
- Ensure your browser supports WebSockets and that microphone access is granted when prompted.

## License

Thanks ChatGPT!