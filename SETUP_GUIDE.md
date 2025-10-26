# GM League Season 2 - Live Scores Setup Guide

## 📋 Complete Setup Instructions for New Laptop

### Step 1: Install Python
1. Download Python 3.7 or higher from: https://www.python.org/downloads/
2. During installation, **CHECK the box** "Add Python to PATH"
3. Verify installation by opening Command Prompt and typing:
   ```
   python --version
   ```

### Step 2: Transfer Project Files
1. Copy the entire project folder to the new laptop
2. Place it in a location like: `C:\GM-League-Season-2\`

### Step 3: Open Project Location
1. Open Command Prompt (cmd) or PowerShell
2. Navigate to the project folder:
   ```
   cd C:\GM-League-Season-2\GM-League-Season-2-Live-Scores-main
   ```

### Step 4: Install Requirements
Run this command to install all required packages:
```
pip install -r requirements.txt
```

This will install:
- Flask (Web Framework)
- Flask-SQLAlchemy (Database)
- Flask-Login (Authentication)
- Flask-SocketIO (Real-time updates)
- Eventlet (WebSocket support)

### Step 5: Run the Application
Start the server with:
```
python app.py
```

You should see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### Step 6: Access the Application
Open your browser and go to:
- **Main Page**: http://localhost:5000
- **Admin Login**: http://localhost:5000/login
- **Leaderboard**: http://localhost:5000/leaderboard

## 🔐 Admin Login Credentials

You have 6 admin accounts (all can work simultaneously):

| Username | Password |
|----------|----------|
| yashaswini | yashu@1704 |
| admin1 | admin@123 |
| admin2 | admin@123 |
| admin3 | admin@123 |
| admin4 | admin@123 |
| admin5 | admin@123 |

## 📱 Features Overview

### For All Users:
- ✅ View live scores for 4 sports (Football, Kabaddi, Basketball, Badminton)
- ✅ See all players and their statistics
- ✅ View team totals (points & goals)
- ✅ Filter players by sport
- ✅ Real-time score updates
- ✅ Mobile responsive design
- ✅ Separate leaderboard page

### For Admins (Login Required):
- ✅ Add/Edit/Delete players
- ✅ Click "+1 Point" to add points during matches
- ✅ Manage live scores
- ✅ Update team information
- ✅ View player statistics
- ✅ Multiple admins can work simultaneously

## 🎯 How to Use

### Adding Players (Before Match):
1. Login to Admin Dashboard
2. Go to "Player & Team Management" section
3. Fill in:
   - Sport: Select sport (Football/Kabaddi/Basketball/Badminton)
   - Team Name: Enter team name
   - Player Name: Enter player name
4. Click "Add Player"
5. Repeat for all players

### Managing Scores (During Match):
1. Find the player in the admin dashboard
2. Click "+1 Point" button to add points
3. Points and goals update automatically
4. Team totals are calculated automatically
5. All viewers see updates in real-time

### Viewing Scores (Public):
1. Open http://localhost:5000
2. View live scores at the top
3. Scroll down to see players and teams
4. Filter by sport if needed
5. Click "Leaderboard" to view rankings

## 🚀 Project Structure

```
GM-League-Season-2-Live-Scores-main/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── config.py              # Configuration
├── requirements.txt       # Python dependencies
├── leaderboard.json       # Leaderboard data
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── admin.html        # Admin dashboard
│   ├── leaderboard.html  # Leaderboard page
│   └── login.html        # Login page
└── SETUP_GUIDE.md        # This file
```

## 🛠️ Troubleshooting

### Issue: Port 5000 already in use
**Solution**: Kill the process using port 5000:
```
netstat -ano | findstr :5000
taskkill /PID <process_id> /F
```

Or change the port in `app.py` (last line):
```python
socketio.run(app, debug=True, port=5001)
```

### Issue: Module not found
**Solution**: Install requirements again:
```
pip install -r requirements.txt
```

### Issue: Database errors
**Solution**: Delete `gmu_score.db` and restart the app:
```
del gmu_score.db
python app.py
```

### Issue: Can't login
**Solution**: Make sure you're using correct credentials (see Admin Login Credentials above)

## 🌐 Network Access (Optional)

To access from other devices on the same network:

1. Find your IP address:
   ```
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., 192.168.1.100)

2. Update `app.py` last line to:
   ```python
   socketio.run(app, debug=True, host='0.0.0.0')
   ```

3. Access from other devices:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```

## 📊 Database

The application uses SQLite database (`gmu_score.db`):
- Created automatically on first run
- Stores users, scores, and players
- No separate database server needed

## 🔒 Security Notes

- For production use, change default passwords
- Implement SSL/HTTPS
- Use environment variables for secrets
- Consider using PostgreSQL instead of SQLite for production

## 📞 Support

If you encounter any issues:
1. Check that Python is installed correctly
2. Verify all requirements are installed
3. Make sure port 5000 is not in use
4. Check the console for error messages
5. Ensure you're in the correct directory when running commands

---

**Built with ❤️ for GM League Season 2**

