<script setup>
import designImg from "../assets/design.webp";
import supervisionImg from "../assets/supervision.avif";
import surveyImg from "../assets/survey-engineer.jpg";
import labImg from "../assets/lab-testing.avif";

const services = [
  {
    image: designImg,
    title: "Thiết kế & Thẩm tra thiết kế",
    items: [
      { name: "Dân dụng & Công nghiệp (Kiến trúc, Kết cấu, Điện, Cấp thoát nước)", rank: "Hạng III" },
      { name: "Giao thông (Đường bộ)", rank: "Hạng II" },
      { name: "Giao thông (Cầu)", rank: "Hạng III" },
      { name: "Hạ tầng kỹ thuật (Cấp, thoát nước)", rank: "Hạng II" },
    ],
  },
  {
    image: supervisionImg,
    title: "Giám sát thi công xây dựng",
    items: [
      { name: "Dân dụng & Công nghiệp", rank: "Hạng III" },
      { name: "Giao thông (Đường bộ)", rank: "Hạng II" },
      { name: "Giao thông (Cầu)", rank: "Hạng III" },
      { name: "Hạ tầng kỹ thuật (Cấp, thoát nước)", rank: "Hạng II" },
      { name: "Hạ tầng kỹ thuật (Chiếu sáng)", rank: "Hạng III" },
    ],
  },
  {
    image: surveyImg,
    title: "Khảo sát xây dựng",
    items: [
      { name: "Khảo sát địa hình", rank: "Hạng II" },
      { name: "Khảo sát địa chất", rank: "Hạng III" },
    ],
  },
  {
    image: labImg,
    title: "Thí nghiệm kiểm tra vật liệu",
    items: [
      { name: "Thử nghiệm chất lượng vật liệu công trình", rank: "Hạng III" },
    ],
  },
];
</script>

<template>
  <section id="services" class="section services">
    <div class="container">
      <h2 class="section-title">Dịch vụ</h2>
      <p class="section-subtitle">Chúng tôi cung cấp dịch vụ xuyên suốt vòng đời dự án, từ khảo sát nền đến thiết kế kỹ thuật cuối cùng và hỗ trợ triển khai.</p>

      <div class="services-grid">
        <article v-for="service in services" :key="service.title" class="service-card">
          <img :src="service.image" :alt="service.title" loading="lazy" class="service-img" />
          <h3>{{ service.title }}</h3>
          <ul class="service-items">
            <li v-for="(item, index) in service.items" :key="index">
              <span class="item-name">{{ item.name }}</span>
              <span class="item-rank">{{ item.rank }}</span>
            </li>
          </ul>
        </article>
      </div>
    </div>
  </section>
</template>

<style scoped>
.services {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.74) 0%, rgba(226, 235, 241, 0.86) 100%);
}

.services-grid {
  margin-top: 1.6rem;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.service-card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 1.2rem;
  transition: transform 0.2s ease;
}

.service-card:hover {
  transform: translateY(-4px);
}

.service-img {
  width: 100%;
  height: 140px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 0.9rem;
}

.service-card h3 {
  margin: 0;
  font-family: "Be Vietnam Pro", "Segoe UI", sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  color: var(--brand-deep);
  font-size: 1rem;
}

.service-items {
  margin: 0.9rem 0 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.6rem;
}

.service-items li {
  display: grid;
  gap: 0.25rem;
  font-size: 0.92rem;
  line-height: 1.4;
}

.item-name {
  color: var(--muted);
}

.item-rank {
  color: var(--accent);
  font-weight: 600;
  font-size: 0.85rem;
}

@media (max-width: 1060px) {
  .services-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 620px) {
  .services-grid {
    grid-template-columns: 1fr;
  }
}
</style>
