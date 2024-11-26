const express = require('express');

const fs = require('fs');

const app = express();

const PORT = 3000;

app.use(express.json());

app.use(express.static('frontend'));

let schedules = [];

let users = [];

// ユーザ登録

app.post('/register', (req, res) => {

    const { username } = req.body;

    if (!username) return res.status(400).json({ message: 'ユーザ名が必要です。' });

    users.push(username);

    res.json({ message: 'ユーザ登録が完了しました！' });

});

// スケジュール登録

app.post('/add-schedule', (req, res) => {

    const { title, date } = req.body;

    if (!title || !date) return res.status(400).json({ message: 'タイトルと日付が必要です。' });

    schedules.push({ title, date });

    res.json({ message: 'スケジュールが登録されました！' });

});

// スケジュール一覧

app.get('/schedules', (req, res) => {

    res.json(schedules);

});

// 特定の日のスケジュール検索

app.get('/search', (req, res) => {

    const { date } = req.query;

    const results = schedules.filter(schedule => schedule.date === date);

    res.json(results);

});

app.listen(PORT, () => {

    console.log(`Server is running on http://localhost:${PORT}`);

}); 