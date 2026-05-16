export async function renderTeacher(app) {
  app.innerHTML = `
    <div class="container page">
      <div class="page-header">
        <h1 class="page-title">Hiểu về Thầy 👨‍🏫</h1>
        <p class="page-subtitle">Dạy bằng TÂM — Dẫn lối bằng TRI THỨC — Đồng hành bằng CÂU CHUYỆN THẬT</p>
      </div>

      <div class="teacher-grid">
        <!-- Cột trái: Hình ảnh & Thông tin nhanh -->
        <div class="teacher-image-col">
          <div class="teacher-portrait-wrap">
            <img id="teacher-img" src="/images/teacher.webp" alt="ThS. Phó Hải Đăng" class="teacher-portrait">
          </div>
          
          <div class="teacher-info-box">
            <h3 style="margin-bottom: 0.5rem">ThS. Phó Hải Đăng</h3>
            <p style="color: var(--accent); font-size: 0.9rem; font-weight: 600; margin-bottom: 1rem">Giảng viên chính</p>
            
            <div class="teacher-contact">
              <div class="teacher-contact-item">
                <div class="teacher-contact-icon">💼</div>
                <span>Khoa học máy tính, QTKD, TMĐT</span>
              </div>
              <div class="teacher-contact-item">
                <div class="teacher-contact-icon">📱</div>
                <span>0982360370 (Zalo)</span>
              </div>
              <div class="teacher-contact-item">
                <div class="teacher-contact-icon">🌐</div>
                <a href="https://facebook.com/phohaidang" target="_blank">fb.com/phohaidang</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Cột phải: Triết lý & Phương pháp -->
        <div class="teacher-content-col">
          <div class="teacher-philosophy-card">
            <div class="philosophy-title">✨ Triết lý giáo dục</div>
            <p class="philosophy-text">
              <strong>"Dạy bằng TÂM — Dẫn lối bằng TRI THỨC — Đồng hành bằng CÂU CHUYỆN THẬT"</strong>. Đối với tôi, vai trò của một người thầy không chỉ dừng lại ở việc truyền thụ kiến thức, mà là dùng cái tâm để khơi gợi niềm đam mê, dùng tri thức để định hướng tương lai, và dùng câu chuyện thật từ cuộc sống để đồng hành cùng sinh viên trên mỗi bước đi.
            </p>
          </div>

          <div class="teacher-philosophy-card">
            <div class="philosophy-title">📖 Phương pháp chia sẻ</div>
            <p class="philosophy-text">
              Thầy là người chia sẻ tri thức qua <strong>trải nghiệm thực tế</strong>, qua những câu chuyện đời thực để sinh viên hấp thụ kiến thức nhanh chóng, dễ dàng. Lý thuyết chỉ có giá trị khi nó được soi sáng bởi thực tiễn.
            </p>
          </div>

          <div class="teacher-philosophy-card">
            <div class="philosophy-title">🔍 Tư duy cốt lõi</div>
            <p class="philosophy-text">
              Thầy tập trung truyền đạt các <strong>khái niệm cốt lõi</strong>. Sinh viên là người tự nghiền sâu để suy luận các ngọn ngành, ứng dụng vào bản thân. Tôi tin rằng khả năng tự học và tư duy độc lập là tài sản lớn nhất của mỗi sinh viên.
            </p>
          </div>

          <div class="teacher-philosophy-card">
            <div class="philosophy-title">💡 Bài học cuộc sống</div>
            <p class="philosophy-text">
              Thầy không chỉ truyền đạt tri thức chuyên môn mà sẽ chia sẻ những bài học sâu sắc về <strong>thái độ, về tư duy</strong> đằng sau tri thức ấy. Kiến thức có thể lỗi thời, nhưng cách làm người và tư duy đúng đắn sẽ đi cùng các em suốt cuộc đời.
            </p>
          </div>

          <div class="card card-accent" style="margin-top: 2rem">
            <h3>🤝 Lời nhắn gửi</h3>
            <p style="margin-top: 0.5rem; color: var(--text-secondary)">
              Hãy coi mỗi buổi học là một cơ hội để kết nối, thảo luận và cùng nhau phát triển. Đừng ngần ngại đặt câu hỏi và chia sẻ góc nhìn của chính mình.
            </p>
          </div>
        </div>
      </div>
    </div>
  `;

  // Image fallback logic
  const img = document.getElementById('teacher-img');
  const formats = ['webp', 'png', 'jpg', 'jpeg'];
  let currentFormatIndex = 0;

  img.onerror = () => {
    currentFormatIndex++;
    if (currentFormatIndex < formats.length) {
      img.src = `/images/teacher.${formats[currentFormatIndex]}`;
    } else {
      img.src = 'https://api.dicebear.com/7.x/avataaars/svg?seed=teacher';
      img.onerror = null;
    }
  };
}
