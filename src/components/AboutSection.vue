<template>
  <section id="about" class="section about">
    <div class="container about-grid">
      <div>
        <h2 class="section-title">Về chúng tôi</h2>
        <p class="section-subtitle">
          CÔNG TY TNHH TƯ VẤN KHẢO SÁT VÀ THIẾT KẾ XÂY DỰNG KHÁNH LY
        </p>
        <div class="company-info">
          <p><strong>Người đại diện:</strong> Ông Đàm Trọng Xuân Anh</p>
          <p><strong>Chức vụ:</strong> Phó giám đốc</p>
          <p><strong>Mã số thuế:</strong> 3701616836</p>
        </div>
      </div>

      <div class="about-card">
        <p>
          Công ty chúng tôi chuyên cung cấp dịch vụ tư vấn, khảo sát, thiết kế, thẩm tra và giám sát thi công 
          cho các dự án dân dụng, công nghiệp, giao thông và hạ tầng kỹ thuật.
        </p>
        <p>
          Với đội ngũ kỹ sư giàu kinh nghiệm và năng lực được chứng nhận, chúng tôi cam kết cung cấp 
          giải pháp kỹ thuật chất lượng cao, tuân thủ tiêu chuẩn và đáp ứng mọi yêu cầu của khách hàng.
        </p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.7rem;
  align-items: start;
}

.about-card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 1.5rem;
}

.about-card p {
  margin: 0 0 0.9rem;
  color: var(--muted);
}

.about-card p:last-child {
  margin-bottom: 0;
}

.company-info {
  margin-top: 1rem;
  display: grid;
  gap: 0.4rem;
}

.company-info p {
  margin: 0;
  font-size: 0.95rem;
}

.company-info strong {
  color: var(--brand-deep);
  font-weight: 600;
}

@media (max-width: 860px) {
  .about-grid {
    grid-template-columns: 1fr;
  }
}
</style>
