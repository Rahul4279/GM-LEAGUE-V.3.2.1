# GM League Season 2 - Live Scores

A real-time sports score tracking website built with Flask, SocketIO, and modern web technologies. This application allows multiple administrators to update live scores for multiple sports events simultaneously, which are instantly broadcast to all connected viewers.

## 🏆 Key Features

### For Viewers
- ✅ **Real-time Score Updates**: Live score updates without page refresh
- ✅ **Beautiful Modern UI**: Responsive design with smooth animations
- ✅ **Multiple Sports**: Football, Kabaddi, Basketball, and Badminton
- ✅ **Player Management**: View all players with their statistics
- ✅ **Team Statistics**: See team totals (points & goals)
- ✅ **Leaderboard**: Separate page with rankings
- ✅ **Mobile Responsive**: Perfect on phones, tablets, and desktops

### For Administrators
- ✅ **Multiple Admins**: 6 admin accounts can work simultaneously
- ✅ **Player Management**: Add/Edit/Delete players with ease
- ✅ **Quick Point Entry**: Click "+1" to add points during matches
- ✅ **Real-time Updates**: Changes broadcast instantly to all viewers
- ✅ **Sport Filtering**: Filter players by sport
- ✅ **Secure Login**: Password-protected admin panel
- ✅ **Team Auto-Calculation**: Team totals update automatically

## 🚀 Quick Start Guide

### Installation (New Laptop)

1. **Install Python 3.7+** from https://www.python.org/downloads/
   - ✅ Check "Add Python to PATH" during installation

2. **Copy project files** to your laptop

3. **Open Command Prompt** and navigate to project:
   ```
   cd path\to\GM-League-Season-2-Live-Scores-main
   ```

4. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```
   python app.py
   ```

6. **Access the website**:
   - Main Page: http://localhost:5000
   - Admin Login: http://localhost:5000/login
   - Leaderboard: http://localhost:5000/leaderboard

## 🔐 Admin Credentials

| Username | Password | Use Case |
|----------|----------|----------|
| yashaswini | yashu@1704 | Primary admin |
| admin1 | admin@123 | Admin 1 |
| admin2 | admin@123 | Admin 2 |
| admin3 | admin@123 | Admin 3 |
| admin4 | admin@123 | Admin 4 |
| admin5 | admin@123 | Admin 5 |

**All 6 accounts can be logged in simultaneously!**

## 📱 How to Use

### Adding Players (Before Match):
1. Login to Admin Dashboard (use any admin account)
2. Scroll to "Player & Team Management"
3. Fill in: Sport, Team Name, Player Name
4. Click "Add Player"
5. Repeat for all players

### Managing Scores (During Match):
1. Find the player in the team cards
2. Click **"+1 Point"** button
3. Points and goals update automatically
4. Team totals update automatically
5. All viewers see changes instantly

### Public View:
1. Open http://localhost:5000
2. View live match scores at top
3. Scroll to see players and teams
4. Filter by sport using dropdown
5. Click "Leaderboard" for rankings

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Real-time**: Flask-SocketIO + Eventlet
- **Authentication**: Flask-Login
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome

## 📂 Project Structure

```
GM-League-Season-2-Live-Scores-main/
├── app.py                 # Main Flask application
├── models.py              # Database models (User, Score, Player)
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── leaderboard.json       # Leaderboard data
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page (live scores + players)
│   ├── admin.html        # Admin dashboard
│   ├── leaderboard.html  # Leaderboard page
│   └── login.html        # Login page
├── .gitignore           # Git ignore file
├── README.md            # This file
└── SETUP_GUIDE.md       # Detailed setup instructions
```

## 🐛 Troubleshooting

**Port 5000 already in use?**
```bash
netstat -ano | findstr :5000
taskkill /PID <process_id> /F
```

**Module not found?**
```bash
pip install -r requirements.txt
```

**Database errors?**
Delete `gmu_score.db` and restart the app

## 🌐 Network Access

To access from other devices on same network:

1. Change last line in `app.py`:
   ```python
   socketio.run(app, debug=True, host='0.0.0.0')
   ```

2. Find your IP: `ipconfig`
3. Access from other devices: `http://YOUR_IP:5000`

## 📊 Features Breakdown

### Player Management
- Add players with team and sport
- Edit player names, points, and goals
- Delete players
- Filter by sport
- View player statistics

### Score Management
- Update live match scores
- Toggle live/off status
- Delete scores
- Real-time broadcasting

### Team Statistics
- Auto-calculate team totals
- View team points and goals
- Multiple matches simultaneously
- Real-time updates

## 🔒 Security Notes

- For production: Change default passwords
- Implement SSL/HTTPS
- Use environment variables for secrets
- Consider PostgreSQL for production

## 📞 Support

Check `SETUP_GUIDE.md` for detailed setup instructions and troubleshooting.

---

**Built with ❤️ for GM League Season 2**
**Version 2.0 - Multiple Admin Support**
