---
title: Movie Env
emoji: 🎬
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# 🎬 Movie Recommendation OpenEnv

## 📌 Description
This environment simulates a real-world movie recommendation system where an AI agent interacts with a user and suggests movies based on preferences.

## 🎯 Objective
Train an AI agent to:
- Understand user preferences
- Ask clarifying questions
- Recommend relevant movies

## ⚙️ Environment API

### reset()
Returns initial user profile

### step(action)
Takes action:
- ask → ask user preference
- recommend → suggest movie

Returns:
- observation
- reward (0.0 – 1.3)
- done

### state()
Returns current environment state

---

## 📊 Tasks

### Easy
User likes action movies  
Target: Avengers, Mad Max  

### Medium
User likes romantic drama  
Target: Titanic, The Notebook  

### Hard
User likes philosophical sci-fi  
Target: Interstellar, Blade Runner 2049  

---

## 🎯 Reward Design

- +1.0 → correct recommendation  
- +0.3 → bonus for perfect match  
- +0.2 → asking questions  
- -0.2 → repeated actions  

---

## ▶️ Run Instructions

```bash
python inference.py
