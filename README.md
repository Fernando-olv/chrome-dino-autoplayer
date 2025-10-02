# 🦖 Chrome Dino Bot  
_Automated Chrome Dino player built with Python, PyAutoGUI and OpenCV_

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![PyAutoGUI](https://img.shields.io/badge/pyautogui-automation-yellow)
![OpenCV](https://img.shields.io/badge/opencv-computer%20vision-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 📌 About  
This project showcases how to use **PyAutoGUI** (for screen automation) and **OpenCV** (for image detection) by creating a simple bot that plays the **Google Chrome Dinosaur Game** automatically.  

The bot scans the screen for the dino and obstacles (cacti, pterodactyls) and presses **space** at the right time to make the dino jump.  

---

## 🛠️ Technologies  
- [Python 3.9+](https://www.python.org/)  
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)  
- [OpenCV](https://opencv.org/)  

---

## ⚡ Features  
✅ Detects the dinosaur and cactus on the screen  
✅ Automates jumps using keyboard events  
✅ Adjustable detection thresholds (`confidence` values)  
✅ Error handling with `ImageNotFoundException`  
🚧 To do:  
- Detect pterodactyl (flying obstacle)  
- Adapt to night mode (grayscale detection idea)  

---

## 📂 Project Structure  

```
.
├── Automacao/
│   ├── img/          # Obstacle images for detection
│   └── dino.png      # Dino reference image
├── bot.py            # Main script
└── README.md
```

---

## ▶️ How to Run  

1. **Clone the repository**  
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

2. **Install dependencies**  
```bash
pip install pyautogui opencv-python
```

3. **Start the Chrome Dino Game**  
- Open Chrome  
- Go offline or type `chrome://dino` in the address bar  
- Make sure the dino and obstacles are visible on the screen  

4. **Run the bot**  
```bash
python bot.py
```

---

## 🎮 Demo  
![Demo](dino_running.gif)

---

## 📌 Notes  
- The bot relies on **image matching**, so images in `Automacao/img` must match your game screen resolution.  
- Adjust `confidence` values in the code if detection is not accurate.  

---

## 📜 License  
This project is licensed under the **MIT License** – feel free to use and modify.  

---

## 🤝 Contributing  
Contributions are welcome!  
- Fork this repo  
- Create a branch (`feature/new-detection`)  
- Commit your changes  
- Open a Pull Request  

---

Made with ❤️ using Python, PyAutoGUI & OpenCV.
