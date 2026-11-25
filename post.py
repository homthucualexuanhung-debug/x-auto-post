import os
import random
import tweepy

# Lấy 4 mã API của X từ hệ thống bảo mật của GitHub
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

# 10 biến thể nội dung viết sẵn (không dùng AI nên không bao giờ quá tải)
DANH_SACH_BAI_VIET = [
    """Một ngày 30 đến 35 bài
Mỗi ngày 1K đến 1K Rep
Đánh tan mọi nghi ngờ về việc các bác bảo em đang Spam nền tảng và sẽ không được duyệt các tình yêu Việt nam 🇻🇳
Em đã làm chuột bạch thành công như lời hứa cho mọi người đây
Vì vậy nhiệm vụ của mọi người là thoải mái sáng tạo, thoải mái bình luận (Tránh comment giống nhau dễ bị đánh nhất là chào buổi sáng và buổi tối)""",

    """30 - 35 bài đăng mỗi ngày.
1.000 lượt tương tác (Rep) đều đặn mỗi ngày.
Đã tự tay kiểm chứng thực tế để anh em Việt Nam 🇻🇳 yên tâm cày cuốc mà không sợ bị đánh gậy spam hay trượt duyệt!
Cứ tự tin sáng tạo nội dung chất và đi bình luận có tâm nhé mọi người (Nhớ né mấy câu chào buổi sáng/tối rập khuôn ra kẻo thuật toán quét).""",

    """Nhiều bác vẫn lo đăng 30-35 bài với đi 1K rep mỗi ngày sẽ bị X bóp tương tác hoặc không được duyệt kiếm tiền.
Em đã trực tiếp làm chuột bạch và vượt qua ngon lành cho cộng đồng Việt Nam 🇻🇳 rồi đây!
Anh em cứ thoải mái bung sức sáng tạo, tương tác nhiệt tình lên nhé. Chỉ cần lưu ý viết bình luận đa dạng, tuyệt đối tránh copy-paste chào buổi sáng hay buổi tối là an toàn tuyệt đối.""",

    """Tổng kết thực chiến cho anh em Việt Nam 🇻🇳:
- Tần suất: 30 đến 35 bài/ngày.
- Tương tác: Chạm mốc 1K Rep/ngày.
Kết quả: Duyệt mượt mà, đập tan mọi tin đồn bị nền tảng đánh spam!
Việc của mọi người bây giờ là cứ tự do sáng tạo và đi dạo bình luận thật tự nhiên (Hạn chế comment trùng lặp kiểu GM/GN hay chào buổi sáng tối nhé).""",

    """Hứa với anh em Việt Nam 🇻🇳 là làm tới cùng, và hôm nay em đã test thành công công thức: 30-35 bài/ngày + 1K rep/ngày hoàn toàn sạch sẽ, không hề dính spam!
Mọi nghi ngờ đã được giải tỏa. Cả nhà cứ mạnh dạn lên bài, thoải mái giao lưu bình luận nhé (Mẹo nhỏ: viết comment có nội dung khác nhau, đừng spam mấy câu chào hỏi giống hệt nhau).""",

    """Đừng để nỗi sợ bị đánh spam kìm hãm anh em nữa!
Mức 30-35 post và 1K rep mỗi ngày đã được em kiểm chứng thành công 100% cho các tình yêu Việt Nam 🇻🇳.
Cứ tự tin sáng tạo nội dung mới và tương tác thật chất lượng mỗi ngày. Nhớ quy tắc vàng: bình luận tự nhiên, tránh lặp đi lặp lại mấy câu chào buổi sáng, buổi tối là ok hết.""",

    """Báo tin vui cho cộng đồng X Việt Nam 🇻🇳:
Kỷ luật 30 đến 35 bài mỗi ngày kèm 1K rep đã được em chuột bạch thành công rực rỡ, nền tảng duyệt bình thường chứ không hề bị khóa hay đánh spam như lời đồn.
Anh em cứ thoải mái sáng tạo và đi tương tác chéo nhiệt tình nhé (Lưu ý nhỏ là né comment giống nhau hàng loạt kiểu chào buổi sáng/tối ra nha).""",

    """Thực tế đã chứng minh: 30-35 bài/ngày và 1K rep/ngày hoàn toàn nằm trong vùng an toàn nếu anh em làm đúng cách.
Em đã tiên phong test thành công để các tình yêu Việt Nam 🇻🇳 vững tâm cày cuốc!
Nhiệm vụ của cả nhà là thỏa sức sáng tạo và bình luận thật tự nhiên (Tránh comment công nghiệp giống nhau như chào buổi sáng hay chúc ngủ ngon là bền vững).""",

    """Dành cho bác nào còn đang rụt rè sợ đăng nhiều bị quét spam:
Em đã đích thân thử nghiệm 30-35 bài cùng 1K rep mỗi ngày và đã được duyệt thành công cho anh em Việt Nam 🇻🇳 xem rồi đây.
Mọi người cứ tự tin lên sóng, thoải mái giao lưu bình luận nhé. Chỉ cần tránh lặp lại một mẫu câu chào buổi sáng/tối cho tất cả các bài là tài khoản khỏe re.""",

    """Cột mốc 30-35 bài viết và 1.000 rep mỗi ngày hoàn toàn khả thi và an toàn tuyệt đối!
Em đã làm chuột bạch thành công như đã hứa với cộng đồng Việt Nam 🇻🇳.
Giờ thì anh em cứ bung lụa sáng tạo, bình luận rôm rả lên nhé (Nhớ đổi mới câu chữ khi đi comment, đừng dùng mãi câu chào buổi sáng hay buổi tối kẻo dính bộ lọc spam)."""
]

x_client = tweepy.Client(
    consumer_key=X_API_KEY,
    consumer_secret=X_API_SECRET,
    access_token=X_ACCESS_TOKEN,
    access_token_secret=X_ACCESS_SECRET
)

def chay_tu_dong():
    # Chọn ngẫu nhiên 1 bài trong 10 mẫu và 2 người trong 7 người
    bai_duoc_chon = random.choice(DANH_SACH_BAI_VIET)
    nguoi_duoc_tag = random.sample(DANH_SACH_TAG, 2)
    chuoi_tag = " ".join(nguoi_duoc_tag)

    noi_dung_post = f"{bai_duoc_chon}\n\n{chuoi_tag}"

    # Đăng thẳng lên X
    tweet = x_client.create_tweet(text=noi_dung_post)
    print(f"Đăng thành công! ID: {tweet.data['id']}")

if __name__ == "__main__":
    chay_tu_dong()
