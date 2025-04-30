import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
import os

# Lấy API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")

def run_gpt_agent(prompt, df):
    with st.spinner("Đang xử lý với GPT..."):
        try:
            llm = ChatOpenAI(temperature=0, model_name="gpt-4", openai_api_key=OPENAI_API_KEY)
            agent = create_pandas_dataframe_agent(
                llm, df, verbose=True, allow_dangerous_code=True
            )
            result = agent.run(prompt)
            st.success("✅ GPT đã xử lý xong:")
            st.markdown(result)

            st.subheader("📊 Tự động hiển thị thống kê & biểu đồ sau phân tích")
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
            st.error(f"❌ Lỗi khi chạy agent: {e}")

# Prompt mặc định để clean & analyze
default_clean_analyze_prompt = """
Bạn hãy làm sạch và phân tích dữ liệu CSV này theo các bước sau. Trình bày kết quả bằng tiếng Việt, rõ ràng và ngắn gọn, phù hợp để hiển thị trên ứng dụng Streamlit:

1. Phát hiện các cột có giá trị thiếu (null). 
   - Nếu là số: điền bằng giá trị trung bình (mean).
   - Nếu là text: điền bằng giá trị phổ biến nhất (mode).
   - Ghi rõ đã xử lý cột nào, theo cách nào.

2. Xoá những dòng bị trống toàn bộ (nếu có).

3. Chuẩn hoá kiểu dữ liệu:
   - Nếu có cột ngày tháng, hãy chuyển về kiểu datetime.
   - Nếu cột có dữ liệu số, hãy đảm bảo ở dạng float hoặc int.
   - Ghi rõ những cột đã được đổi kiểu.

4. Phân tích dữ liệu:
   - Với mỗi cột: xác định là số hay phân loại (categorical).
   - Nếu là số: tính mean, median, min, max, std.
   - Nếu là phân loại: liệt kê 5 giá trị xuất hiện nhiều nhất.

5. Cuối cùng, tóm tắt lại toàn bộ các bước bạn đã làm và kết quả phân tích.
"""

st.set_page_config(layout="wide")
st.title("🧠 GPT Data Agent (LangChain + Streamlit)")

uploaded_file = st.file_uploader("📂 Upload file CSV", type="csv")

if uploaded_file is not None:
    encoding = st.selectbox("Chọn encoding", ["utf-8", "latin1", "iso-8859-1", "utf-16", "cp1252"], index=1)
    df = pd.read_csv(uploaded_file, encoding=encoding)

    st.subheader("📋 Dữ liệu đã tải (100 dòng đầu)")
    st.dataframe(df.head(100), use_container_width=True)

    st.subheader("💬 Gõ yêu cầu bằng tiếng Việt hoặc English")
    user_prompt = st.text_area("Ví dụ: Hãy làm sạch và phân tích dữ liệu", height=120)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚀 Gửi yêu cầu cho GPT Agent"):
            if user_prompt.strip() == "":
                st.warning("⚠️ Vui lòng nhập yêu cầu trước khi gửi.")
            else:
                run_gpt_agent(user_prompt, df)

    with col2:
        if st.button("🧹 Clean & Analyze tự động (GPT)"):
            run_gpt_agent(default_clean_analyze_prompt, df)

