
import streamlit as st
import pandas as pd

st.title("WORK TALK 위험성평가 엑셀 자동 통합 프로그램")

st.write("📂 폴더 안에 있는 여러 엑셀 파일을 하나로 통합합니다.")
st.write("✅ 파일명은 '위험성평가_이름_날짜.xlsx' 형태를 추천합니다.")
st.write("---")

uploaded_files = st.file_uploader("엑셀 파일 여러개 업로드하기", accept_multiple_files=True, type=["xlsx"])

if uploaded_files:
    dfs = []
    for uploaded_file in uploaded_files:
        df = pd.read_excel(uploaded_file)
        df['파일명'] = uploaded_file.name  # 파일명 추가해서 누가 작성했는지 표시
        dfs.append(df)
    
    if dfs:
        merged_df = pd.concat(dfs, ignore_index=True)
        st.success("✅ 통합이 완료되었습니다!")

        @st.cache_data
        def convert_df(df):
            return df.to_excel(index=False, engine='openpyxl')

        merged_file = convert_df(merged_df)

        st.download_button(
            label="📥 통합된 엑셀파일 다운로드 (위험성평가_통합본.xlsx)",
            data=merged_file,
            file_name='위험성평가_통합본.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
