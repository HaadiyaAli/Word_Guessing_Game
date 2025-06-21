# 🎯 Word Guessing Game

A fun terminal-based word guessing game built with Python. Players try to guess a randomly selected word, one letter at a time — but instead of choosing from a local list, this version fetches fresh words using the [API Ninjas Random Word API](https://api-ninjas.com/api/randomword)!

---

## 🚀 Features

- Random word fetched live from the internet via API
- Case-insensitive letter matching
- User-friendly messages and validation for empty input
- Automatically handles spaces in multi-word phrases
- Dynamic attempt counter based on word length

---

## 🧠 How It Works

1. A word is retrieved from the Random Word API.
2. The player sees a series of underscores representing the word.
3. They guess letters until they either complete the word or run out of attempts.
4. Correct guesses reveal the matching letters. Wrong guesses reduce attempts.

---
To try yourself you must create an account with API Ninjas and insert your own API
