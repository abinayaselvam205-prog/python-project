import streamlit as st 
import threading 
import time 
import random 
 
st.set_page_config(page_title="Hospital Monitoring System", 
layout="centered") 
st.title("Real-Time Hospital Monitoring System (Multithreading Demo)") 
st.write("This demo simulates multiple hospital tasks running concurrently using Python threads.") 

 
# ---------- Placeholders for real-time updates ---------- 
sensor_placeholder = st.empty() 
notification_placeholder = st.empty() 
log_placeholder = st.empty() 
progress_placeholder = st.progress(0) 
 
# ---------- Function 1: Reading patient sensor data ---------- 
def read_sensor_data(): 
    for i in range(5): 
        heart_rate = random.randint(60, 120) 
        temperature = round(random.uniform(36.5, 39.0), 1) 
        sensor_placeholder.markdown( f"**Sensor Reading {i+1}:** Heart Rate = `{heart_rate}` bpm | Temp = `{temperature}°C`" )
        time.sleep(2) 
 
# ---------- Function 2: Sending doctor notifications ---------- 
def notify_doctor(): 
    for i in range(3): 
        notification_placeholder.markdown( f"**Doctor Notification {i+1}:** Patient report sent to duty doctor." )
        time.sleep(3) 
 
# ---------- Function 3: Logging data ---------- 
def log_data(): 
    for i in range(4): 
        log_placeholder.markdown(f"**Log Entry {i+1}:** Data saved to Temp = `{temperature}°C`" )
        time.sleep(2.5) 
 
# ---------- Function to run all threads ---------- 
def run_monitoring_system(): 
    t1 = threading.Thread(target=read_sensor_data) 
    t2 = threading.Thread(target=notify_doctor) 
    t3 = threading.Thread(target=log_data) 
 
    t1.start() 
    t2.start() 
    t3.start() 
 
    total_duration = 10 
    for i in range(total_duration): 
        progress_placeholder.progress((i + 1) / total_duration) 
        time.sleep(1) 
 
    t1.join() 
    t2.join() 
    t3.join() 
 
    st.success("All monitoring tasks completed successfully!") 
 
# ---------- Streamlit Button to Start ---------- 
if st.button("Start Hospital Monitoring"): 
    st.info("Monitoring started... Please wait while tasks run in parallel.") 
    run_monitoring_system() 
 
