<template>
  <section class="hero section">
    <div class="container hero-grid">
      <div class="hero-copy">
        <p class="eyebrow">Kỹ thuật cầu đường</p>
        <h1>Thiết kế hạ tầng dựa trên khảo sát cho giao thông an toàn và hiệu quả</h1>
        <p>
          Chúng tôi cung cấp dịch vụ tư vấn kỹ thuật xây dựng trọn gói cho cầu và tuyến đường,
          từ khảo sát hiện trường, phân tích tính khả thi đến hồ sơ thiết kế sẵn sàng thi công.
        </p>
        <div class="cta-row">
          <a class="btn btn-primary" href="#contact">Yêu cầu tư vấn</a>
          <a class="btn btn-secondary" href="#projects">Xem dự án</a>
        </div>
      </div>

      <div class="hero-panel">
        <div class="metric-card">
          <strong>150+ km</strong>
          <span>Thiết kế bình đồ và hình học tuyến đường</span>
        </div>
        <div class="metric-card">
          <strong>65+</strong>
          <span>Công trình cầu và cống đã triển khai</span>
        </div>
        <div class="metric-card">
          <strong>30%</strong>
          <span>Giảm trung bình khối lượng chỉnh sửa nhờ tích hợp khảo sát</span>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  position: relative;
  padding-top: 6.2rem;
  padding-bottom: 5.8rem;
}

.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background:
    linear-gradient(115deg, rgba(20, 52, 73, 0.88) 0%, rgba(31, 79, 115, 0.72) 45%, rgba(234, 143, 45, 0.26) 100%),
    url('../assets/hero-bridge.webp') center / cover no-repeat;
  z-index: -2;
}

.hero::after {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(180deg, rgba(15, 34, 47, 0) 0%, rgba(15, 34, 47, 0.32) 100%);
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 2rem;
  align-items: end;
}

.hero-copy {
  color: #f3f7fa;
  animation: rise 0.7s ease-out;
}

.eyebrow {
  margin: 0 0 0.7rem;
  font-family: 'Be Vietnam Pro', 'Segoe UI', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.09em;
  font-weight: 700;
  color: #ffd7a7;
}

.hero-copy h1 {
  max-width: 14ch;
  font-family: 'Be Vietnam Pro', 'Segoe UI', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.02em;
  line-height: 1.05;
  font-size: clamp(2rem, 4.2vw, 3.9rem);
}

.hero-copy p {
  margin: 0;
  max-width: 60ch;
  font-size: 1.05rem;
  line-height: 1.55;
}

.cta-row {
  display: flex;
  gap: 0.8rem;
  margin-top: 1.7rem;
  flex-wrap: wrap;
}

.btn {
  padding: 0.82rem 1.25rem;
  border-radius: 999px;
  font-weight: 700;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.btn:hover {
  transform: translateY(-2px);
}

.btn-primary {
  color: #102736;
  background: #f0b060;
  box-shadow: 0 10px 18px rgba(240, 176, 96, 0.25);
}

.btn-secondary {
  color: #f4f9fc;
  border: 1px solid rgba(244, 249, 252, 0.65);
  background: rgba(255, 255, 255, 0.05);
}

.hero-panel {
  display: grid;
  gap: 0.8rem;
  animation: rise 0.9s ease-out;
}

.metric-card {
  background: rgba(14, 36, 50, 0.75);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: var(--radius);
  padding: 1rem;
  color: #e6eff5;
}

.metric-card strong {
  display: block;
  font-family: 'Be Vietnam Pro', 'Segoe UI', sans-serif;
  font-size: 1.9rem;
  line-height: 1.05;
}

.metric-card span {
  color: #b8c9d5;
  font-size: 0.96rem;
}

@keyframes rise {
  from {
    opacity: 0;
    transform: translateY(14px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 920px) {
  .hero-grid {
    grid-template-columns: 1fr;
  }

  .hero-copy h1 {
    max-width: 16ch;
  }
}
</style>
