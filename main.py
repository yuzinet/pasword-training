import streamlit as st
import random
import string
import time

def generate_password(length=8):
    """ランダムなパスワードを生成する"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def main():
    st.title("パスワード入力練習")
    st.write("表示されたパスワードを正確に入力してください！")

    if 'password' not in st.session_state:
        st.session_state.password = generate_password()
        st.session_state.start_time = time.time()
        st.session_state.attempts = 0

    # パスワードを表示
    st.header("以下のパスワードを入力:")
    st.code(st.session_state.password)

    # ユーザー入力
    user_input = st.text_input("パスワードを入力:", type="password")
    show_password = st.checkbox("入力を表示")

    if show_password:
        st.write("あなたの入力:", user_input)

    if user_input:
        st.session_state.attempts += 1
        
        if user_input == st.session_state.password:
            end_time = time.time()
            time_taken = end_time - st.session_state.start_time
            st.success(f"正解！🎉\n所要時間: {time_taken:.2f}秒\n試行回数: {st.session_state.attempts}回")
            
            if st.button("次のパスワードへ"):
                st.session_state.password = generate_password()
                st.session_state.start_time = time.time()
                st.session_state.attempts = 0
                st.experimental_rerun()
        else:
            st.error("不正解です。もう一度試してください。")

    # 難易度設定
    st.sidebar.header("設定")
    password_length = st.sidebar.slider("パスワードの長さ", 4, 16, 8)
    
    if st.sidebar.button("新しいパスワードを生成"):
        st.session_state.password = generate_password(password_length)
        st.session_state.start_time = time.time()
        st.session_state.attempts = 0
        st.experimental_rerun()

if __name__ == "__main__":
    main()