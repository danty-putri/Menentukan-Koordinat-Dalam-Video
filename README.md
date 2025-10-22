# 🎥 Get Pixel Coordinates from Video with OpenCV

This project allows you to **click on points in a video** to retrieve their **(x, y)** pixel coordinates using the **OpenCV** library.
Each clicked point is connected by a line, forming a path that updates dynamically while the video plays.

---

## 🚀 Features

* Display video frames in real time.
* Click on any point to get its pixel coordinates.
* Automatically shows coordinates `(X, Y)` beside each clicked point.
* Draws lines connecting consecutive points.
* Resizable video window.
* Press **‘q’** to quit.

---

## 🧩 Requirements

Make sure you have Python 3.x installed, then install dependencies:

```bash
pip install opencv-python
```

---

## 💻 How to Run

1. Clone or download this repository.
2. Place your video file (e.g., `pos.mp4`) in the same folder as the script.
3. Run the script:

   ```bash
   python get_coordinates.py
   ```
4. A window will appear:

   * **Left click** anywhere in the video → prints pixel coordinates in terminal and displays them on video.
   * **Press ‘q’** → to exit the program.

---

## 🧠 Example Output

```
Koordinat Pixel: X=350, Y=220
Koordinat Pixel: X=560, Y=270
Koordinat Pixel: X=780, Y=300
```

The clicked points will appear as **green circles** connected by **green lines**, with their coordinates displayed beside them.

---

## 📂 Project Structure

```
📦 get-pixel-coordinates-video
 ┣ 📜 get_coordinates.py
 ┣ 📜 README.md
 ┗ 🎞️ pos.mp4
```

---

## 🖼️ Preview

You can display an example result in your README using:

```markdown
![Preview](https://github.com/username/get-pixel-coordinates-video/blob/main/example_output.jpg)
```

---

## 📋 Notes

* You can modify the variable `video_path` in the script to use a different video file.
* Works for `.mp4`, `.avi`, `.mov`, and other common video formats supported by OpenCV.

---

## 🧑‍💻 Author

Created by **Putri** — for interactive pixel coordinate visualization using OpenCV.
