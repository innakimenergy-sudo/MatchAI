import streamlit as st
import os
import json
st.set_page_config(
    page_title="MatchAI",
    page_icon="🤖",
    layout="wide"
)
st.title("🎯 MatchAI Model Deployment")
st.markdown("**Developer**: innakimenergy-sudo | **Email**: inna.kim.energy@gmail.com")
with st.sidebar:
    st.header("📁 Model Files")
    
files = os.listdir(".")
for file in sorted(files):
        if os.path.isfile(file):
            size = os.path.getsize(file)
            size_mb = size / (1024 * 1024)
            icon = "🔶" if "model.safetensors" in file else "📄"
            st.write(f"{icon} {file}: {size_mb:.1f} MB")
    
st.divider()
st.info("**Large File Handling**: model.safetensors uses Git LFS")
tab1, tab2, tab3 = st.tabs(["Model", "Config", "Deployment"])

with tab1:
    st.header("AI Model Information")
    
    # Check for model file
    if os.path.exists("model.safetensors"):
        st.success("✅ Large model file found: model.safetensors")
        size = os.path.getsize("model.safetensors") / (1024 * 1024)
        st.metric("File Size", f"{size:.1f} MB")
    else:
        st.error("❌ model.safetensors not found!")
    if os.path.exists("config.json"):
        st.success("✅ Config file found")
        with open("config.json", "r") as f:
            config = json.load(f)
        st.json(config)
    else:
        st.warning("⚠️ config.json not found")

with tab2:
    st.header("Configuration")
json_files = [f for f in os.listdir(".") if f.endswith(".json")]
    
for json_file in json_files:
        with st.expander(f"📄 {json_file}"):
            try:
                with open(json_file, "r") as f:
                    data = json.load(f)
                st.json(data)
            except:
                st.text(open(json_file, "r").read())

with tab3:
    st.header("Deployment Status")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("GitHub")
        st.markdown("[innakimenergy-sudo/MatchAI](https://github.com/innakimenergy-sudo/MatchAI)")
        st.success("Ready for upload")
    
    with col2:
        st.subheader("Streamlit Cloud")
        st.markdown("[Deploy Now](https://streamlit.io/cloud)")
        st.info("Will deploy after GitHub push")
    
    with col3:
        st.subheader("Requirements")
        if os.path.exists("requirements.txt"):
            st.success("✅ requirements.txt found")
            st.code(open("requirements.txt").read())
        else:
            st.warning("⚠️ Create requirements.txt")
    
  st.divider()
    st.subheader("📋 Next Steps")
    st.markdown("""
    1. **Push to GitHub** with Git LFS
    2. **Deploy on Streamlit Cloud**
    3. **Share your model links**
    """)
st.divider()
st.caption("MatchAI Deployment | Large File Support via Git LFS | Windows")
