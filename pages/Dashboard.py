import streamlit as st
from database import db
import font
from datetime import datetime

if "db" not in st.session_state:
    st.session_state["db"] = db

# Accessing the session database
session_db = st.session_state["db"]

# Display welcome message
if session_db.get("username"):
    st.header(f"Welcome, {session_db['username']}!")
else:
    st.header("Welcome, Boss!")

if st.button("Show login details"):
    st.write("Login Details:")
    st.write(session_db)

# Recent Actions Section
st.subheader("Recent Actions")
actions = session_db.get("recent_actions", [])
if actions:
    for action in actions[-5:]:
        st.write(f"- {action['timestamp']} - {action['action']}")
else:
    st.write("No recent actions.")

st.subheader("Files Uploaded")
uploaded_files = session_db.get("uploaded_files", [])
if uploaded_files:
    for file in uploaded_files[-5:]:
        st.write(f"- {file['filename']} (Uploaded on {file['timestamp']})")
else:
    st.write("No files uploaded yet.")

st.subheader("Statistics Overview")
st.write(f"Total Records Processed: {session_db.get('total_records', 0)}")
st.write(f"Active Users: {session_db.get('active_users', 0)}")
st.write(f"Reports Generated: {session_db.get('reports_generated', 0)}")

st.subheader("System Notifications")
notifications = session_db.get("notifications", [])
if notifications:
    for notification in notifications:
        st.write(f"- {notification}")
else:
    st.write("No new notifications.")

st.subheader("User Activity Feed")
user_activities = session_db.get("user_activities", [])
if user_activities:
    for activity in user_activities[-5:]:
        st.write(f"- {activity['timestamp']} - {activity['activity']}")
else:
    st.write("No user activity recorded.")

st.subheader("Quick Actions")
col1, col2 = st.columns(2)
with col1:
    if st.button("Upload New File"):
        st.write("Redirecting to file upload page...")
with col2:
    if st.button("Generate Report"):
        st.write("Redirecting to report generation...")

st.subheader("System Health")
st.progress(80)
st.write("System Status: Operational")

st.subheader("Upcoming Tasks")
upcoming_tasks = session_db.get("upcoming_tasks", [])
if upcoming_tasks:
    for task in upcoming_tasks:
        st.write(f"- {task['task']} (Due by {task['due_date']})")
else:
    st.write("No upcoming tasks.")
