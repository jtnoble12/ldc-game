import streamlit as st

st.title("🕹️ The Adaptive Leader: An LDC Leadership Game")

st.write("Welcome, leader! You're facing a disruptive challenge. Can you navigate the fog and make the right choices?")

# Game Introduction
st.write("🚀 **Scenario:** You are the CEO of FutureTech Inc. AI startups are disrupting your industry, and employees fear layoffs.")
st.write("📢 The Board demands an AI strategy. Your employees resist automation. What do you do?")

# First Choice
option1 = st.radio("Choose your strategy:", 
                   ["1️⃣ Act Fast: Implement AI company-wide immediately.", 
                    "2️⃣ Slow Down: Run small AI pilot projects.", 
                    "3️⃣ Avoid: Wait for market clarity before deciding."])

if option1 == "1️⃣ Act Fast: Implement AI company-wide immediately.":
    st.write("⚠️ **Your employees revolt!** They feel blindsided. Productivity drops. Morale declines.")
    st.write("📉 Your decision **hurt employee trust**, but it positioned FutureTech ahead in AI adoption.")
elif option1 == "2️⃣ Slow Down: Run small AI pilot projects.":
    st.write("✅ **Smart move!** You launch small pilots to test AI in customer service and logistics.")
    st.write("📈 Employees **see value in AI and start engaging**. The Board is pleased but expects faster action.")
elif option1 == "3️⃣ Avoid: Wait for market clarity before deciding.":
    st.write("😬 **Risky!** AI startups are taking market share while you wait.")
    st.write("📉 **Stock price falls** as investors lose confidence. Your employees feel uncertain about the future.")

# Second Choice (if AI Pilots were chosen)
if option1 == "2️⃣ Slow Down: Run small AI pilot projects.":
    option2 = st.radio("🔍 Employees are still nervous. What’s your next step?", 
                       ["A) Offer AI Training to Upskill Employees", 
                        "B) Lay off Non-Tech Employees to Cut Costs", 
                        "C) Pause AI Expansion to Gather More Data"])
    
    if option2 == "A) Offer AI Training to Upskill Employees":
        st.write("🎉 **Great choice!** Employees feel valued. AI adoption speeds up. The company thrives!")
    elif option2 == "B) Lay off Non-Tech Employees to Cut Costs":
        st.write("⚠️ **Backlash!** Employees strike, media criticizes you. Your reputation takes a hit.")
    elif option2 == "C) Pause AI Expansion to Gather More Data":
        st.write("🤔 **Neutral Choice.** The Board is impatient, but employees appreciate the careful approach.")

# Final Outcome
st.write("📊 **Your Leadership Score:** Based on your choices, you've led with either innovation, stability, or resistance. No path is perfect!")

st.write("💡 **Key Takeaway:** Leading disruptive change requires balancing employee trust, speed, and adaptability.")

st.write("🔄 **Play again? Refresh the page!**")
