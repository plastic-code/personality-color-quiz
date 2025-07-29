import streamlit as st

st.set_page_config(page_title="Personality Color Quiz", layout="centered")
st.title("🔍 Discover Your Personality Type")
st.markdown("Answer the 15 questions below to find out your dominant and secondary color — based on *Surrounded by Idiots* by Thomas Erikson.")

questions = [
    ("How do you handle unfamiliar environments?", [
        ("Jump in and take control", "Red"),
        ("Observe and stay low-key until comfortable", "Green"),
        ("Talk to people and make connections fast", "Yellow"),
        ("Assess structure and rules before acting", "Blue"),
    ]),
    ("What describes your work style best?", [
        ("Precise and detail-driven", "Blue"),
        ("Supportive and team-oriented", "Green"),
        ("Efficient and focused on goals", "Red"),
        ("Energetic and social", "Yellow"),
    ]),
    ("How do you respond when someone disagrees with you strongly?", [
        ("Stand your ground and debate", "Red"),
        ("Try to defuse tension and empathize", "Green"),
        ("Use humor or change topic to stay positive", "Yellow"),
        ("Stick to facts and logical points", "Blue"),
    ]),
    ("What motivates you the most?", [
        ("Doing things the right way and being accurate", "Blue"),
        ("Helping others and maintaining peace", "Green"),
        ("Winning, achieving, and excelling", "Red"),
        ("Having fun and being admired", "Yellow"),
    ]),
    ("What do you prioritize in your daily planning?", [
        ("Deadlines and productivity", "Red"),
        ("Flexibility to be spontaneous", "Yellow"),
        ("People’s needs and emotional balance", "Green"),
        ("Efficiency, details, and structure", "Blue"),
    ]),
    ("What do you value most in others?", [
        ("Competence and confidence", "Red"),
        ("Loyalty, empathy, and trust", "Green"),
        ("Creativity, wit, and spark", "Yellow"),
        ("Integrity and precision", "Blue"),
    ]),
    ("What’s your biggest strength?", [
        ("Taking charge and setting direction", "Red"),
        ("Being calm and making others feel safe", "Green"),
        ("Inspiring and engaging people", "Yellow"),
        ("Analyzing and planning accurately", "Blue"),
    ]),
    ("How do you feel about change?", [
        ("Exciting — I love the rush", "Yellow"),
        ("Necessary if it helps reach goals", "Red"),
        ("I need time and reassurance", "Green"),
        ("Unsettling — I prefer predictability", "Blue"),
    ]),
    ("When under pressure, you...", [
        ("Double down, focus, and dominate", "Red"),
        ("Stay silent or withdraw to avoid tension", "Green"),
        ("Crack jokes or look for fun escape", "Yellow"),
        ("Zoom in on logic and become perfectionist", "Blue"),
    ]),
    ("In group projects, you often...", [
        ("Push progress and take leadership", "Red"),
        ("Mediate conflict and keep harmony", "Green"),
        ("Entertain, motivate, and keep things light", "Yellow"),
        ("Ensure accuracy and structure", "Blue"),
    ]),
    ("Your communication style is...", [
        ("Brief, blunt, and results-driven", "Red"),
        ("Gentle, polite, and careful", "Green"),
        ("Lively, expressive, and spontaneous", "Yellow"),
        ("Thoughtful, factual, and clear", "Blue"),
    ]),
    ("What annoys you most at work?", [
        ("Slowness or indecision", "Red"),
        ("Harsh tones or arguments", "Green"),
        ("Routines and strict rules", "Yellow"),
        ("Mess, errors, or imprecision", "Blue"),
    ]),
    ("How do you behave in brainstorming sessions?", [
        ("Drive toward a goal quickly", "Red"),
        ("Support all voices and ideas", "Green"),
        ("Throw out wild, creative suggestions", "Yellow"),
        ("Structure ideas into workable formats", "Blue"),
    ]),
    ("What makes you feel most valued?", [
        ("When people recognize my ideas or creativity", "Yellow"),
        ("When my efforts make the group stronger", "Green"),
        ("When I'm trusted to get results independently", "Red"),
        ("When others rely on my accuracy or insight", "Blue"),
    ]),
    ("What role do you naturally take in a crisis?", [
        ("Jump in and take charge", "Red"),
        ("Stay calm and comfort others", "Green"),
        ("Keep energy up and look for silver lining", "Yellow"),
        ("Analyze options and create a plan", "Blue"),
    ]),
]

st.divider()

scores = {"Red": 0, "Yellow": 0, "Green": 0, "Blue": 0}
responses = {}

for i, (q_text, options) in enumerate(questions):
    st.subheader(f"Q{i+1}. {q_text}")
    choice = st.radio("", [opt[0] for opt in options], key=f"q{i}")
    for text, color in options:
        if text == choice:
            scores[color] += 1
            responses[f"Q{i+1}"] = color

if st.button("🔎 Show My Results"):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    primary = sorted_scores[0]
    secondary = sorted_scores[1] if sorted_scores[1][1] >= 0.75 * primary[1] else None

    st.markdown(f"## 🎯 Your Primary Color is: {primary[0]}")
    if secondary:
        st.markdown(f"## 🔄 Your Secondary Color is: {secondary[0]}")

    descriptions = {
        "Red": "🔥 **Red (Dominant)**: Assertive, goal-oriented, and action-driven. Thrives on results and control.",
        "Yellow": "🌟 **Yellow (Influencer)**: Energetic, expressive, social. Inspires others and values recognition.",
        "Green": "🍃 **Green (Stable)**: Loyal, calm, patient. Dislikes conflict and supports group harmony.",
        "Blue": "🔷 **Blue (Conscientious)**: Detail-oriented, analytical, and precise. Prefers structure and logic.",
    }

    st.markdown(f"\n{descriptions[primary[0]]}")
    if secondary:
        st.markdown(f"\n{descriptions[secondary[0]]}")

    st.divider()
    st.markdown("### Your Answer Breakdown:")
    for i, (q_text, _) in enumerate(questions):
        st.write(f"Q{i+1}: {responses.get(f'Q{i+1}', 'N/A')}")
