import os
import random
import tweepy
from google import genai

# Lấy API Keys từ hệ thống bảo mật của GitHub
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
X_API_KEY = os.environ["X_API_KEY"]
X_API_SECRET = os.environ["X_API_SECRET"]
X_ACCESS_TOKEN = os.environ["X_ACCESS_TOKEN"]
X_ACCESS_SECRET = os.environ["X_ACCESS_SECRET"]

# Danh sách 7 username muốn tag (tự bốc ngẫu nhiên 2 người mỗi bài)
DANH_SACH_TAG = [
    "@phuonggiahn",
    "@EliasNaoki9",
    "@hocgiad",
    "@khanhhuyenday98",
    "@admvhv",
    "@Jessica_havana",
    "@minhkui01"
]

BAI_MAU = """Một ngày 30 đến 35 bài
Mỗi ngày 1K đến 1K Rep
Đánh tan mọi nghi ngờ về việc các bác bảo em đang Spam nền tảng và sẽ không được duyệt các tình yêu Việt nam 🇻🇳
Em đã làm chuột bạch thành công như lời hứa cho mọi người đây
Vì vậy nhiệm vụ của mọi người là thoải mái sáng tạo,thoải mái bình luận (Tránh comment giống nhau dễ bị đánh nhất là chào buổi sáng và buổi tối)"""

gemini_client = genai.Client(api_key=GEMINI_API_KEY)
x_client = tweepy.Client(
    consumer_key=X_API_KEY,
    consumer_secret=X_API_SECRET,
    access_token=X_ACCESS_TOKEN,
    access_token_secret=X_ACCESS_SECRET
)

def chay_tu_dong():
    nguoi_duoc_tag = random.sample(DANH_SACH_TAG, min(2, len(DANH_SACH_TAG)))
    chuoi_tag = " ".join(nguoi_duoc_tag)

    prompt = f"""
    Hãy viết lại đoạn văn bản mẫu dưới đây thành 1 phiên bản mới hoàn toàn khác biệt về câu chữ để đăng lên mạng xã hội X (Twitter).
    
    Yêu cầu bắt buộc:
    1. Giữ nguyên ý nghĩa cốt lõi: khẳng định tần suất đăng 30-35 bài/ngày và 1K rep/ngày là an toàn, đã kiểm chứng thành công (làm chuột bạch) để động viên cộng đồng Việt Nam 🇻🇳 thoải mái tương tác, sáng tạo và tránh comment trùng lặp (như chào buổi sáng/tối).
    2. Thay đổi cấu trúc câu, dùng từ ngữ tự nhiên, năng lượng tích cực, giọng văn gần gũi thực chiến. Trình bày thoáng mắt, có xuống dòng rõ ràng.
    3. Không dùng lại y nguyên câu mở đầu hay kết thúc của bài mẫu.
    4. Cuối bài viết, bắt buộc xuống dòng và gắn thẻ đúng 2 tài khoản này: {chuoi_tag}
    5. Chỉ xuất ra nội dung bài đăng hoàn chỉnh, tuyệt đối không thêm lời dẫn hay giải thích.

    Văn bản mẫu:
    "{BAI_MAU}"
    """

    response = gemini_client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
    )
    noi_dung_post = response.text.strip()
    
    # Đăng lên X
    tweet = x_client.create_tweet(text=noi_dung_post)
    print(f"Đăng thành công! ID: {tweet.data['id']}")

if __name__ == "__main__":
    chay_tu_dong()
