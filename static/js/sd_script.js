// ユーザ登録
document.getElementById('registerUser').addEventListener('click', () => {
    const username = document.getElementById('username').value;
    if (!username) {
        alert('ユーザ名を入力してください！');
        return;
    }
    fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username })
    }).then(response => response.json())
      .then(data => alert(data.message))
      .catch(error => console.error('Error:', error));
 });
 // スケジュール登録
 document.getElementById('addSchedule').addEventListener('click', () => {
    const title = document.getElementById('scheduleTitle').value;
    const date = document.getElementById('scheduleDate').value;
    if (!title || !date) {
        alert('タイトルと日付を入力してください！');
        return;
    }
    fetch('/add-schedule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, date })
    }).then(response => response.json())
      .then(data => alert(data.message))
      .catch(error => console.error('Error:', error));
 });
 // スケジュール一覧の取得
 function fetchSchedules() {
    fetch('/schedules')
        .then(response => response.json())
        .then(data => {
            const scheduleList = document.getElementById('scheduleList');
            scheduleList.innerHTML = '';
            data.forEach(schedule => {
                const div = document.createElement('div');
                div.textContent = `${schedule.date}: ${schedule.title}`;
                scheduleList.appendChild(div);
            });
        })
        .catch(error => console.error('Error:', error));
 }
 fetchSchedules();
 // スケジュール検索
 document.getElementById('searchSchedule').addEventListener('click', () => {
    const date = document.getElementById('searchDate').value;
    fetch(`/search?date=${date}`)
        .then(response => response.json())
        .then(data => {
            const searchResults = document.getElementById('searchResults');
            searchResults.innerHTML = '';
            data.forEach(schedule => {
                const div = document.createElement('div');
                div.textContent = `${schedule.date}: ${schedule.title}`;
                searchResults.appendChild(div);
            });
        })
        .catch(error => console.error('Error:', error));
 });