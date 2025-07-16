# 🤖 Line Detector Bot – Tread-o-Quest Challenge

Welcome to our Arduino-based **Line Detector Bot**, built for the thrilling robotics competition **Tread-o-Quest (TOQ)** — where bots race against time through a tricky maze filled with black-and-white lines, sharp turns, and steep ramps.

This was a fun and intense project that I built with my teammate **Souvik**, and it taught us a lot about embedded systems, problem-solving under pressure, and teamwork. Huge thanks to our mentor **Ansuman Patro** for always being there to guide us.

---

## 📸 Our Bot

![Our Bot](OurBOT.jpg)

---

## 🧩 The Challenge Track

![Track and Problem Statement](TRACK_and_Problem_Statement.jpg)

We were given a maze-like track with:
- **Black and white lines** for navigation,
- **Intersections and forks** requiring decision-making,
- **Inclined ramps** that tested the bot’s control and grip,
- And a **timer**, pushing us to be both fast and accurate.

The goal? Build a bot that can detect and follow lines automatically, handle obstacles smartly, and finish the track as fast as possible.

---

## 🛠️ What’s Inside

We kept things simple and focused:
- **Sensors**: IR sensor array for detecting black/white paths.
- **Brains**: Arduino Uno running all logic in `main.ino`.
- **Movement**: DC motors with L298N motor driver for control.
- **Chassis**: Lightweight acrylic frame + castor wheel.
- **Power**: Rechargeable battery pack.

---

## 🧠 How It Worked

1. **Line Sensing**  
   Calibrated our IR sensor array to pick up black vs white surfaces reliably under different lighting.

2. **Bot Design & Building**  
   Focused on making it light but stable, especially for slopes and tight turns.

3. **Control Logic (main.ino)**  
   - Simple logic + tweaks for smoother cornering.
   - Speed adjustments on ramps.
   - Recovery if the bot went off-track.

4. **Testing & Iteration**  
   Built a DIY version of the track at home and kept refining things — we had plenty of “oops” moments, especially syncing motor speed with what sensors saw!

---

## 💬 What We Learned

- Getting **hardware and code to play nice** takes time and patience.
- Fine-tuning sensors is critical — small calibration issues can make your bot misbehave badly.
- Working together and dividing roles helped us move fast and stay motivated.
- Real-world robotics is nothing like simulations — there’s a lot of debugging on your knees 😄.

---

## 🙏 Shoutout

Big thanks to **Ansuman Patro** for his mentorship. And of course, to my teammate **Souvik** — wouldn’t have been half as fun doing this solo.

---

## 🗂️ Project Files

Here’s what’s in this repo:

