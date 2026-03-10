<template>
  <section id="about" class="section about">
    <div class="container about-grid">
      <div>
        <h2 class="section-title">Về chúng tôi</h2>
        <p class="section-subtitle">CÔNG TY TNHH TƯ VẤN KHẢO SÁT VÀ THIẾT KẾ XÂY DỰNG KHÁNH LY</p>
        <div class="company-info">
          <p><strong>Giấy CNĐKDN:</strong> 3701616836 (Cấp 22/09/2009)</p>
          <p><strong>Trụ sở chính:</strong> Số 44/50, đường 30/4, Thủ Dầu Một, HCM</p>
          <p><strong>Năng lực:</strong> Khảo sát (Hạng II-III), Thiết kế & Giám sát (Hạng II-III)</p>
        </div>
      </div>

      <div class="about-card">
        <p>Công ty TNHH Tư vấn Khảo sát Thiết kế Xây dựng Khánh Ly chuyên cung cấp dịch vụ khảo sát, thiết kế và giám sát kỹ thuật cho các dự án giao thông, dân dụng, công nghiệp và hạ tầng.</p>
        <p>
          Với đội ngũ kỹ sư có trình độ cao và năng lực được chứng nhận, chúng tôi cam kết mang đến giải pháp thiết kế hiệu quả, đáp ứng đầy đủ yêu cầu kỹ thuật, mỹ thuật, an toàn và hiệu quả đầu tư.
        </p>
        <p style="margin-top: 1rem; font-style: italic"><strong>Phương châm:</strong> Uy tín – Chất lượng – Hiệu quả</p>
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
