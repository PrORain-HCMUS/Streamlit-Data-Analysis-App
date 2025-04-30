import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
import os

# Lấy API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")

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
    with st.spinner("⏳ Đang xử lý..."):
        try:
            if "llama3" in model_choice or "groq" in model_choice:
                from langchain_community.llms import Groq
                groq_api_key = os.getenv("GROQ_API_KEY", "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")
                llm = Groq(model=model_choice.split()[0], api_key=groq_api_key, temperature=0)
            else:
                llm = ChatOpenAI(
                    temperature=0,
                    model_name=model_choice,
                    openai_api_key=os.getenv("OPENAI_API_KEY", "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")
                )

            agent = create_pandas_dataframe_agent(
                llm, df, verbose=True, allow_dangerous_code=True
            )
            result = agent.run(prompt)
            st.success("✅ Đã xử lý xong:")
            st.markdown(result)

            st.subheader("📊 Tự động thống kê & biểu đồ")
            for col in df.columns:
                with st.expander(f"📌 Cột: `{col}`"):
                    st.write("**Loại dữ liệu:**", str(df[col].dtype))
                    st.write("**Giá trị thiếu:**", df[col].isnull().sum())
                    st.write("**Giá trị duy nhất:**", df[col].nunique())

                    if pd.api.types.is_numeric_dtype(df[col]):
                        st.write("**Thống kê số:**")
                        st.write(df[col].describe())
                        fig, ax = plt.subplots()
                        sns.histplot(df[col].dropna(), bins=30, kde=True, ax=ax)
                        ax.set_title(f"Histogram of {col}")
                        st.pyplot(fig)
                    else:
                        value_counts = df[col].astype(str).value_counts().head(20)
                        st.write("**Top 20 giá trị phổ biến:**")
                        st.write(value_counts)
                        fig, ax = plt.subplots()
                        value_counts.plot(kind="bar", ax=ax, color="skyblue")
                        ax.set_title(f"Bar Chart of {col} (Top 20)")
                        st.pyplot(fig)
        except Exception as e:
            st.error(f"❌ Lỗi: {e}")

st.set_page_config(layout="wide")
st.title("🫠 AI Data Agent (LangChain + Streamlit)")

model_choice = st.selectbox("🤖 Chọn mô hình AI", ["gpt-3.5-turbo", "gpt-4", "llama3-8b (groq)"])

uploaded_file = st.file_uploader("📂 Upload file CSV", type="csv")
if uploaded_file:
    encoding = st.selectbox("Chọn encoding", ["utf-8", "latin1", "utf-16"], index=0)
    df = pd.read_csv(uploaded_file, encoding=encoding)
    st.subheader("📋 Xem nhanh dữ liệu (100 dòng)")
    st.dataframe(df.head(100), use_container_width=True)

    user_prompt = st.text_area("💬 Gửi yêu cầu cho AI Agent", height=150)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Gửi yêu cầu"):
            if user_prompt.strip():
                run_ai_agent(user_prompt, df, model_choice)
            else:
                st.warning("⚠️ Vui lòng nhập yêu cầu.")

    with col2:
        if st.button("🧹 Clean & Analyze tự động"):
            run_ai_agent(default_clean_analyze_prompt, df, model_choice)
