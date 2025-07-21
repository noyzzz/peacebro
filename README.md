# ✋ Real-Time Hand Tracking with MediaPipe + OpenCV (Docker + IP Webcam)

This project uses [MediaPipe](https://mediapipe.dev/) to detect and track hands in real-time using video streamed from your Android phone via the IP Webcam app.

Runs entirely in Docker using your provided Conda `environment.yml` and `.env` config for flexibility.

---

## 📦 Features

- 📱 Connects to IP Webcam Android app via `.env` config
- 🧠 Detects up to 2 hands with 21 landmarks each using MediaPipe
- ✌️ Recognizes the peace sign gesture
- 🐳 Dockerized for reproducibility
- ⚙️ Uses `docker-compose` for simple launching
- ✅ Automatically reloads webcam URL from `.env`

---

## 💠 Requirements

- Android device with [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam) app
- Docker + Docker Compose
- WSL2 with WSLg (if using GUI from Windows)
- A valid `environment.yml` file (provided by you)

---

## 📁 Project Structure

```
hand-tracker/
├── main.py               # Hand-tracking script
├── environment.yml       # Conda environment (provided)
├── Dockerfile            # Container setup
├── docker-compose.yml    # Easy run config
├── .env                  # Camera IP config
└── README.md             # This file
```

---

## 🚀 Getting Started

### 1. Start IP Webcam on your Android

- Install **IP Webcam** from the Play Store
- Start the camera server
- Note the stream URL, e.g.:  `http://192.168.1.79:8080/video`

### 2. Create `.env` file

```env
IP_CAM_URL=http://192.168.1.79:8080/video
```

### 3. Build and Run the App

```bash
docker compose build
docker compose up
```

> 💻 On WSL2 with WSLg, `cv2.imshow()` should open normally.

---

## 🧠 How It Works

- `main.py` loads the IP camera stream from `.env`
- MediaPipe detects hand landmarks
- Peace sign is recognized if index + middle fingers are up
- OpenCV displays the video with landmarks and gesture label

---

## 🧪 Peace Sign Detection Logic

```
This is the next step!

```


## 📄 License

MIT License. Use freely for education and research.
