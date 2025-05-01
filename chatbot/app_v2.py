import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html
import os

# API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")

# Prompt mặc định để clean & analyze
default_clean_analyze_prompt = """
Bạn hãy làm sạch và phân tích dữ liệu CSV này theo các bước sau. Trình bày kết quả bằng tiếng Việt, rõ ràng và ngắn gọn, phù hợp hiển thị Streamlit:

1. Phát hiện các cột có giá trị thiếu (null). 
   - Số: điền mean.  
   - Text: điền mode. 
   - Ghi rõ đã xử lý cột nào.

2. Xoá những dòng trống toàn bộ.

3. Chuẩn hoá kiểu dữ liệu: datetime, float/int.

4. Phân tích dữ liệu: 
   - Số: mean, median, std, min, max
   - Phân loại: Top 5 giá trị

5. Tóm tắt toàn bộ các bước trên.
"""

def run_ai_agent(prompt, df, model_choice):
    with st.spinner("Đang xử lý..."):
        try:
            if "mistral" in model_choice.lower():
                from langchain_community.llms import Ollama
                llm = Ollama(model="mistral")
                result = llm.invoke(prompt)
                st.markdown(result)
                return
            else:
                llm = ChatOpenAI(
                    temperature=0,
                    model_name=model_choice,
                    openai_api_key=OPENAI_API_KEY
                )

            agent = create_pandas_dataframe_agent(
                llm,
                df,
                verbose=True,
                handle_parsing_errors=True,
                allow_dangerous_code=True,
                max_iterations=30,
                max_execution_time=300
            )
            result = agent.run(prompt)
            st.success("✅ Đã xử lý xong:")
            st.markdown(result)
        except Exception as e:
            st.error(f"❌ Lỗi: {e}")

st.set_page_config(layout="wide")
st.title("AI Data Agent + PyGWalker")

model_choice = st.selectbox("Chọn mô hình AI", ["gpt-3.5-turbo", "gpt-4", "mistral (ollama)"])

uploaded_file = st.file_uploader("Tải lên file CSV", type="csv")
if uploaded_file:
    encoding = st.selectbox("Chọn encoding", ["utf-8", "latin1", "utf-16"], index=0)
    df = pd.read_csv(uploaded_file, encoding=encoding)
    st.write("📦 Dataset có kích thước:", df.shape)

    # Phân tích trực quan tương tác
    st.subheader("📊 Phân tích tương tác với PyGWalker")
    init_streamlit_comm()
    pyg_html = get_streamlit_html(df, use_kernel_calc=True)
    st.components.v1.html(pyg_html, height=800, scrolling=True)

    # Yêu cầu AI phân tích dữ liệu
    st.subheader("🤖 Hỏi AI về dữ liệu")
    user_prompt = st.text_area("Gửi yêu cầu cho AI Agent", height=150)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Gửi yêu cầu"):
            if user_prompt.strip():
                run_ai_agent(user_prompt, df, model_choice)
            else:
                st.warning("⚠️ Vui lòng nhập yêu cầu.")

    with col2:
        if st.button("Clean & Analyze tự động"):
            run_ai_agent(default_clean_analyze_prompt, df, model_choice)
